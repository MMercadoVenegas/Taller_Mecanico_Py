import tkinter as tk

# Función para verificar el usuario y contraseña
def verificar_login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    # Verificar las credenciales (puedes implementar tu propia lógica de autenticación aquí)
    if usuario == "usuario" and contrasena == "contrasena":
        # Contraseña correcta, mostrar la interfaz de trabajo
        ventana_login.destroy()

    else:
        # Contraseña incorrecta, mostrar un mensaje de error
        mensaje_label.config(text="Credenciales incorrectas")

# Función para mostrar la interfaz de trabajo

    

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