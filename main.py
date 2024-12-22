import tkinter as tk
import tkinter.font as tkfont
from gui import *
from functions import *
import os

def main():
    # Инициализация основного окна
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, 'icon.ico')
    
    root = tk.Tk()
    root.title("QuickNote")
    root.geometry("800x600")
    root.iconbitmap(icon_path)
    
    # Создаем фрейм для текста и ползунка
    frame = tk.Frame(root)
    frame.pack(expand=1, fill=tk.BOTH)
    
    # Текстовое поле
    text = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), undo=True)
    text.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
    text.config(bg="white", fg="#272727", insertbackground="#272727")
    
    # Ползунок прокрутки
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.config(yscrollcommand=scrollbar.set)

    # Привязка горячих клавиш
    text.bind("<Key>", lambda event: on_key(event, text))
    root.bind("<KeyPress>", lambda event: on_key_press(event, text, root))
    
    # Меню и остальная часть программы
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    # Меню Файл
    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(label="Открыть", command=lambda: open_file(text, root))
    file_menu.add_command(label="Сохранить", command=lambda: save_file(text, root))
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=lambda: exit_editor(root, "Arial", 12))
    menu.add_cascade(label="Файл", menu=file_menu)
    
    # Меню Правка
    edit_menu = tk.Menu(menu, tearoff=0)
    edit_menu.add_command(label="Вырезать", command=lambda: cut_text(text, root))
    edit_menu.add_command(label="Копировать", command=lambda: copy_text(text, root))
    edit_menu.add_command(label="Вставить", command=lambda: paste_text(text, root))
    edit_menu.add_command(label="Отменить", command=lambda: undo(text))
    edit_menu.add_command(label="Повторить", command=lambda: redo(text))
    menu.add_cascade(label="Правка", menu=edit_menu)
    
    # Меню Поиск
    find_menu = tk.Menu(menu, tearoff=0)
    find_menu.add_command(label="Найти", command=lambda: find_text(text, root))
    find_menu.add_command(label="Заменить", command=lambda: replace_text(text, root))
    menu.add_cascade(label="Поиск", menu=find_menu)
    
    # Меню Формат
    format_menu = tk.Menu(menu, tearoff=0)
    format_menu.add_command(label="Изменить шрифт", command=lambda: change_font(text, root))
    menu.add_cascade(label="Формат", menu=format_menu)
    
    # Меню Инструменты
    tools_menu = tk.Menu(menu, tearoff=0)
    tools_menu.add_command(label="Статистика текста", command=lambda: show_stats(text))
    menu.add_cascade(label="Инструменты", menu=tools_menu)
    
    # Меню Вид
    view_menu = tk.Menu(menu, tearoff=0)
    view_menu.add_command(label="Переключить тему", command=lambda: toggle_theme(text))
    view_menu.add_command(label="Увеличить шрифт", command=lambda: increase_font(text))
    view_menu.add_command(label="Уменьшить шрифт", command=lambda: decrease_font(text))
    menu.add_cascade(label="Вид", menu=view_menu)
    
    # Запуск основного цикла
    root.mainloop()

if __name__ == "__main__":
    main()