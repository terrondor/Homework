import tkinter
import os
from tkinter import filedialog, messagebox, scrolledtext


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    if filename:
        text['text'] = 'Файл: ' + os.path.basename(filename)
        read_file(filename)


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
            text_area.delete(1.0, tkinter.END)
            text_area.insert(tkinter.END, file_content)
    except Exception as e:
        messagebox.showerror('Ошибка', f'Не удалось открыть файл: {e}')


def search_text():
    search_query = search_entry.get()
    content = text_area.get(1.0, tkinter.END)
    if search_query in content:
        messagebox.showinfo('Результат поиска', f'"{search_query}" найдено в файле.')
    else:
        messagebox.showinfo('Результат поиска', f'"{search_query}", не найдено.')


def show_info():
    messagebox.showinfo('Информация', 'Инфа о приложении')


def show_about():
    messagebox.showinfo('О программе', 'Программа создана terrond в 2024 году, version: 1.0')


window = tkinter.Tk()
window.title('Проводник')
window.geometry('800x600')
window.configure(bg='silver')
window.resizable(False, False)

text = tkinter.Label(window, text='Файл:', height=2, width=100, background='grey', foreground='white')
text.grid(column=1, row=0, padx=10, pady=10)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', command=file_select)
button_select.grid(column=1, row=1, pady=10)

search_entry = tkinter.Entry(window, width=30)
search_entry.grid(column=1, row=20, padx=10, pady=10)

search_button = tkinter.Button(window, width=20, height=2, text='Поиск', command=search_text)
search_button.grid(column=1, row=3, pady=10)

text_area = scrolledtext.ScrolledText(window, width=70, height=15)
text_area.grid(column=1, row=4, padx=10, pady=10)

menu = tkinter.Menu(window)
window.config(menu=menu)

help_menu = tkinter.Menu(menu)
menu.add_cascade(label='Справка', menu=help_menu)
help_menu.add_command(label='Информация', command=show_info)
help_menu.add_command(label='О программе', command=show_about)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.mainloop()
