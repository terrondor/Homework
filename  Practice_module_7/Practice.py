import tkinter
import os
from tkinter import filedialog, messagebox


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    if filename:
        text['text'] = 'Файл: ' + os.path.basename(filename)


def show_info():
    messagebox.showinfo('Информация', 'Инфа о приложении')


def show_about():
    messagebox.showinfo('О программе', 'Программа создана terrond в 2024 году, version: 1.0')


window = tkinter.Tk()
window.title('Проводник')
window.geometry('500x100')
window.configure(bg='silver')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=2, width=100, background='grey', foreground='white')
text.grid(column=1, row=0, padx=10, pady=10)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', command=file_select)
button_select.grid(column=1, row=1, pady=10)

menu = tkinter.Menu(window)
window.config(menu=menu)

help_menu = tkinter.Menu(menu)
menu.add_cascade(label='Справка', menu=help_menu)
help_menu.add_command(label='Информация', command=show_info)
help_menu.add_command(label='О программе', command=show_about)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.mainloop()
