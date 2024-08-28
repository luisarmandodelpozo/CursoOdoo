import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    if user_input == "1":
        messagebox.showinfo("Resultado", "Hola")
    else:
        root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Hola o Cerrar")

# Etiqueta y cuadro de entrada
label = tk.Label(root, text="Escribe un número:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Botón
button = tk.Button(root, text="Enviar", command=on_button_click)
button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()