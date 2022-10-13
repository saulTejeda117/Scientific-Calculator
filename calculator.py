from tkinter import *
from turtle import right

from sympy import * 

# Operciones básicas

# Integración
# Derivación

def main():
    operationsList = []
    # Mainwindow features
    mainWindow = Tk()
    mainWindow.title('Calculadora')
    mainWindow.configure(width = 320, height = 500)
    mainWindow.resizable(False, False)

    Label(mainWindow, text = operationsList, name = 'operations', font=('Helvetica', 20), justify='right').place(x = 10, y = 0)
    Label(mainWindow, text = operationsList, name = 'results', font=('Helvetica', 30), justify=RIGHT).place(x = 10, y = 50)

    resultLabel = mainWindow.nametowidget('results')
    operationsLabel = mainWindow.nametowidget('operations')

    # Clear screen
    def clean():
        operationsList.clear()
        resultLabel.configure(text = operationsList)
        operationsLabel.configure(text = operationsList)

    # Add an element to make an operation
    def add_elementList(element):
        operationsList.append(element)
        resultLabel.configure(text = operationsList)
        
    # Make the operation 
    def show_result(result):
        resultLabel.configure(text = str(result))
        operationsLabel.configure(text = operationsList)
        # Clear the screen
        if(result == 'Error'):
            clean()
    def make_operation():
        values = " ".join(operationsList)
        values = values.replace(' ', '')
        data = [*operationsList]
        i=0
        while(len(data) > i):
            if(data[0] == "∫"):
                try:
                    numbers = values.split("∫")
                    x = symbols('x')
                    f = parse_expr(numbers[1])
                    result = integrate(f, x)
                except:
                    result = 'Error'
            elif(data[0] == "f(x)"):
                try:
                    numbers = values.split("f(x)")
                    x = symbols('x')
                    f = parse_expr(numbers[1])
                    result = diff(f, x)
                except:
                    result = 'Error'
            else:
                try:
                    # get a string with operations and it do them
                    result = eval(values)
                except:
                    result = 'Error'
            i+= 1
        show_result(result)

    # Number buttons postitions
    x = 9
    xpos = 0
    ypos = 180
    while(x >= 0):
        if(xpos == 160):
            Button(mainWindow, name = str(x), text = x, width = 8, height = 4, border=5, command = lambda element = x: add_elementList(str(element))).place(x = xpos, y = ypos)
            xpos = 0
            ypos += 80
        else:
            Button(mainWindow, name = str(x), text = x, width = 8, height = 4, border=5, command = lambda element = x: add_elementList(str(element))).place(x = xpos, y = ypos)
            xpos += 80
        x -=1

    # Operation buttons position
    Button(mainWindow, name = 'dot', text = '.', width = 8, height = 4, border=5, command = lambda: add_elementList('.')).place(x = 80, y = 420)
    Button(mainWindow, name = 'equal', text = '=', width = 8, height = 4, border=5, command = lambda: make_operation()).place(x = 160, y = 420)
    Button(mainWindow, name = 'plus', text = '+', width = 8, height = 4, border=5, command = lambda: add_elementList('+')).place(x = 240, y = 420)
    Button(mainWindow, name = 'minus', text = '-', width = 8, height = 4, border=5, command = lambda: add_elementList('-')).place(x = 240, y = 340)
    Button(mainWindow, name = 'mult', text = '*', width = 8, height = 4, border=5, command = lambda: add_elementList('*')).place(x = 240, y = 260)
    Button(mainWindow, name = 'div', text = '÷', width = 8, height = 4, border=5, command = lambda: add_elementList('/')).place(x = 240, y = 180)
    Button(mainWindow, name = 'integration', text = '∫x', width = 8, height = 4, border=5, command = lambda: add_elementList('∫')).place(x = 80, y = 99)
    Button(mainWindow, name = 'derivation', text = 'dy/dx', width = 8, height = 4, border=5, command = lambda: add_elementList('f(x)')).place(x = 0, y = 99)
    Button(mainWindow, name = 'x', text = 'x', width = 8, height = 4, border=5,command = lambda: add_elementList('x')).place(x = 160, y = 99)
    Button(mainWindow, name = 'clear', text = '◄', width = 8, height = 4, border=5, command = clean).place(x = 240, y = 99)
    mainWindow.mainloop()
main()