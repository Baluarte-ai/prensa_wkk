# WKK - Sistema de Control de Prensa

Sistema de control y monitoreo de prensa industrial para Raspberry Pi con interfaz táctil.

## Características

- Lectura de fuerza/presión en tiempo real vía Modbus (sensor USB)
- Evaluación automática de piezas OK/NOK
- Gráfica en tiempo real de fuerza vs setpoints
- Control de electroválvula vía GPIO
- Registro automático en base de datos SQLite
- Exportación de registros a Excel (.xlsx)

## Requisitos

- Raspberry Pi con Raspberry Pi OS
- Python 3.7+
- Pantalla táctil (recomendado 7" o 10")
- Sensor de fuerza con interfaz Modbus RTU (USB)

## Instalación en Raspberry Pi

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/prensa_wkk.git
cd prensa_wkk

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python Codigo.py
```

## Ejecución

```bash
# Producción (Raspberry Pi con hardware conectado)
python Codigo.py

# Demo (Windows/Linux sin hardware, datos simulados)
python Codigo_demo.py
```

## Configuración de Hardware

| Componente | Pin GPIO |
|---|---|
| LED (Electroválvula) | GPIO 17 |
| Sensor de Pulso | GPIO 4 |
| Sensor Modbus | USB (/dev/ttyUSB0) |

## Estructura del Proyecto

```
prensa_wkk/
├── Codigo.py              # Aplicación principal (Raspberry Pi)
├── Codigo_demo.py         # Demo para visualización (Windows/Linux)
├── requirements.txt       # Dependencias Python
├── assets/
│   ├── Logo WKK.png               # Logo WKK (transparente)
│   ├── Logo WKK.jpg               # Logo WKK (original)
│   ├── Logo Horizontal sin fondo.png  # Logo Baluarte
│   └── convert_logos.py           # Script de conversión de logos
└── README.md
```

## Desarrollado por

**Proyectos de Integración Baluarte**
