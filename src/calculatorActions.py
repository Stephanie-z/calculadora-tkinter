import re
import math


def deleteInvalidChars(equation: str) -> str:
    cleaned = equation
    # Remove todos os caracteres invalidos - caracteres != [0123456789./*-+^e]
    cleaned = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', cleaned, 0)
    # Remove os operadores duplicados (.+/-*^)
    cleaned = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', cleaned, 0)
    # Remove patenteses vazios - *() ou () 
    cleaned = re.sub(r'\*?\(\)', '', cleaned)
    return cleaned


def solveExponentiations(equation: str) -> str:
    exponentiationRegex = re.compile(r'\d+\.?\d*(?:\^|\*\*)\d+\.?\d*', flags=re.S)
    newEquation = deleteInvalidChars(equation)
    foundEquations = exponentiationRegex.findall(newEquation)
    while foundEquations:
        for equation in foundEquations:
            firstNumber, secondNumber = re.split(r'(?:\^|\*\*)', equation)
            solved = math.pow(float(firstNumber), float(secondNumber))
            newEquation = newEquation.replace(equation, str(solved), 1)
        foundEquations = exponentiationRegex.findall(newEquation)
    return newEquation


def solveParentheses(equation: str) -> str:
    parenthesesRegex = re.compile(r'\([\d\^\/\*\-\+\.]+\)', flags=re.S)
    newEquation = deleteInvalidChars(equation)
    foundEquations = parenthesesRegex.findall(newEquation)
    while foundEquations:
        for equation in foundEquations:
            exponentiationsSolved = solveExponentiations(equation)
            result = eval(deleteInvalidChars(exponentiationsSolved))
            newEquation = newEquation.replace(equation, str(result), 1)
        foundEquations = parenthesesRegex.findall(newEquation)
    return newEquation


def calculate(equation: str) -> str:
    cleanedEquation = deleteInvalidChars(equation)
    try:
        eqParentesesSolved = solveParentheses(cleanedEquation)
        eqExponentiationSolved = solveExponentiations(eqParentesesSolved)
        successfullySolvedEquation = eval(eqExponentiationSolved)
        return str(successfullySolvedEquation)
    except Exception:
        raise