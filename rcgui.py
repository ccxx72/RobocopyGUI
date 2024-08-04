import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from localization import translations, robocopy_options
import subprocess
from ttkthemes import ThemedTk
import json
import os

CONFIG_FILE = "config.json"

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#FFFFEA", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()

class RobocopyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robocopy GUI")

        self.load_config()

        self.master.geometry(f"{self.window_width}x{self.window_height}")

        self.style = ttk.Style(self.master)
        self.style.theme_use(initial_theme)

        self.source_path = tk.StringVar()
        self.destination_path = tk.StringVar()
        self.language_var = tk.StringVar(value=self.current_language)
        self.theme_var = tk.StringVar(value=self.current_theme)
        self.selected_options = {}

        self.setup_ui()

        self.master.bind("<Configure>", self.on_resize)

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                config = json.load(file)
                self.current_language = config.get('language', 'en')
                self.current_theme = config.get('theme', 'arc')
                self.window_width = config.get('window_width', 900)
                self.window_height = config.get('window_height', 700)
        else:
            self.current_language = 'en'
            self.current_theme = 'arc'
            self.window_width = 900
            self.window_height = 700

    def save_config(self):
        config = {
            'language': self.current_language,
            'theme': self.current_theme,
            'window_width': self.master.winfo_width(),
            'window_height': self.master.winfo_height()
        }
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file)

    def get_text(self, key):
        return translations[self.current_language][key]

    def setup_ui(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        # Top section
        top_frame = ttk.Frame(self.master, padding="10 10 10 0")
        top_frame.grid(row=0, column=0, sticky="ew")

        ttk.Label(top_frame, text=self.get_text('language'), style="TLabel").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        language_menu = ttk.Combobox(top_frame, textvariable=self.language_var, values=['en', 'it'], state='readonly', width=5)
        language_menu.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        language_menu.bind('<<ComboboxSelected>>', self.change_language)

        ttk.Label(top_frame, text=self.get_text('source'), style="TLabel").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(top_frame, textvariable=self.source_path, width=50).grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        browse_source_btn = ttk.Button(top_frame, text=self.get_text('browse'), command=self.browse_source, style="TButton")
        browse_source_btn.grid(row=1, column=2, padx=5, pady=5)
        ToolTip(browse_source_btn, "Select source directory")

        ttk.Label(top_frame, text=self.get_text('destination'), style="TLabel").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(top_frame, textvariable=self.destination_path, width=50).grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        browse_dest_btn = ttk.Button(top_frame, text=self.get_text('browse'), command=self.browse_destination, style="TButton")
        browse_dest_btn.grid(row=2, column=2, padx=5, pady=5)
        ToolTip(browse_dest_btn, "Select destination directory")

        # Theme selection
        ttk.Label(top_frame, text="Theme:", style="TLabel").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        theme_menu = ttk.Combobox(top_frame, textvariable=self.theme_var, values=self.master.get_themes(), state='readonly', width=20)
        theme_menu.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        theme_menu.bind('<<ComboboxSelected>>', self.change_theme)

        # Middle section with tabs
        tab_control = ttk.Notebook(self.master)
        tab_control.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.option_listboxes = []
        for i, category in enumerate(self.get_text('option_categories')):
            tab = ttk.Frame(tab_control, padding=10)
            tab_control.add(tab, text=category)

            listbox = tk.Listbox(tab, selectmode=tk.MULTIPLE, exportselection=False, bg="white", selectbackground="#a6a6a6")
            listbox.pack(expand=True, fill="both")
            scrollbar = ttk.Scrollbar(listbox, orient=tk.VERTICAL)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            self.option_listboxes.append(listbox)
            listbox.bind('<<ListboxSelect>>', lambda e, index=i: self.on_select(e, index))

        self.populate_listboxes()

        # Bottom section
        bottom_frame = ttk.Frame(self.master, padding="10 0 10 10")
        bottom_frame.grid(row=2, column=0, sticky="ew")

        ttk.Label(bottom_frame, text=self.get_text('command_preview'), style="TLabel").pack(anchor="w")
        self.command_preview = tk.Text(bottom_frame, height=3, bg="white", wrap=tk.WORD)
        self.command_preview.pack(fill="x", expand=True, pady=5)

        run_button = ttk.Button(bottom_frame, text=self.get_text('run_robocopy'), command=self.run_robocopy, style="Accent.TButton")
        run_button.pack(pady=10)
        ToolTip(run_button, "Execute Robocopy command")

        # Status bar
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.master, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, sticky="ew")

        self.update_command()
        self.status_var.set("Ready")

    def change_language(self, event):
        self.current_language = self.language_var.get()
        self.save_config()
        self.master.title(self.get_text('title'))
        self.setup_ui()

    def change_theme(self, event):
        theme = self.theme_var.get()
        self.master.set_theme(theme)
        self.current_theme = theme
        self.save_config()

    def populate_listboxes(self):
        options = robocopy_options[self.current_language]
        for i, option_list in enumerate(options):
            self.option_listboxes[i].delete(0, tk.END)
            for option in option_list:
                self.option_listboxes[i].insert(tk.END, option)
        
        # Restore selections after populating
        for i, listbox in enumerate(self.option_listboxes):
            if i in self.selected_options:
                for index in self.selected_options[i]:
                    listbox.selection_set(index)

    def on_select(self, event, listbox_index):
        listbox = event.widget
        selected_indices = listbox.curselection()
        self.selected_options[listbox_index] = selected_indices
        self.update_command()

    def update_command(self):
        source = self.source_path.get()
        destination = self.destination_path.get()
        selected_options = []
        for i, listbox in enumerate(self.option_listboxes):
            if i in self.selected_options:
                selected_options.extend([listbox.get(index).split(' - ')[0] for index in self.selected_options[i]])
        options = ' '.join(selected_options)
        command = f'robocopy "{source}" "{destination}" {options}'
        self.command_preview.delete(1.0, tk.END)
        self.command_preview.insert(tk.END, command)

    def browse_source(self):
        self.source_path.set(filedialog.askdirectory())
        self.update_command()

    def browse_destination(self):
        self.destination_path.set(filedialog.askdirectory())
        self.update_command()

    def run_robocopy(self):
        command = self.command_preview.get(1.0, tk.END).strip()
        
        if not self.source_path.get() or not self.destination_path.get():
            messagebox.showerror(self.get_text('error_title'), self.get_text('error_message'))
            return

        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            messagebox.showinfo("Success", "Robocopy command executed successfully.")
            self.status_var.set("Robocopy command executed successfully")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Robocopy command failed: {e}")
            self.status_var.set("Robocopy command failed")

    def on_resize(self, event):
        self.save_config()

if __name__ == "__main__":
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            initial_theme = config.get('theme', 'arc')
    else:
        initial_theme = 'arc'

    root = ThemedTk(theme=initial_theme)
    app = RobocopyGUI(root)
    root.mainloop()
