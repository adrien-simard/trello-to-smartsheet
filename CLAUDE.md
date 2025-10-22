# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Trello to Smartsheet migration tool** that converts Trello boards (from JSON exports) into Smartsheet sheets with Kanban Card View support. The project includes both a command-line interface and a GUI application, and can be packaged as a standalone Windows executable.

## Core Architecture

### Two-Layer Application Structure

1. **Migration Engine** (`trello_to_smartsheet_kanban.py`)
   - `TrelloToSmartsheetMigrator` class handles all migration logic
   - Reads Trello JSON exports and creates corresponding Smartsheet sheets
   - Preserves structure: Trello lists → Smartsheet dropdown values (for Card View lanes)
   - Preserves data: cards → rows, comments → discussions, members → multi-contact lists
   - Email generation/mapping: Auto-generates emails as `firstname.lastname@epfl.ch` or uses provided Excel mapping

2. **GUI Wrapper** (`trello_gui.py`)
   - tkinter-based desktop application
   - Wraps the migration engine with user-friendly interface
   - Manages settings persistence in `~/.trello_smartsheet_settings.txt`
   - Runs migration in separate thread to keep UI responsive

### Data Flow

```
Trello JSON Export
    ↓
TrelloToSmartsheetMigrator
    ├─ Parse JSON (boards, lists, cards, members, labels, actions)
    ├─ Create Smartsheet with columns (Card Name, List, Description, Due Date, Members, Labels, URL, Created Date)
    ├─ Map Trello lists → Smartsheet PICKLIST options (for Card View lanes)
    ├─ Map Trello labels → Smartsheet MULTI_PICKLIST options
    ├─ Generate/lookup member emails (auto-generate or from Excel mapping)
    ├─ Add cards as rows with proper cell types (contacts, dates, multi-select)
    └─ Add comments as native Smartsheet discussions on rows
        ↓
Smartsheet Sheet (ready for Card View)
```

## Development Commands

### Environment Setup

```bash
# Create and activate conda environment
conda env create -f environment.yml
conda activate trello-smartsheet
```

### Running the Application

```bash
# Run GUI application
python trello_gui.py

# Run CLI migration directly
python trello_to_smartsheet_kanban.py <board.json> [api_token] [folder_id] [email_mapping.xlsx]

# Or with environment variable
set SMARTSHEET_ACCESS_TOKEN=your_token
python trello_to_smartsheet_kanban.py board.json
```

### Building the Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build optimized lightweight executable (~20-30 MB)
python build_lightweight.py

# Output: dist\TrelloToSmartsheet.exe
```

The build script excludes unnecessary packages (numpy, pandas, matplotlib, scipy, PIL) to minimize size.

## Key Implementation Details

### Smartsheet Column Types and Mapping

- **Card Name** (TEXT_NUMBER, Primary): Trello card title
- **List** (PICKLIST): Trello list name - critical for Card View lanes
- **Description** (TEXT_NUMBER): Trello card description
- **Due Date** (DATE): Formatted as YYYY-MM-DD from ISO 8601
- **Members** (MULTI_CONTACT_LIST): Uses `object_value` with MULTI_CONTACT format
- **Labels** (MULTI_PICKLIST): Uses `object_value` with MULTI_PICKLIST format
- **URL** (TEXT_NUMBER): Direct link to original Trello card
- **Created Date** (DATE): From Trello's dateLastActivity

### Email Handling Strategy

The migrator supports two modes for member email addresses:

1. **Auto-generation** (default): Converts "John SMITH" → "john.smith@epfl.ch"
   - Implementation in `generate_email_from_name()`: splits name, takes first and last parts

2. **Excel mapping file** (optional): Two-column format (Name | Email)
   - Loaded via `openpyxl` in `load_email_mapping()`
   - Supports case-insensitive matching

### Smartsheet API Patterns

- **Sheet creation**: Use `Folders.create_sheet_in_folder()` or `Home.create_sheet()` depending on folder_id
- **Column options**: Set PICKLIST and MULTI_PICKLIST options during sheet creation with extracted list/label names
- **Multi-value cells**: Use `object_value` with proper `objectType` (MULTI_CONTACT or MULTI_PICKLIST)
- **Discussions**: Use `Discussions.create_discussion_on_row()` with formatted text including author and timestamp

### Comment Migration Strategy

Trello comments are converted to Smartsheet discussions:
- Extract `commentCard` actions from Trello's actions array
- Format: `[Author Name (email) - YYYY-MM-DD HH:MM]\nComment text`
- Added to corresponding row via discussions API
- Preserves author attribution and timestamps

## Important Constraints

1. **Archived items excluded**: Filtered using `closed` field in lists/cards
2. **Sheet name limit**: Smartsheet limits to 50 characters (auto-truncated)
3. **Thread-safe GUI**: Migration runs in separate thread via `threading.Thread`
4. **API error handling**: All Smartsheet operations wrapped in try-except
5. **Batch operations**: Rows added in single batch call for efficiency

## Testing Approach

When testing or making changes:
- Use small Trello JSON exports first (fewer cards/comments)
- Verify Card View works: Lane Field must be set to "List" column
- Check multi-contact cells display correctly (proper email format required)
- Test both with and without email mapping file
- Verify comments appear in discussions panel on rows
