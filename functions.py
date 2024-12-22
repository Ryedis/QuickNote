import tkinter as tk
from tkinter import filedialog, messagebox
import json

def open_file(text, root):
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "r", encoding="utf-8") as file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())
    root.title(f"QuickNote - {filepath}")

def save_file(text, root):
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text.get("1.0", tk.END))
    root.title(f"QuickNote - {filepath}")

def cut_text(text, root):
    root.clipboard_clear()
    root.clipboard_append(text.selection_get())
    text.delete("sel.first", "sel.last")

def copy_text(text, root):
    root.clipboard_clear()
    root.clipboard_append(text.selection_get())

def paste_text(text, root):
    text.insert(tk.INSERT, root.clipboard_get())

# Поиск и замена текста
def find_text(text, root):
    find_window = tk.Toplevel(root)
    find_window.title("Найти")
    tk.Label(find_window, text="Найти:").pack(side=tk.LEFT)
    search_entry = tk.Entry(find_window)
    search_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def search():
        start_pos = "1.0"
        word = search_entry.get()
        while True:
            start_pos = text.search(word, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(word)}c"
            text.tag_add("highlight", start_pos, end_pos)
            text.tag_config("highlight", background="yellow")
            start_pos = end_pos

    tk.Button(find_window, text="Найти", command=search).pack(side=tk.RIGHT)

def replace_text(text, root):
    replace_window = tk.Toplevel(root)
    replace_window.title("Заменить")
    tk.Label(replace_window, text="Найти:").grid(row=0, column=0)
    search_entry = tk.Entry(replace_window)
    search_entry.grid(row=0, column=1)

    tk.Label(replace_window, text="Заменить на:").grid(row=1, column=0)
    replace_entry = tk.Entry(replace_window)
    replace_entry.grid(row=1, column=1)

    def replace():
        word = search_entry.get()
        replacement = replace_entry.get()
        content = text.get("1.0", tk.END)
        new_content = content.replace(word, replacement)
        text.delete("1.0", tk.END)
        text.insert(tk.END, new_content)

    tk.Button(replace_window, text="Заменить", command=replace).grid(row=2, column=1)

def increase_font(text):
    current_font = text.cget("font")
    font_name, font_size = current_font.split()
    font_size = int(font_size)
    new_size = font_size + 1
    text.config(font=(font_name, new_size))

def decrease_font(text):
    current_font = text.cget("font")
    font_name, font_size = current_font.split()
    font_size = int(font_size)
    new_size = max(8, font_size - 1)
    text.config(font=(font_name, new_size))
    