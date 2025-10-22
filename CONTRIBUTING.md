# Contributing to Trello to Smartsheet Migration Tool

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 🌟 How to Contribute

### Reporting Bugs

Before creating a bug report, please:
1. Check the [existing issues](../../issues) to avoid duplicates
2. Use the latest version of the tool
3. Collect relevant information:
   - Operating system and version
   - Python version (if running from source)
   - Steps to reproduce the issue
   - Migration log output
   - Expected vs actual behavior

Create a detailed bug report with:
- Clear, descriptive title
- Step-by-step reproduction instructions
- Screenshots or log excerpts (remove sensitive data)
- Any error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
1. Check if the feature has already been suggested
2. Clearly describe the feature and its benefits
3. Explain use cases
4. Consider implementation complexity

### Pull Requests

#### Before You Start

1. **Fork the repository** and clone your fork
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   or
   ```bash
   git checkout -b fix/issue-description
   ```

#### Development Setup

```bash
# Create conda environment
conda env create -f environment.yml
conda activate trello-smartsheet

# Or use pip
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### Making Changes

1. **Follow the existing code style**:
   - Use 4 spaces for indentation
   - Follow PEP 8 guidelines
   - Add docstrings to functions and classes
   - Keep functions focused and modular

2. **Test your changes**:
   - Test with the GUI application
   - Test with the CLI interface
   - Test with various Trello board sizes
   - Test edge cases (empty boards, archived items, etc.)

3. **Document your changes**:
   - Update relevant documentation
   - Add comments for complex logic
   - Update CHANGES.md if applicable

#### Code Style Guidelines

```python
# Good example
def create_row_from_card(
    self,
    card: Dict[str, Any],
    column_map: Dict[str, int],
    list_lookup: Dict[str, str]
) -> Row:
    """
    Create a Smartsheet row from a Trello card.

    Args:
        card: Trello card object
        column_map: Dictionary mapping column names to column IDs
        list_lookup: Dictionary mapping list IDs to names

    Returns:
        Row object ready to be added to Smartsheet
    """
    # Implementation here
    pass
```

#### Submitting Pull Requests

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add support for custom fields"
   ```

2. **Use conventional commit messages**:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes (formatting)
   - `refactor:` - Code refactoring
   - `test:` - Adding or updating tests
   - `chore:` - Maintenance tasks

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Reference any related issues (#123)
   - Describe what changed and why
   - Include screenshots for UI changes
   - List any breaking changes

#### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Changes have been tested thoroughly
- [ ] Documentation has been updated
- [ ] Commit messages follow conventional format
- [ ] No sensitive data (API tokens, personal info) included
- [ ] All existing tests still pass
- [ ] New functionality includes appropriate error handling

## 🏗️ Project Structure

```
trello-to-smartsheet/
├── trello_to_smartsheet_kanban.py  # Core migration engine
├── trello_gui.py                    # GUI application
├── build_lightweight.py             # Build script for exe
├── environment.yml                  # Conda environment
├── requirements.txt                 # Pip requirements
└── README.md                        # Main documentation
```

### Key Components

- **TrelloToSmartsheetMigrator**: Main migration class
  - `load_trello_data()`: Parses Trello JSON
  - `create_sheet()`: Creates Smartsheet structure
  - `add_cards_to_sheet()`: Migrates card data
  - `add_comments_to_rows()`: Migrates comments

- **TrelloMigrationGUI**: GUI wrapper class
  - Modern tkinter interface
  - Threading for responsive UI
  - Settings persistence

## 🧪 Testing Guidelines

### Manual Testing

1. **Test with sample data**:
   - Small boards (< 10 cards)
   - Medium boards (10-100 cards)
   - Large boards (> 100 cards)

2. **Test edge cases**:
   - Empty boards
   - Boards with no comments
   - Cards without members
   - Cards without labels
   - Archived lists/cards
   - Special characters in names

3. **Test error handling**:
   - Invalid API tokens
   - Network issues
   - Missing Trello JSON file
   - Invalid folder IDs

### Automated Testing (Future)

We welcome contributions to add automated testing:
- Unit tests for core functions
- Integration tests for API calls
- UI tests for the GUI application

## 📋 Feature Requests

Current feature wish list:
- [ ] Support for attachments
- [ ] Support for checklists
- [ ] Support for custom fields
- [ ] Progress tracking with percentages
- [ ] Multi-board batch migration
- [ ] macOS and Linux support
- [ ] Undo/rollback functionality

Feel free to work on these or suggest new features!

## 🔒 Security

If you discover a security vulnerability:
1. **Do NOT** create a public issue
2. Email the maintainers directly
3. Include detailed information about the vulnerability
4. Allow time for a fix before public disclosure

## 💬 Questions?

- Open a [discussion](../../discussions) for questions
- Join our community chat (if available)
- Check the [wiki](../../wiki) for additional information

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## 🙏 Recognition

Contributors will be recognized in:
- The project README
- Release notes
- GitHub's contributor graph

Thank you for contributing to make this tool better! 🎉
