# Conversor de Coordenadas DD <-> GMS

Este proyecto es una aplicación de escritorio desarrollada en Python que permite convertir coordenadas geográficas entre:
- **Grados Decimales (DD)**
- **Grados, Minutos y Segundos (GMS)**

Utiliza la biblioteca `tkinter` para ofrecer una interfaz gráfica amigable para el usuario.

## Requisitos
- Python 3.x
- Módulo `tkinter` instalado

### Instalación de `tkinter` en sistemas Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

## Uso
### Ejecutar el programa
```bash
python conversor_coordenadas_gui.py
```

### Funcionalidades
- **Conversión de DD a GMS**:
  - Ingrese un valor en grados decimales (ejemplo: -73.985656).
  - Presione el botón "Convertir a GMS".
  - Obtendrá los valores correspondientes en grados, minutos y segundos.

- **Conversión de GMS a DD**:
  - Ingrese los valores en grados, minutos y segundos.
  - Presione el botón "Convertir a DD".
  - El resultado se mostrará en grados decimales.

## Estructura del Proyecto
```
conversor_coordenadas_gui.py   # Código fuente principal
README.md                      # Documentación del proyecto
```

