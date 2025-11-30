import asyncio
import aiohttp
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Importamos nuestros módulos
from src.verificador import verificar_url
from src.reporte import guardar_csv

# Inicializar colorama para colores en la terminal
init(autoreset=True)

async def main():
    archivo_entrada = Path("sitios.txt")
    
    if not archivo_entrada.exists():
        print(Fore.RED + f"[ERROR] No se encontró el archivo {archivo_entrada}")
        print("Por favor crea un archivo 'sitios.txt' con una URL por línea.")
        return

    # Leer URLs y limpiar espacios en blanco
    urls = [linea.strip() for linea in archivo_entrada.read_text().splitlines() if linea.strip()]

    if not urls:
        print(Fore.YELLOW + "[AVISO] El archivo sitios.txt está vacío.")
        return

    print(f"{Style.BRIGHT}Iniciando monitoreo de {len(urls)} sitios web...\n")

    # Crear la sesión asíncrona única (Mejor práctica)
    async with aiohttp.ClientSession() as sesion:
        tareas = []
        for url in urls:
            # Añadir la tarea a la lista sin ejecutarla todavía
            tareas.append(verificar_url(sesion, url))
        
        # Ejecutar todas las tareas simultáneamente (gather)
        resultados = await asyncio.gather(*tareas)

    # Imprimir tabla de resultados en consola
    print(f"{'ESTADO':<8} {'CÓDIGO':<8} {'TIEMPO':<10}URL")
    print("-" * 60)

    for res in resultados:
        # Definir color según si está online u offline
        color = Fore.GREEN if res.esta_online else Fore.RED
        icono = "✔" if res.esta_online else "✘"
        
        # Imprimir fila formateada
        print(f"{color}{icono} GET    {res.codigo_estado:<8} {res.tiempo_respuesta:.2f}s      {res.url}")

    # Guardar reporte en CSV
    guardar_csv(resultados)

if __name__ == "__main__":
    # Ajuste necesario para Windows si usas Python 3.8 o superior
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Programa detenido por el usuario.")
