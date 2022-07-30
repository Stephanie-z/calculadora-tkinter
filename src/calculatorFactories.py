import tkinter as tk
from typing import List


def makeRoot() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def makeLabel(root, **gridOptions) -> tk.Label:
    label = tk.Label(root, text='', anchor='e', justify='right', background='#fff')
    label.grid(**gridOptions)
    return label


def makeDisplay(root, **gridOptions) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(**gridOptions)
    display.config( font=('Helvetica', 40, 'bold'), justify='right', bd=1, relief='flat', highlightthickness=1, highlightcolor='#ccc')
    display.bind('<Control-a>', displayControlA)
    return display


def displayControlA(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def makeButton(root, text, **gridOptions) -> tk.Button:
    btn = tk.Button(root, text=text)
    btn.grid(**gridOptions)
    btn.config(font=('Helvetica', 15, 'normal'), pady=40, width=1, background='#f1f2f3', bd=0, cursor='hand2', highlightthickness=0, highlightcolor='#ccc', activebackground='#ccc', highlightbackground='#ccc')
    return btn


def makeButtons(root, startingRow) -> List[List[tk.Button]]:
    buttonTexts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, rowValue in enumerate(buttonTexts, start=startingRow):
        buttonRow = []
        for col, colValue in enumerate(rowValue):
            btn = makeButton(root, text=colValue, row=row, column=col, sticky='news', padx=5, pady=5)
            buttonRow.append(btn)
        buttons.append(buttonRow)
    return buttons