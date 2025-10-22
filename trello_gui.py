#!/usr/bin/env python3
"""
Trello to Smartsheet Migration - GUI Application

A graphical interface for migrating Trello boards to Smartsheet.
"""

import os
import sys
import threading
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

# Import version info
try:
    from __version__ import __version__
except ImportError:
    __version__ = "1.0.0"

# Import the migrator class
from trello_to_smartsheet_kanban import TrelloToSmartsheetMigrator


class TrelloMigrationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Trello to Smartsheet Migration Tool v{__version__}")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Variables
        self.json_file = tk.StringVar()
        self.api_token = tk.StringVar()
        self.folder_id = tk.StringVar()
        self.email_mapping_file = tk.StringVar()

        # Modern color scheme
        self.colors = {
            'primary': '#0079BF',      # Trello Blue
            'primary_dark': '#026AA7',
            'secondary': '#00C853',    # Success Green
            'background': '#F4F5F7',
            'surface': '#FFFFFF',
            'text_primary': '#172B4D',
            'text_secondary': '#5E6C84',
            'border': '#DFE1E6',
            'hover': '#EBECF0'
        }

        # Configure root background
        self.root.configure(bg=self.colors['background'])

        # Load saved settings
        self.load_settings()

        # Apply modern styling
        self.setup_styles()

        # Create UI
        self.create_widgets()

    def setup_styles(self):
        """Configure modern ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure colors
        style.configure('.',
            background=self.colors['background'],
            foreground=self.colors['text_primary'],
            borderwidth=0,
            focuscolor=self.colors['primary']
        )

        # Modern frame style
        style.configure('Card.TFrame',
            background=self.colors['surface'],
            relief='flat'
        )

        # Modern label styles
        style.configure('TLabel',
            background=self.colors['surface'],
            foreground=self.colors['text_primary'],
            font=('Segoe UI', 10)
        )

        style.configure('Title.TLabel',
            background=self.colors['surface'],
            foreground=self.colors['text_primary'],
            font=('Segoe UI', 24, 'bold')
        )

        style.configure('Subtitle.TLabel',
            background=self.colors['surface'],
            foreground=self.colors['text_secondary'],
            font=('Segoe UI', 10)
        )

        style.configure('FieldLabel.TLabel',
            background=self.colors['surface'],
            foreground=self.colors['text_secondary'],
            font=('Segoe UI', 9, 'bold')
        )

        # Modern entry style
        style.configure('Modern.TEntry',
            fieldbackground=self.colors['surface'],
            foreground=self.colors['text_primary'],
            borderwidth=1,
            relief='solid',
            padding=8,
            font=('Segoe UI', 10)
        )

        # Primary button style
        style.configure('Primary.TButton',
            background=self.colors['primary'],
            foreground='white',
            borderwidth=0,
            focuscolor='none',
            padding=(20, 10),
            font=('Segoe UI', 10, 'bold')
        )

        style.map('Primary.TButton',
            background=[('active', self.colors['primary_dark']),
                       ('pressed', self.colors['primary_dark'])]
        )

        # Secondary button style
        style.configure('Secondary.TButton',
            background=self.colors['surface'],
            foreground=self.colors['text_primary'],
            borderwidth=1,
            relief='solid',
            padding=(15, 8),
            font=('Segoe UI', 9)
        )

        style.map('Secondary.TButton',
            background=[('active', self.colors['hover']),
                       ('pressed', self.colors['hover'])]
        )

        # Modern progressbar
        style.configure('Modern.Horizontal.TProgressbar',
            background=self.colors['primary'],
            troughcolor=self.colors['border'],
            borderwidth=0,
            thickness=6
        )

    def create_widgets(self):
        # Header section with gradient-like effect
        header_frame = tk.Frame(self.root, bg=self.colors['surface'], height=100)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
        header_frame.grid_propagate(False)

        # Title with icon
        title_container = tk.Frame(header_frame, bg=self.colors['surface'])
        title_container.pack(expand=True)

        title_label = ttk.Label(
            title_container,
            text="🔄 Trello → Smartsheet",
            style='Title.TLabel'
        )
        title_label.pack(pady=(10, 5))

        subtitle_label = ttk.Label(
            title_container,
            text="Migrate your boards with ease",
            style='Subtitle.TLabel'
        )
        subtitle_label.pack()

        # Main content area with padding
        content_frame = tk.Frame(self.root, bg=self.colors['background'])
        content_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=30, pady=20)

        # Card-style frame for inputs
        input_card = ttk.Frame(content_frame, style='Card.TFrame', padding=25)
        input_card.pack(fill=tk.BOTH, expand=False, pady=(0, 20))

        # Trello JSON File
        row = 0
        ttk.Label(input_card, text="TRELLO JSON EXPORT", style='FieldLabel.TLabel').grid(
            row=row, column=0, sticky=tk.W, pady=(0, 5)
        )
        row += 1
        file_frame = ttk.Frame(input_card, style='Card.TFrame')
        file_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 15))

        self.json_entry = ttk.Entry(file_frame, textvariable=self.json_file, style='Modern.TEntry')
        self.json_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        ttk.Button(
            file_frame, text="Browse", command=self.browse_json_file, style='Secondary.TButton'
        ).pack(side=tk.RIGHT)

        # API Token
        row += 1
        ttk.Label(input_card, text="SMARTSHEET API TOKEN", style='FieldLabel.TLabel').grid(
            row=row, column=0, sticky=tk.W, pady=(0, 5)
        )
        row += 1
        token_frame = ttk.Frame(input_card, style='Card.TFrame')
        token_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 15))

        self.token_entry = ttk.Entry(token_frame, textvariable=self.api_token, show="*", style='Modern.TEntry')
        self.token_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.show_token_btn = ttk.Button(
            token_frame, text="👁", command=self.toggle_token_visibility, style='Secondary.TButton', width=3
        )
        self.show_token_btn.pack(side=tk.RIGHT)

        # Folder ID
        row += 1
        ttk.Label(input_card, text="FOLDER ID (OPTIONAL)", style='FieldLabel.TLabel').grid(
            row=row, column=0, sticky=tk.W, pady=(0, 5)
        )
        row += 1
        ttk.Entry(
            input_card, textvariable=self.folder_id, style='Modern.TEntry'
        ).grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 15))

        # Email Mapping File
        row += 1
        ttk.Label(input_card, text="EMAIL MAPPING FILE (OPTIONAL)", style='FieldLabel.TLabel').grid(
            row=row, column=0, sticky=tk.W, pady=(0, 5)
        )
        row += 1
        email_frame = ttk.Frame(input_card, style='Card.TFrame')
        email_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Entry(email_frame, textvariable=self.email_mapping_file, style='Modern.TEntry').pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10)
        )
        ttk.Button(
            email_frame, text="Browse", command=self.browse_email_file, style='Secondary.TButton'
        ).pack(side=tk.RIGHT)

        # Info label
        row += 1
        info_label = tk.Label(
            input_card,
            text="💡 No mapping file? Emails will be auto-generated as firstname.lastname@epfl.ch",
            font=("Segoe UI", 9),
            foreground=self.colors['text_secondary'],
            bg=self.colors['surface'],
            anchor='w'
        )
        info_label.grid(row=row, column=0, sticky=tk.W, pady=(5, 0))

        # Configure input card grid
        input_card.columnconfigure(0, weight=1)

        # Action buttons
        button_frame = ttk.Frame(content_frame, style='Card.TFrame', padding=20)
        button_frame.pack(fill=tk.X, pady=(0, 20))

        self.migrate_btn = ttk.Button(
            button_frame,
            text="🚀 Start Migration",
            command=self.start_migration,
            style='Primary.TButton'
        )
        self.migrate_btn.pack(side=tk.LEFT, padx=(0, 10))

        ttk.Button(
            button_frame,
            text="Clear Log",
            command=self.clear_log,
            style='Secondary.TButton'
        ).pack(side=tk.LEFT)

        # Log area card
        log_card = ttk.Frame(content_frame, style='Card.TFrame', padding=20)
        log_card.pack(fill=tk.BOTH, expand=True)

        ttk.Label(log_card, text="MIGRATION LOG", style='FieldLabel.TLabel').pack(
            anchor='w', pady=(0, 10)
        )

        # Log text with modern styling
        log_frame = tk.Frame(log_card, bg=self.colors['surface'])
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=12,
            state='disabled',
            wrap=tk.WORD,
            font=('Consolas', 9),
            bg='#F8F9FA',
            fg=self.colors['text_primary'],
            relief='flat',
            borderwidth=0,
            padx=10,
            pady=10
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Progress bar
        self.progress = ttk.Progressbar(
            log_card,
            mode='indeterminate',
            style='Modern.Horizontal.TProgressbar'
        )
        self.progress.pack(fill=tk.X, pady=(10, 0))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def browse_json_file(self):
        filename = filedialog.askopenfilename(
            title="Select Trello JSON Export",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.json_file.set(filename)

    def browse_email_file(self):
        filename = filedialog.askopenfilename(
            title="Select Email Mapping File",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if filename:
            self.email_mapping_file.set(filename)

    def toggle_token_visibility(self):
        if self.token_entry.cget('show') == '*':
            self.token_entry.config(show='')
            self.show_token_btn.config(text='🔒')
        else:
            self.token_entry.config(show='*')
            self.show_token_btn.config(text='👁')

    def log(self, message):
        """Add message to log area"""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        self.root.update()

    def clear_log(self):
        """Clear the log area"""
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state='disabled')

    def validate_inputs(self):
        """Validate user inputs"""
        if not self.json_file.get():
            messagebox.showerror("Error", "Please select a Trello JSON file")
            return False

        if not os.path.exists(self.json_file.get()):
            messagebox.showerror("Error", "Trello JSON file not found")
            return False

        if not self.api_token.get():
            messagebox.showerror("Error", "Please enter your Smartsheet API token")
            return False

        if self.folder_id.get():
            try:
                int(self.folder_id.get())
            except ValueError:
                messagebox.showerror("Error", "Folder ID must be a number")
                return False

        # Email mapping file is optional - if provided but doesn't exist, warn and clear
        if self.email_mapping_file.get() and not os.path.exists(self.email_mapping_file.get()):
            result = messagebox.askyesno(
                "Warning",
                "Email mapping file not found.\n\n" +
                "Emails will be auto-generated from names (firstname.lastname@epfl.ch).\n\n" +
                "Do you want to continue?"
            )
            if not result:
                return False
            self.email_mapping_file.set("")

        return True

    def save_settings(self):
        """Save settings to file"""
        try:
            settings_file = Path.home() / '.trello_smartsheet_settings.txt'
            with open(settings_file, 'w') as f:
                f.write(f"folder_id={self.folder_id.get()}\n")
                if self.email_mapping_file.get():
                    f.write(f"email_mapping={self.email_mapping_file.get()}\n")
        except:
            pass

    def load_settings(self):
        """Load saved settings"""
        try:
            settings_file = Path.home() / '.trello_smartsheet_settings.txt'
            if settings_file.exists():
                with open(settings_file, 'r') as f:
                    for line in f:
                        if line.startswith('folder_id='):
                            self.folder_id.set(line.split('=', 1)[1].strip())
                        elif line.startswith('email_mapping='):
                            path = line.split('=', 1)[1].strip()
                            if os.path.exists(path):
                                self.email_mapping_file.set(path)
        except:
            pass

    def start_migration(self):
        """Start the migration process"""
        if not self.validate_inputs():
            return

        # Save settings for next time
        self.save_settings()

        # Disable button
        self.migrate_btn.config(state='disabled')
        self.progress.start()
        self.clear_log()

        # Run migration in separate thread
        thread = threading.Thread(target=self.run_migration, daemon=True)
        thread.start()

    def run_migration(self):
        """Run the actual migration"""
        try:
            # Redirect stdout to log
            import io
            import sys

            class LogCapture:
                def __init__(self, gui):
                    self.gui = gui

                def write(self, text):
                    if text.strip():
                        self.gui.log(text.rstrip())

                def flush(self):
                    pass

            old_stdout = sys.stdout
            sys.stdout = LogCapture(self)

            # Get parameters
            json_file = self.json_file.get()
            api_token = self.api_token.get()
            folder_id = int(self.folder_id.get()) if self.folder_id.get() else None
            email_mapping = self.email_mapping_file.get() if self.email_mapping_file.get() else None

            self.log("=" * 60)
            self.log("Starting Trello to Smartsheet Migration")
            self.log("=" * 60)
            if email_mapping:
                self.log(f"Using email mapping file: {email_mapping}")
            else:
                self.log("No email mapping file - emails will be auto-generated")

            # Create migrator and run
            migrator = TrelloToSmartsheetMigrator(api_token, folder_id, email_mapping)
            sheet_id = migrator.migrate_board(json_file)

            self.log("=" * 60)
            self.log("MIGRATION COMPLETED SUCCESSFULLY!")
            self.log(f"Sheet ID: {sheet_id}")
            self.log("=" * 60)

            # Restore stdout
            sys.stdout = old_stdout

            # Show success message
            self.root.after(0, lambda: messagebox.showinfo(
                "Success",
                f"Migration completed successfully!\nSheet ID: {sheet_id}"
            ))

        except Exception as e:
            # Restore stdout
            sys.stdout = old_stdout

            error_msg = str(e)
            self.log(f"\n[ERROR] Migration failed: {error_msg}")

            # Show error message
            self.root.after(0, lambda: messagebox.showerror(
                "Error",
                f"Migration failed:\n{error_msg}"
            ))

        finally:
            # Re-enable button and stop progress
            self.root.after(0, lambda: self.migrate_btn.config(state='normal'))
            self.root.after(0, lambda: self.progress.stop())


def main():
    root = tk.Tk()
    app = TrelloMigrationGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
