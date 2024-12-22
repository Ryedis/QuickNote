import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, ttk
from functions import *

def undo(text):
    text.edit_undo()

def redo(text):
    text.edit_redo()

def on_key(event, text):
    if event.char == " " or event.char == "\n":
        text.edit_separator()

def exit_editor(root):
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

def change_font(text, root):
    font_window = tk.Toplevel(root)
    font_window.title("Изменить шрифт")

    fonts = tkfont.families()

    search_entry = tk.Entry(font_window)
    search_entry.pack(side=tk.TOP, fill=tk.X)

    font_select = ttk.Combobox(font_window, values=fonts, state="normal", width=30)
    font_select.pack(side=tk.LEFT)

    tk.Label(font_window, text="Размер шрифта:").pack(side=tk.LEFT)
    size_entry = tk.Entry(font_window)
    size_entry.pack(side=tk.LEFT)
    
    def filter_fonts(event=None):
        query = search_entry.get().lower()
        filtered_fonts = [font for font in fonts if query in font.lower()]
        font_select['values'] = filtered_fonts
        if filtered_fonts:
            font_select.current(0)

    search_entry.bind("<KeyRelease>", filter_fonts)

    def apply_font():
        selected_font = font_select.get()
        font_size = int(size_entry.get()) if size_entry.get().isdigit() else 12
        if selected_font:
            text.config(font=(selected_font, font_size))

    tk.Button(font_window, text="Применить", command=apply_font).pack(side=tk.LEFT)

# Статистика текста
def show_stats(text):
    content = text.get("1.0", tk.END)
    char_count = len(content) - 1
    word_count = len(content.split())
    line_count = int(text.index("end").split(".")[0]) - 1
    messagebox.showinfo("Статистика", f"Символов: {char_count}\nСлов: {word_count}\nСтрок: {line_count}")

# Темы оформления
def toggle_theme(text):
    current_bg = text.cget("bg")
    if current_bg == "white":
        new_bg = "#272727"
        new_fg = "white"
        new_ib="white"
    else:
        new_bg = "white"
        new_fg = "#272727"
        new_ib="#272727"

    text.config(bg=new_bg, fg=new_fg, insertbackground=new_ib)

def on_key_press(event, text, root):
    if event.state & 0x4:  # Проверка нажатия Ctrl
        # Для отмены действия (Ctrl+Z или Ctrl+Я)
        if event.keycode == 90:  # keycode для 'z'
            undo(text)
        elif event.keycode == 1071:  # keycode для 'я'
            undo(text)

        # Для повторного действия (Ctrl+Y или Ctrl+Н)
        elif event.keycode == 89:  # keycode для 'y'
            redo(text)
        elif event.keycode == 1081:  # keycode для 'н'
            redo(text)

        # Для сохранения (Ctrl+S или Ctrl+Ы)
        elif event.keycode == 83:  # keycode для 's'
            save_file(text, root)
        elif event.keycode == 1067:  # keycode для 'ы'
            save_file(text, root)

        # Для выхода (Ctrl+Q или Ctrl+Й)
        elif event.keycode == 81:  # keycode для 'q'
            exit_editor(text)
        elif event.keycode == 1060:  # keycode для 'й'
            exit_editor(text)

        elif event.keysym == "equal":  # При нажатии на '+' (клавиша 'equal')
            increase_font(text)
        # Для уменьшения шрифта (Ctrl+Minus)
        elif event.keysym == "minus":  # При нажатии на '-'
            decrease_font(text)

        # Для копирования текста (Ctrl+C или Ctrl+С)
        elif event.keycode == 67:  # keycode для 'c'
            copy_text(text, root)
        elif event.keycode == 1057:  # keycode для 'с'
            copy_text(text, root)

        # Для вставки текста (Ctrl+V или Ctrl+Б)
        elif event.keycode == 86:  # keycode для 'v'
            paste_text(text, root)
        elif event.keycode == 1074:  # keycode для 'б'
            paste_text(text, root)

        # Для вырезания текста (Ctrl+X или Ctrl+Э)
        elif event.keycode == 88:  # keycode для 'x'
            cut_text(text, root)
        elif event.keycode == 1064:  # keycode для 'э'
            cut_text(text, root)
