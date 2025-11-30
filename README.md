# Monitor de Estado Web

Herramienta de línea de comandos (CLI) desarrollada en **Python** para verificar la disponibilidad y tiempos de respuesta de múltiples sitios web mediante peticiones asíncronas.

## 📋 Características

-   **Verificación Asíncrona:** Usa `asyncio` y `aiohttp` para consultar varias URLs de forma simultánea.
-   **Reportes CSV Automáticos:** Genera `reporte_estado.csv` con:
    -   Fecha y hora
    -   URL consultada
    -   Estado (Online/Offline)
    -   Código HTTP
    -   Latencia
-   **Configuración Sencilla:** Carga automáticamente las URLs desde `sitios.txt`.
-   **Manejo Robusto de Errores:** Soporta fallos de conexión, timeouts y errores DNS sin detener la ejecución.

------------------------------------------------------------------------

## 📦 Requisitos

-   Python **3.8 o superior**
-   Conexión a internet

------------------------------------------------------------------------

## 🔧 Instalación

### 1. Clonar el repositorio

``` bash
git clone https://github.com/victorgutierrezx/monitor-web.git
cd monitor-web
```

### 2. Crear y activar entorno virtual

**Windows**

``` bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Uso

### 1. Agregar sitios a `sitios.txt`

Cada URL debe ocupar una línea:

    https://www.google.com
    https://www.github.com
### 2. Ejecutar el monitoreo

``` bash
python main.py
```

### 3. Revisar resultados

-   Se mostrarán en la terminal.
-   También se generará el archivo **reporte_estado.csv**.

------------------------------------------------------------------------

## 📁 Estructura del Proyecto

    monitor_web/
    ├── sitios.txt           # Lista de URLs a verificar
    ├── main.py              # Script
    ├── requirements.txt     # Dependencias
    ├── src/
    │   ├── verificador.py   # Lógica asíncrona de conexión
    │   └── reporte.py       # Generación del archivo CSV
    └── README.md

------------------------------------------------------------------------

## 📩 Contacto

**Email:** contacto@victorgutierrez.dev **Autor:** Víctor Gutiérrez
