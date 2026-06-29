import tkinter as tk
from gpiozero import LED, Button

# --- 1. CONFIGURACIÓN DE PINES ---
# Salida del pistón
piston = LED(17)

# Entradas esperando 3.3V (1 lógico)
pin_pulso = Button(22, pull_up=False)
pin_paro = Button(26, pull_up=False)

# --- 2. ESTADO INICIAL (PISTÓN ENCENDIDO DESDE EL ARRANQUE) ---
piston.off()

# --- 3. LÓGICA DE CONTROL ---
def apagar_piston():
    # Corta la energía instantáneamente
    piston.on()
    
def encender_piston_manual():
    # Permite reiniciar el sistema manualmente
    piston.off()

# Asignar las interrupciones de hardware:
# Si cualquiera de los dos pines recibe un "1", se dispara apagar_piston
pin_pulso.when_pressed = apagar_piston
pin_paro.when_pressed = apagar_piston

def actualizar_interfaz():
    # Refleja el estado real de los pines de entrada en la pantalla
    if pin_pulso.is_pressed:
        canvas.itemconfig(luz_4, fill="blue")
    else:
        canvas.itemconfig(luz_4, fill="gray")

    if pin_paro.is_pressed:
        canvas.itemconfig(luz_22, fill="orange")
    else:
        canvas.itemconfig(luz_22, fill="gray")

    # Refleja el estado real de la salida del pistón (Pin 17)
    if piston.value:
        canvas.itemconfig(luz_piston, fill="green")
        estado_label.config(text="PISTÓN ACTIVO (EN MOVIMIENTO)", fg="green")
    else:
        canvas.itemconfig(luz_piston, fill="red")
        estado_label.config(text="PISTÓN DETENIDO (CORTE ACTIVADO)", fg="red")

    # Bucle de refresco de interfaz (20 FPS)
    ventana.after(50, actualizar_interfaz)

def cerrar():
    piston.on()
    pin_pulso.close()
    pin_paro.close()
    ventana.destroy()

# --- 4. DISEÑO DE INTERFAZ GRÁFICA ---
ventana = tk.Tk()
ventana.title("Control de Pistón Inverso")
ventana.geometry("400x300")
ventana.resizable(False, False)

tk.Label(ventana, text="Panel de Control del Pistón", font=("Arial", 14, "bold")).pack(pady=10)

# Lienzo para las luces
canvas = tk.Canvas(ventana, width=350, height=100)
canvas.pack()

# Indicadores
canvas.create_text(60, 20, text="Pulso\n(Pin 4)", font=("Arial", 10, "bold"), justify="center")
luz_4 = canvas.create_oval(35, 40, 85, 90, fill="gray", outline="black", width=2)

canvas.create_text(175, 20, text="Paro\n(Pin 22)", font=("Arial", 10, "bold"), justify="center")
luz_22 = canvas.create_oval(150, 40, 200, 90, fill="gray", outline="black", width=2)

canvas.create_text(290, 20, text="Pistón\n(Pin 17)", font=("Arial", 10, "bold"), justify="center")
luz_piston = canvas.create_oval(265, 40, 315, 90, fill="green", outline="black", width=2)

# Etiqueta de Estado
estado_label = tk.Label(ventana, text="INICIANDO...", font=("Arial", 12, "bold"))
estado_label.pack(pady=10)

# Botones Manuales para Pruebas o Reinicio
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_encender = tk.Button(frame_botones, text="Re-Encender Pistón", bg="green", fg="white", width=16, command=encender_piston_manual)
btn_encender.grid(row=0, column=0, padx=10)

btn_apagar = tk.Button(frame_botones, text="Apagar Manual", bg="red", fg="white", width=16, command=apagar_piston)
btn_apagar.grid(row=0, column=1, padx=10)

# --- 5. EJECUCIÓN ---
ventana.protocol("WM_DELETE_WINDOW", cerrar)
actualizar_interfaz() 
ventana.mainloop()