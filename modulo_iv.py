import tkinter as tk
from datetime import datetime

# Crear una función para guardar los datos del trabajo
def guardar_trabajo():
    marca = marca_entry.get()
    modelo = modelo_entry.get()
    cliente = cliente_entry.get()
    tipo_trabajo = tipo_trabajo_var.get()
    comentarios = comentarios_entry.get()
    fecha_hora = datetime.now()

    # Aquí puedes realizar cualquier lógica adicional, como asignar tiempos de trabajo según el tipo

    # Guardar los datos en algún lugar (base de datos, archivo, etc.)

    # Limpiar los campos después de guardar
    marca_entry.delete(0, tk.END)
    modelo_entry.delete(0, tk.END)
    cliente_entry.delete(0, tk.END)
    tipo_trabajo_var.set('')
    comentarios_entry.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Trabajos en el Taller")

# Etiquetas y campos de entrada
marca_label = tk.Label(ventana, text="Marca:")
marca_label.pack()
marca_entry = tk.Entry(ventana)
marca_entry.pack()

modelo_label = tk.Label(ventana, text="Modelo:")
modelo_label.pack()
modelo_entry = tk.Entry(ventana)
modelo_entry.pack()

cliente_label = tk.Label(ventana, text="Nombre del Cliente:")
cliente_label.pack()
cliente_entry = tk.Entry(ventana)
cliente_entry.pack()

tipo_trabajo_label = tk.Label(ventana, text="Tipo de Trabajo:")
tipo_trabajo_label.pack()
tipo_trabajo_var = tk.StringVar()
tipo_trabajo_combobox = tk.OptionMenu(ventana, tipo_trabajo_var, "Reparación", "Mantenimiento", "Diagnóstico", "Limpieza Básica", "Limpieza Profunda")
tipo_trabajo_combobox.pack()

comentarios_label = tk.Label(ventana, text="Comentarios:")
comentarios_label.pack()
comentarios_entry = tk.Entry(ventana)
comentarios_entry.pack()

# Botón para guardar el trabajo
guardar_button = tk.Button(ventana, text="Guardar Trabajo", command=guardar_trabajo)
guardar_button.pack()

# Iniciar la aplicación
ventana.mainloop()