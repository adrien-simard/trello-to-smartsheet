# 🚀 Quick Start Guide

Get up and running in less than 5 minutes!

## For End Users (Windows)

### 1️⃣ Download
- Go to [Releases](../../releases)
- Download `TrelloToSmartsheet.exe`

### 2️⃣ Prepare Your Data
**Export from Trello:**
1. Open your Trello board
2. Click "Show Menu" (top right)
3. Select "More" → "Print and Export"
4. Click "Export as JSON"
5. Save the file

**Get Smartsheet API Token:**
1. Go to [Smartsheet Account](https://app.smartsheet.com/b/home?lx=paqhA4JOW6Y6XDE6V6OaSw)
2. Click "API Access" or "Apps & Integrations"
3. Generate new access token
4. Copy the token

### 3️⃣ Run Migration
1. Double-click `TrelloToSmartsheet.exe`
2. Fill in the fields:
   - **Trello JSON Export**: Browse to your .json file
   - **Smartsheet API Token**: Paste your token
   - **Folder ID**: (Optional) Numeric folder ID
   - **Email Mapping**: (Optional) .xlsx file with name↔email mapping
3. Click **🚀 Start Migration**
4. Wait for completion
5. Open your new sheet in Smartsheet!

### 4️⃣ Enable Card View (Kanban)
In Smartsheet:
1. Open the new sheet
2. Click "Card View" (top right)
3. Click "Card View Settings"
4. Set **Lane Field** to "List"
5. Customize card display as needed

## For Developers

### Option 1: Using Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/trello-to-smartsheet.git
cd trello-to-smartsheet

# Create environment
conda env create -f environment.yml
conda activate trello-smartsheet

# Run the GUI
python trello_gui.py

# Or run CLI
python trello_to_smartsheet_kanban.py board.json
```

### Option 2: Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/trello-to-smartsheet.git
cd trello-to-smartsheet

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python trello_gui.py
```

### Build Your Own Executable

```bash
# Make sure you're in the environment
conda activate trello-smartsheet

# Install PyInstaller
pip install pyinstaller

# Build
python build_lightweight.py

# Output will be in:
dist\TrelloToSmartsheet.exe
```

## Troubleshooting

### "Please enter your Smartsheet API token"
→ Make sure you've pasted your API token from Smartsheet

### "Trello JSON file not found"
→ Make sure you've selected the correct .json file from Trello export

### "Folder ID must be a number"
→ Leave it empty or use only numeric values (e.g., 1234567890)

### "Email mapping file not found"
→ This is optional. Click "Yes" to continue with auto-generated emails

### Migration fails with API error
→ Check your API token is valid and not expired
→ Verify you have permissions in Smartsheet
→ Check your internet connection

## Need More Help?

- 📖 **Full Documentation**: [README.md](README.md)
- 🐛 **Report Bug**: [Create Issue](../../issues/new?template=bug_report.md)
- 💡 **Feature Request**: [Create Issue](../../issues/new?template=feature_request.md)
- 💬 **Ask Question**: [Discussions](../../discussions)

## Tips for Best Results

✅ **Start Small**: Test with a small board first (< 10 cards)
✅ **Use Email Mapping**: For accurate member assignment
✅ **Check Archives**: Archived lists/cards are not migrated
✅ **Verify Card View**: Set up Card View in Smartsheet after migration
✅ **Review Comments**: Comments appear in the discussions panel

## What Gets Migrated

| Trello | → | Smartsheet |
|--------|---|------------|
| Board Name | → | Sheet Name |
| Lists | → | Dropdown (Card View lanes) |
| Cards | → | Rows |
| Card Title | → | Primary Column |
| Description | → | Description Column |
| Due Date | → | Date Column |
| Members | → | Multi-Contact Column |
| Labels | → | Multi-Select Column |
| Comments | → | Discussions |
| Card URL | → | URL Column |

## What's NOT Migrated

❌ Attachments (planned for future)
❌ Checklists (planned for future)
❌ Custom fields
❌ Archived items
❌ Card cover images

---

**Ready to migrate?** Download now and get started! 🎉

[⬇️ Download Latest Release](../../releases/latest)
