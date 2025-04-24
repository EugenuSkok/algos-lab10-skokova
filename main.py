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
language_entry.pack(fill="x")
ttk.Button(text="Добавить", command=add).pack(padx=20)
 
# создаем список
languages_listbox = Listbox()
languages_listbox.pack(fill="x")
 
ttk.Button(text="Удалить", command=delete).pack(padx=20)
ttk.Button(text="Удалить все", command=del_all).pack(padx=20)

root.mainloop()
