from calculatorFactories import makeRoot, makeDisplay, makeLabel, makeButtons
from calculatorGui import CalculatorGui
from calculatorActions import calculate


def main():
    root = makeRoot()
    display = makeDisplay(root, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = makeLabel(root, row=0, column=0, columnspan=5, sticky='news')
    buttons = makeButtons(root, startingRow=2)

    calculator = CalculatorGui(root, label, display, buttons, calculate)
    calculator.start()


if __name__ == '__main__':
    main()
