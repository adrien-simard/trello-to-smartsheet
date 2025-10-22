"""
Script to build standalone executable for Trello to Smartsheet Migration Tool
"""

import subprocess
import sys
import os

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    print("Installing PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("PyInstaller installed successfully!\n")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")

    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Single file executable
        "--windowed",  # No console window
        "--name", "TrelloToSmartsheet",
        "--icon", "NONE",  # No icon for now
        "--add-data", "trello_to_smartsheet_kanban.py;.",  # Include the main module
        "--hidden-import", "smartsheet",
        "--hidden-import", "openpyxl",
        "trello_gui.py"
    ]

    try:
        subprocess.check_call(cmd)
        print("\n" + "="*60)
        print("SUCCESS! Executable created!")
        print("="*60)
        print("\nYou can find your executable at:")
        print("  dist/TrelloToSmartsheet.exe")
        print("\nFile size is optimized for distribution.")
        print("\nTo run: Simply double-click the .exe file")
    except subprocess.CalledProcessError as e:
        print(f"\nError building executable: {e}")
        print("Please make sure all dependencies are installed.")

if __name__ == "__main__":
    print("="*60)
    print("Trello to Smartsheet - Executable Builder")
    print("="*60)
    print()

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("PyInstaller found!")
    except ImportError:
        print("PyInstaller not found.")
        install_pyinstaller()

    build_executable()
