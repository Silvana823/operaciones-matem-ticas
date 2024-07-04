import tkinter as tk
from tkinter import messagebox


def sumar(entry1, entry2, result):
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        suma = num1 + num2
        result.set(suma)
    except ValueError:
        messagebox.showerror("Error" , " Por  favor , ingrese numero valido")


def resta(entry1, entry2, result):
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        resta = num1 - num2
        result.set(resta)
    except ValueError:
        messagebox.showerror("Error" , " Por  favor , ingrese numero valido")

def multiplicacion(entry1, entry2, result):
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        multiplicacion = num1 * num2
        result.set(multiplicacion)
    except ValueError:
        messagebox.showerror("Error" , " Por  favor , ingrese numero valido")

def division(entry1, entry2, result):
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        division = num1 / num2
        result.set(division)
    except ValueError:
        messagebox.showerror("Error" , " Por  favor , ingrese numero valido")


# Crea la ventana principal

root = tk.Tk()
root.title("Sumador de Numeros")
root.geometry("500x300")


# Crea Widget

label1 = tk.Label(root, text="Numero 1:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Numero 2:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

label_result=tk.Label(root, text="Result:")
label_result.pack(pady=5)
result=tk.StringVar()
entry_result= tk.Entry(root, textvariable=result, state='readonly')
entry_result.pack(pady=5)

button_sum=tk.Button(root, text="Suma", command=lambda: sumar(entry1, entry2, result))
button_sum.pack(padx= 30, pady =30, side=tk.LEFT) 

#resta

button_sum=tk.Button(root, text="Resta", command=lambda: resta(entry1, entry2, result))
button_sum.pack(padx=30, pady=30, side=tk.LEFT)

#multiplicacion
button_sum=tk.Button(root, text="Multiplicacion", command=lambda: multiplicacion(entry1, entry2, result))
button_sum.pack(padx=30, pady=30, side=tk.LEFT)

#division

button_sum=tk.Button(root, text="Division", command=lambda: division(entry1, entry2, result))
button_sum.pack(padx=30, pady=30, side=tk.LEFT)

#Ejecutar el bucle principal

root.mainloop()