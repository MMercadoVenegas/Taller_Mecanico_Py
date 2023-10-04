import tkinter as tk
from datetime import datetime

# Función para verificar el usuario y contraseña
def verificar_login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    # Verificar las credenciales (puedes implementar tu propia lógica de autenticación aquí)
    if usuario == "usuario" and contrasena == "contrasena":
        # Contraseña correcta, mostrar la interfaz de trabajo
        ventana_login.destroy()
        mostrar_interfaz_de_trabajo()
    else:
        # Contraseña incorrecta, mostrar un mensaje de error
        mensaje_label.config(text="Credenciales incorrectas")




# Función para mostrar la interfaz de trabajo
def mostrar_interfaz_de_trabajo():

    ventana = tk.Tk()
    ventana.title("Registro de Trabajos en el Taller")

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

    ventana.mainloop()








# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")

usuario_label = tk.Label(ventana_login, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_login)
usuario_entry.pack()

contrasena_label = tk.Label(ventana_login, text="Contraseña:")
contrasena_label.pack()
contrasena_entry = tk.Entry(ventana_login, show="*")  # Para ocultar la contraseña
contrasena_entry.pack()

iniciar_sesion_button = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login)
iniciar_sesion_button.pack()

mensaje_label = tk.Label(ventana_login, text="")
mensaje_label.pack()

# Iniciar la ventana de inicio de sesión
ventana_login.mainloop()