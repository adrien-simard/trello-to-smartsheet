# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-XX

### 🎨 Added
- **Modern UI Design**: Complete redesign with contemporary card-based layout
  - Trello blue color scheme (#0079BF)
  - Clean white cards on light gray background
  - Professional typography using Segoe UI
  - Improved spacing and visual hierarchy
  - Resizable window (900x700 default, min 800x600)

- **Enhanced User Experience**:
  - Eye/Lock emoji toggle (👁/🔒) for API token visibility
  - Rocket emoji 🚀 for Start Migration button
  - Better visual feedback with modern progress bar
  - Monospace font (Consolas) for log output

- **Version Numbering**: Added version display in window title and CLI output

- **Production-Ready Repository**:
  - MIT License
  - Comprehensive README with badges
  - CONTRIBUTING.md guidelines
  - GitHub Actions workflow for releases
  - Issue templates (bug reports, feature requests)
  - .gitignore for sensitive data
  - requirements.txt for pip users

### 🔧 Changed
- **Email Mapping Made Optional**:
  - Auto-generates emails as `firstname.lastname@epfl.ch` if no mapping file provided
  - Clear warnings and confirmation dialogs for missing mapping files

- **English UI**: All interface text and documentation in English

- **Improved Error Handling**: Better logging and user feedback

### 📚 Documentation
- Complete README overhaul with installation options
- Added CONTRIBUTING.md with development guidelines
- Created CLAUDE.md for AI-assisted development
- Added CHANGELOG.md for version tracking
- Created GitHub issue templates

### 🏗️ Technical
- Added `__version__.py` for centralized version management
- Improved code organization and structure
- Enhanced build process documentation

## [Previous Versions]

### Initial Release
- Core migration functionality
- GUI application with tkinter
- CLI interface support
- Trello JSON to Smartsheet conversion
- Comment migration as discussions
- Member and label support
- Card View (Kanban) lane structure

---

## Legend

- 🎨 Added: New features
- 🔧 Changed: Changes in existing functionality
- 🐛 Fixed: Bug fixes
- 🗑️ Deprecated: Soon-to-be removed features
- ❌ Removed: Removed features
- 🔒 Security: Security updates
- 📚 Documentation: Documentation changes
- 🏗️ Technical: Under-the-hood improvements
