from tkinter import *
from tkinter import ttk
 
 
# удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
 
 
# добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)

def del_all():
    languages_listbox.delete(0, END)
 
 
root = Tk()
root.title("METANIT.COM")
root.geometry("300x250")
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
 
# текстовое поле и кнопка для добавления в список
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
 
# создаем список
languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
ttk.Button(text="Удалить", command=delete).grid(row=1, column=1, padx= 2, pady=2)
ttk.Button(text="Удалить все", command=del_all).grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
