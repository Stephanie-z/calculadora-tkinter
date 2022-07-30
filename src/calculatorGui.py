import tkinter as tk
from typing import List, Callable


class CalculatorGui:
    """ Manages tkinter """

    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttonList: List[List[tk.Button]], calculator: Callable[[str], str]) -> None:
        self.root = root
        self.label = label
        self.display = display
        self.buttonList = buttonList
        self.calculator = calculator

    def start(self) -> None:
        """Start the gui"""
        self.configDisplay()
        self.configButtons()
        self.root.mainloop()

    def configDisplay(self) -> None:
        """Display configs"""
        display = self.display
        display.bind('<Return>', self.calculator)
        display.bind('<KP_Enter>', self.calculator)

    def configButtons(self) -> None:
        """Buttons configs"""
        buttonsList = self.buttonList
        for row in buttonsList:
            for button in row:
                buttonText = button['text']

                if buttonText == 'C':
                    button.bind('<Button-1>', self.clearDisplay)
                    button.config(bg='#EA4335', fg='#fff')

                if buttonText in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.addTextToDisplay)

                if buttonText == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#4785F4', fg='#fff')

    def calculate(self, event=None) -> None:
        """Solve equations"""
        equation = self.display.get()

        try:
            result = self.calculator(equation)

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{equation} = {result}')
        except OverflowError:
            self.label.config(text='Erro ao realizar cálculo: Overflow')
        except Exception:
            self.label.config(text='Conta inválida')

    def addTextToDisplay(self, event=None) -> None:
        """Add text to display"""
        self.display.insert('end', event.widget['text'])
        self.display.focus()

    def clearDisplay(self, event=None) -> None:
        """Clear display"""
        self.display.delete(0, 'end')