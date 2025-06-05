# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 21:31:25 2025

@author: indir
"""

# conversor_coordenadas_gui.py

"""
README - Conversor de Coordenadas DD <-> DMS

Este programa en Python permite convertir coordenadas geográficas entre:
- Grados Decimales (DD)
- Grados, Minutos y Segundos (GMS)

Utiliza la librería `tkinter` para mostrar una interfaz gráfica (GUI) donde el usuario puede ingresar los datos y visualizar los resultados.

## Requisitos
- Python 3.x
- Asegúrese de que `tkinter` esté instalado. En algunas distribuciones mínimas de Python no se incluye por defecto.

### Instalación de tkinter en sistemas basados en Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

## Cómo ejecutar
1. Descargue este archivo.
2. Ejecútelo desde la consola o con doble clic (según su entorno):

```bash
python conversor_coordenadas_gui.py
```

## Uso
### Conversión de DD a GMS
- Ingrese el valor decimal (ej: `-73.985656`) en el primer campo.
- Presione el botón **Convertir a GMS**.
- Aparecerán los valores correspondientes en grados, minutos y segundos.

### Conversión de GMS a DD
- Ingrese los valores en grados, minutos y segundos en la parte inferior.
- Presione el botón **Convertir a DD**.
- Se mostrará el resultado en grados decimales.

## Autor
Desarrollado por [indira sacaza].
"""

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError as e:
    raise ImportError("No se encontró el módulo 'tkinter'. Asegúrese de tenerlo instalado. En sistemas Debian/Ubuntu use: sudo apt-get install python3-tk") from e

def dd_a_gms(dd):
    es_negativo = dd < 0
    dd = abs(dd)
    grados = int(dd)
    minutos_completo = (dd - grados) * 60
    minutos = int(minutos_completo)
    segundos = round((minutos_completo - minutos) * 60, 4)
    if es_negativo:
        grados *= -1
    return grados, minutos, segundos

def gms_a_dd(grados, minutos, segundos):
    dd = abs(grados) + minutos / 60 + segundos / 3600
    if grados < 0:
        dd *= -1
    return round(dd, 6)

def manejar_dd_a_gms():
    try:
        dd = float(entrada_dd.get())
        grados, minutos, segundos = dd_a_gms(dd)
        var_gms_grados.set(str(grados))
        var_gms_minutos.set(str(minutos))
        var_gms_segundos.set(str(segundos))
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para DD.")

def manejar_gms_a_dd():
    try:
        grados = float(entrada_gms_grados.get())
        minutos = float(entrada_gms_minutos.get())
        segundos = float(entrada_gms_segundos.get())
        dd = gms_a_dd(grados, minutos, segundos)
        var_resultado_dd.set(str(dd))
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos para GMS.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor DD <-> GMS")

# Variables
entrada_dd = tk.Entry(ventana)
entrada_dd.grid(row=0, column=1, padx=5, pady=5)
tk.Label(ventana, text="Grados decimales (DD):").grid(row=0, column=0, sticky="e")

tk.Button(ventana, text="Convertir a GMS", command=manejar_dd_a_gms).grid(row=1, column=0, columnspan=2, pady=5)

var_gms_grados = tk.StringVar()
var_gms_minutos = tk.StringVar()
var_gms_segundos = tk.StringVar()

tk.Label(ventana, text="Grados:").grid(row=2, column=0, sticky="e")
tk.Entry(ventana, textvariable=var_gms_grados, state='readonly').grid(row=2, column=1)

tk.Label(ventana, text="Minutos:").grid(row=3, column=0, sticky="e")
tk.Entry(ventana, textvariable=var_gms_minutos, state='readonly').grid(row=3, column=1)

tk.Label(ventana, text="Segundos:").grid(row=4, column=0, sticky="e")
tk.Entry(ventana, textvariable=var_gms_segundos, state='readonly').grid(row=4, column=1)

tk.Label(ventana, text="---").grid(row=5, column=0, columnspan=2)

tk.Label(ventana, text="Grados (GMS):").grid(row=6, column=0, sticky="e")
entrada_gms_grados = tk.Entry(ventana)
entrada_gms_grados.grid(row=6, column=1)

tk.Label(ventana, text="Minutos:").grid(row=7, column=0, sticky="e")
entrada_gms_minutos = tk.Entry(ventana)
entrada_gms_minutos.grid(row=7, column=1)

tk.Label(ventana, text="Segundos:").grid(row=8, column=0, sticky="e")
entrada_gms_segundos = tk.Entry(ventana)
entrada_gms_segundos.grid(row=8, column=1)

tk.Button(ventana, text="Convertir a DD", command=manejar_gms_a_dd).grid(row=9, column=0, columnspan=2, pady=5)

var_resultado_dd = tk.StringVar()
tk.Label(ventana, text="Resultado (DD):").grid(row=10, column=0, sticky="e")
tk.Entry(ventana, textvariable=var_resultado_dd, state='readonly').grid(row=10, column=1)

ventana.mainloop()
