import edge_tts
import asyncio
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk, filedialog

# ==== VARIABLES GLOBALES ====
carpeta_destino = ""

# ==== FUNCIÓN PRINCIPAL ====
async def descargar_sonidos(texto, i, categoria, carpeta):
    voice = "en-US-GuyNeural"
    communicate = edge_tts.Communicate(texto, voice)
    ruta = f"{carpeta}/{categoria}_{i}.mp3"
    await communicate.save(ruta)

def seleccionar_carpeta():
    global carpeta_destino
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_destino = carpeta
        lbl_carpeta.config(text=f"Carpeta seleccionada:\n{carpeta}", fg="green")

def procesar():
    global carpeta_destino
    categoria = combo_categoria.get()
    palabras_texto = txt_palabras.get("1.0", tk.END).strip()

    if not categoria or not palabras_texto or not carpeta_destino:
        messagebox.showwarning("Faltan datos", "Debes seleccionar la categoría, escribir palabras y elegir carpeta.")
        return

    # Convertimos las palabras a lista (una por línea)
    palabras = [p.strip().upper() for p in palabras_texto.splitlines() if p.strip()]

    # Descargamos los audios uno por uno
    try:
        for i, word in enumerate(palabras, start=1):
            asyncio.run(descargar_sonidos(word, i, categoria, carpeta_destino))
        messagebox.showinfo("Completado", f"Se descargaron {len(palabras)} audios en la categoría {categoria}.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# ==== INTERFAZ ====
ventana = tk.Tk()
ventana.title("Descargar audios Spelling Bee")
ventana.geometry("650x500")

# Categoría
tk.Label(ventana, text="Selecciona categoría:", font=("Arial", 12)).pack(pady=5)
combo_categoria = ttk.Combobox(ventana, values=["A", "B"], state="readonly", font=("Arial", 12))
combo_categoria.pack(pady=5)

# Palabras
tk.Label(ventana, text="Escribe las palabras (una por línea):", font=("Arial", 12)).pack(pady=5)
txt_palabras = scrolledtext.ScrolledText(ventana, width=70, height=10, font=("Arial", 11))
txt_palabras.pack(pady=5)

# Selección de carpeta
btn_carpeta = tk.Button(ventana, text="Seleccionar carpeta de destino", command=seleccionar_carpeta, bg="blue", fg="white", font=("Arial", 11, "bold"))
btn_carpeta.pack(pady=10)

lbl_carpeta = tk.Label(ventana, text="Ninguna carpeta seleccionada", font=("Arial", 10), fg="red")
lbl_carpeta.pack(pady=5)

# Botón procesar
btn = tk.Button(ventana, text="Descargar Audios", command=procesar, bg="green", fg="white", font=("Arial", 13, "bold"))
btn.pack(pady=20)

ventana.mainloop()
