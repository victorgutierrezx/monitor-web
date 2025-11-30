import csv
from typing import List
from .verificador import EstadoSitio
from datetime import datetime

def guardar_csv(resultados: List[EstadoSitio], nombre_archivo: str = "reporte_estado.csv"):
    """Guarda la lista de resultados en un archivo CSV."""
    
    encabezados_csv = ["Fecha", "URL", "Estado", "Código", "Tiempo (s)", "Detalle"]
    
    try:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados_csv)
            
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            for res in resultados:
                escritor.writerow([
                    fecha_actual,
                    res.url,
                    "ONLINE" if res.esta_online else "OFFLINE",
                    res.codigo_estado,
                    f"{res.tiempo_respuesta:.2f}",
                    res.motivo
                ])
        print(f"\n[INFO] Reporte guardado exitosamente en: {nombre_archivo}")
    except IOError as e:
        print(f"[ERROR] No se pudo guardar el archivo CSV: {e}")
