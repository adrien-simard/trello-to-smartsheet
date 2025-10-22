# Release Checklist for Publishing

This document provides a step-by-step checklist for publishing this repository to GitHub and creating releases.

## 📋 Pre-Release Checklist

### Repository Setup
- [x] Initialize git repository
- [x] Create .gitignore to exclude sensitive data
- [x] Add LICENSE file (MIT)
- [x] Create comprehensive README.md
- [x] Add CONTRIBUTING.md guidelines
- [x] Add CHANGELOG.md
- [x] Create version management system
- [ ] Test that all Python files run without errors

### Code Quality
- [x] Add version numbers to application
- [x] Ensure all user-facing text is in English
- [x] Remove any hardcoded API tokens or sensitive data
- [x] Clean up temporary/test files
- [ ] Test the GUI application
- [ ] Test the CLI application
- [ ] Build and test the .exe file

### Documentation
- [x] README includes installation instructions
- [x] README includes usage examples
- [x] README includes troubleshooting section
- [x] CONTRIBUTING.md explains how to contribute
- [x] CLAUDE.md explains architecture for AI tools
- [x] Issue templates created
- [x] Pull request template created

### GitHub Setup
- [x] GitHub Actions workflow for releases
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Configure repository settings
- [ ] Add repository description and topics
- [ ] Enable Issues and Discussions

## 🚀 Publishing Steps

### 1. Create GitHub Repository

```bash
# On GitHub.com:
# 1. Click "New Repository"
# 2. Name: trello-to-smartsheet
# 3. Description: "Modern migration tool for converting Trello boards to Smartsheet with Kanban support"
# 4. Public repository
# 5. Do NOT initialize with README (we have one)
```

### 2. Push to GitHub

```bash
# Add all files
git add .

# Create initial commit
git commit -m "feat: initial release v1.0.0

- Modern UI with card-based layout and Trello blue theme
- Complete Trello to Smartsheet migration
- Preserves Kanban structure, comments, members, and labels
- Optional email mapping with auto-generation fallback
- Windows executable build support
- Comprehensive documentation and contributing guidelines
"

# Add remote (replace with your username)
git remote add origin https://github.com/yourusername/trello-to-smartsheet.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Configure Repository

On GitHub.com:
- **Settings → General**:
  - Add description
  - Add website (if any)
  - Add topics: `trello`, `smartsheet`, `migration`, `kanban`, `python`, `tkinter`

- **Settings → Features**:
  - ✅ Enable Issues
  - ✅ Enable Discussions (optional)
  - ✅ Enable Projects (optional)

- **About** (right sidebar):
  - Add description
  - Add topics
  - Add link to releases

### 4. Create First Release

```bash
# Tag the release
git tag -a v1.0.0 -m "Release v1.0.0 - Initial public release"
git push origin v1.0.0
```

The GitHub Action will automatically:
- Build the .exe file
- Create a GitHub Release
- Attach the .exe to the release

**OR manually create release:**
1. Go to Releases → "Create a new release"
2. Tag: `v1.0.0`
3. Title: `v1.0.0 - Initial Release`
4. Description: Copy from CHANGELOG.md
5. Upload `dist/TrelloToSmartsheet.exe` (build it locally first)
6. Publish release

## 📦 Building the Executable Locally

Before creating a release, test the build:

```bash
# Activate environment
conda activate trello-smartsheet

# Install PyInstaller
pip install pyinstaller

# Build
python build_lightweight.py

# Test the executable
.\dist\TrelloToSmartsheet.exe

# Check size (should be ~20-30 MB)
```

## 📢 Post-Release Tasks

### Announce the Release
- [ ] Post on relevant forums/communities
- [ ] Share on social media (if applicable)
- [ ] Notify team members or stakeholders
- [ ] Update any external documentation

### Monitor and Support
- [ ] Watch for issues and respond promptly
- [ ] Check GitHub Actions for build status
- [ ] Monitor download metrics
- [ ] Gather feedback from users

### Update Documentation
- [ ] Update README if needed based on feedback
- [ ] Add FAQ section for common questions
- [ ] Create Wiki pages for advanced topics (optional)

## 🔄 Future Release Process

For subsequent releases:

1. **Make changes** on a feature branch
2. **Update version** in `__version__.py`
3. **Update CHANGELOG.md** with changes
4. **Test thoroughly**
5. **Create PR** and get review (if team)
6. **Merge to main**
7. **Tag release**: `git tag v1.x.x`
8. **Push tag**: `git push origin v1.x.x`
9. **GitHub Action** builds and creates release automatically

## 🆘 Troubleshooting

### Build Fails
- Check Python version (should be 3.11)
- Ensure all dependencies installed
- Check for import errors
- Review build_lightweight.py logs

### GitHub Action Fails
- Check workflow file syntax
- Verify secrets are set (if needed)
- Check Python version in workflow
- Review action logs on GitHub

### Large Executable Size
- Verify exclusions in build_lightweight.py
- Check for unnecessary dependencies
- Consider using UPX compression (remove --noupx)

## 📊 Success Metrics

Track these after release:
- Number of downloads
- GitHub stars
- Issues opened/closed
- Pull requests
- User feedback
- Feature requests

## ✅ Final Checklist Before Publishing

- [ ] All code tested and working
- [ ] Documentation complete and accurate
- [ ] No sensitive data in repository
- [ ] .gitignore properly configured
- [ ] License file present
- [ ] Version numbers correct
- [ ] CHANGELOG up to date
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] First release created
- [ ] Release notes published
- [ ] .exe file tested and working

---

**Ready to publish?** Follow the steps above and share your tool with the community! 🚀
