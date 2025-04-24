# Лабораторная работа №10

## Задание

Разработать графический интерфейс для списка задач (TODO-листа) с возможностью добавления, удаления и выбора задач.

1. Создать окно приложения с заголовком "Мой TODO-лист" и фиксированным размером.

2. Добавить Listbox для отображения списка задач.

3. Добавить поле ввода (Entry) для ввода новой задачи.

4. Добавить кнопки:

    "Добавить" — добавляет задачу в список.
    "Удалить" — удаляет выбранную задачу.
    "Очистить всё" — полностью очищает список.

<img src="./.repo/todo.png" />

## Теория

[Документация](https://metanit.com/python/tkinter/2.12.php)

**Listbox** — это виджет в tkinter, который отображает список элементов. Пользователь может добавлять, выбирать и удалять элементы.

### Создание Listbox

```python
listbox = tk.Listbox(root, width=30, height=5)
listbox.pack(pady=10)
```

### Добавление элементов

```python
listbox.insert(tk.END, "Элемент 1")
listbox.insert(tk.END, "Элемент 2")
listbox.insert(tk.END, "Элемент 3")

root.mainloop()
```

- _listbox = tk.Listbox(root, width=30, height=5)_ — создаёт список.
- _listbox.insert(tk.END, "Элемент")_ — добавляет элемент в конец списка.

### Выбор элемента в Listbox

Можно получить выделенный элемент с помощью curselection().

```python
def get_selected():
    selected = listbox.curselection()
    if selected:
        print("Выбрано:", listbox.get(selected[0]))

select_button = tk.Button(root, text="Выбрать", command=get_selected)
select_button.pack()
```

- _curselection()_ возвращает список индексов выделенных элементов.
- _get(index)_ возвращает текст элемента по индексу.

## Удаление элементов из Listbox

Удалить можно по индексу или все элементы сразу.

### Удаление выбранного элемента:

```python
def delete_selected():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

delete_button = tk.Button(root, text="Удалить", command=delete_selected)
delete_button.pack()
```

_Если ничего не выбрано, код ничего не делает._

### Очистка всего списка:

```python
listbox.delete(0, tk.END)
```



"""
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
