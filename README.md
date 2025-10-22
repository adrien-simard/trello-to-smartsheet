# 🔄 Trello to Smartsheet Migration Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)]()

A modern, lightweight desktop application for migrating Trello boards to Smartsheet, preserving Kanban structure, cards, comments, and member assignments.

![Migration Tool Screenshot](https://via.placeholder.com/800x500/0079BF/FFFFFF?text=Trello+%E2%86%92+Smartsheet+Migration+Tool)

> 💡 **Perfect for teams** transitioning from Trello to Smartsheet while maintaining all project history and structure.

## Features

- **Complete Migration**: Imports cards, descriptions, due dates, members, labels, and comments
- **Kanban View Support**: Preserves list structure as lanes in Smartsheet Card View
- **Email Mapping**: Optional Excel file for custom email mappings
- **Auto-Generated Emails**: Automatically generates emails from names when no mapping file is provided
- **Folder Organization**: Optional folder ID to organize sheets
- **User-Friendly GUI**: Simple graphical interface for easy migration

## Prerequisites

- Windows OS
- Smartsheet account with API access
- Trello board exported as JSON

## 📥 Download

### Option 1: Windows Executable (Recommended for End Users)

1. Go to [Releases](../../releases)
2. Download the latest `TrelloToSmartsheet.exe`
3. Double-click to launch
4. No installation or Python required!

### Option 2: Run from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/trello-to-smartsheet.git
cd trello-to-smartsheet

# Install dependencies
pip install -r requirements.txt

# Run the GUI application
python trello_gui.py
```

## 🚀 Quick Start

### For End Users

1. **Download** the executable from [Releases](../../releases)
2. **Launch** `TrelloToSmartsheet.exe`
3. **Fill in** the required fields (see Usage section below)
4. **Click** 🚀 Start Migration

### For Developers

#### Using Conda (Recommended)

```bash
# Create environment
conda env create -f environment.yml
conda activate trello-smartsheet

# Run the application
python trello_gui.py
```

#### Using pip

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python trello_gui.py
```

#### Building the Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build optimized executable
python build_lightweight.py

# Output: dist\TrelloToSmartsheet.exe
```

## Getting Your Trello Board Data

1. Open your Trello board
2. Click "Show Menu" (top right)
3. Select "More" → "Print and Export"
4. Click "Export as JSON"
5. Save the file (e.g., `board.json`)

## Usage

### Application Fields

- **Trello JSON Export** (required): Select your exported Trello board JSON file
- **Smartsheet API Token** (required): Your Smartsheet API access token
  - Get it at: https://app.smartsheet.com/b/home?lx=paqhA4JOW6Y6XDE6V6OaSw
- **Folder ID** (optional): Numeric ID of the Smartsheet folder to create the sheet in
  - Leave empty to create in Home
- **Email Mapping File** (optional): Excel file (.xlsx) with name-to-email mappings
  - If not provided, emails will be auto-generated as `firstname.lastname@epfl.ch`

### Email Mapping File Format

If you want to provide custom email addresses, create an Excel file with this structure:

| Name | Email |
|------|-------|
| John Smith | john.smith@example.com |
| Jane Doe | jane.doe@example.com |

- **Column 1**: Full name (as it appears in Trello)
- **Column 2**: Corresponding email address
- **First row is the header** (will be skipped)

**Note**: If no mapping file is provided, the tool will automatically generate emails from member names.

## Using Card View in Smartsheet

After migration:

1. Open the newly created sheet in Smartsheet
2. Click the "Card View" button (top right toolbar)
3. Configure Card View:
   - Lane Field: Select "List"
   - Card Display: Customize which fields to show
4. The Trello lists will appear as vertical lanes
5. Drag and drop cards between lanes just like in Trello!

## Data Mapping

| Trello Element | Smartsheet Column | Type | Notes |
|----------------|-------------------|------|-------|
| Board Name | Sheet Name | - | Prefixed with "Trello Import - " |
| Lists | List | Dropdown | Used for Card View lanes |
| Card Title | Card Name | Text (Primary) | Main card identifier |
| Card Description | Description | Text | Full text preserved |
| Due Date | Due Date | Date | Formatted as YYYY-MM-DD |
| Members | Members | Multi-Contact | Auto-generated or from mapping file |
| Labels | Labels | Multi-Select | All label names |
| Card URL | URL | Text | Direct link to original Trello card |
| Comments | Discussions | - | Native Smartsheet discussions with author and timestamp |

## Sheet Structure

The created Smartsheet will have these columns:

1. **Card Name** (Text/Number, Primary)
2. **List** (Dropdown) - Contains all Trello list names
3. **Description** (Text/Number)
4. **Due Date** (Date)
5. **Members** (Multi-Contact List) - Smartsheet contacts
6. **Labels** (Multi-Select Dropdown) - All label names
7. **URL** (Text/Number)
8. **Created Date** (Date)

## Troubleshooting

### "Email mapping file not found"
- This is just a warning - the tool will continue with auto-generated emails
- Verify the file path if you want to use custom mappings
- Format: `firstname.lastname@epfl.ch`

### "Please enter your Smartsheet API token"
- Get your token at: https://app.smartsheet.com/b/home?lx=paqhA4JOW6Y6XDE6V6OaSw
- Make sure you copy the entire token
- Token should not have expired

### "Folder ID must be a number"
- Folder ID should be numeric only (e.g., `1234567890`)
- Leave empty to create sheet in Home

### "Migration failed: API error"

Common causes:
- Invalid API token
- Insufficient permissions in Smartsheet
- Rate limiting (too many requests)
- Network connectivity issues

Check the error message in the log for specific details.

### Comments not showing up

Comments are added as Smartsheet "Discussions." To view them:
1. Open the sheet
2. Click on a row
3. Look for the discussion icon or panel on the right

### Executable is too large
- The optimized build should be ~20-30 MB
- If larger, rebuild using `python build_lightweight.py`
- Ensure you're using the conda environment

## Limitations

- **Archived Items**: Archived lists and cards are excluded from migration
- **Attachments**: Not currently migrated (planned for future version)
- **Checklists**: Not currently migrated (planned for future version)
- **Card Cover Images**: Not preserved
- **Custom Fields**: Trello custom fields are not migrated

## Advanced Usage

### Migrating Multiple Boards

Simply run the application multiple times with different JSON files. Each board will create a separate Smartsheet.

### Command Line Usage

You can also run the migration from command line:

```bash
python trello_to_smartsheet_kanban.py board.json [api_token] [folder_id] [email_mapping.xlsx]
```

Or set environment variable:
```cmd
set SMARTSHEET_ACCESS_TOKEN=your_token_here
python trello_to_smartsheet_kanban.py board.json
```

## Technical Details

### Dependencies

- `smartsheet-python-sdk` - Smartsheet API client
- `openpyxl` - Excel file reading (for optional email mapping)
- `tkinter` - GUI framework (built-in with Python)

### Build Size

- Optimized executable: ~20-30 MB
- Excludes unnecessary packages (numpy, pandas, matplotlib, etc.)
- Uses Python 3.11 for optimal size and performance

## Security Notes

- **Never commit your API token** to version control
- Store the token securely (consider using a password manager)
- API tokens have the same permissions as your user account
- Revoke tokens you're no longer using in Smartsheet settings
- The application saves Folder ID and email mapping path locally (not the API token)

## Project Structure

```
smartsheets-trello/
├── trello_gui.py                    # GUI application
├── trello_to_smartsheet_kanban.py   # Migration logic
├── environment.yml                  # Conda environment config
├── build_lightweight.py             # Build script for exe
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── SETUP_INSTRUCTIONS.md            # Detailed setup guide
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Fork the repo and clone your fork
git clone https://github.com/yourusername/trello-to-smartsheet.git

# Create a branch
git checkout -b feature/your-feature-name

# Make changes and test
python trello_gui.py

# Submit a pull request
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section above
2. Search [existing issues](../../issues)
3. Create a [new issue](../../issues/new) with:
   - Description of the problem
   - Steps to reproduce
   - Migration log output
   - Expected vs actual behavior

## 🔗 Resources

- [Smartsheet API Documentation](https://smartsheet.redoc.ly/)
- [Trello Export Guide](https://support.atlassian.com/trello/docs/exporting-data-from-trello/)
- [Project Issues](../../issues)
- [Project Wiki](../../wiki)

## ⭐ Show Your Support

If this tool helped you, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📢 Sharing with others

## 📊 Next Steps After Migration

1. Open the created sheet in Smartsheet
2. Switch to **Card View** (top right menu)
3. Click "Card View Settings"
4. Set **Lane Field** to "List"
5. Customize card display fields as needed
6. Enjoy your Kanban board in Smartsheet!
