import aiohttp
import asyncio
from dataclasses import dataclass
from time import perf_counter

@dataclass
class EstadoSitio:
    """Clase de datos para almacenar la información de cada sitio."""
    url: str
    codigo_estado: int
    motivo: str
    tiempo_respuesta: float
    esta_online: bool

async def verificar_url(sesion: aiohttp.ClientSession, url: str) -> EstadoSitio:
    """Verifica el estado de una URL dada usando una sesión aiohttp."""
    tiempo_inicio = perf_counter()
    # Usamos un encabezado para simular un navegador real
    encabezados = {'User-Agent': 'Mozilla/5.0 (Monitor Web Python)'}

    try:
        # Timeout de 10 segundos para evitar bloqueos largos
        async with sesion.get(url, headers=encabezados, timeout=10) as respuesta:
            tiempo_fin = perf_counter()
            # Consideramos que está online si el código es menor a 400
            esta_online = respuesta.status < 400
            
            return EstadoSitio(
                url=url,
                codigo_estado=respuesta.status,
                motivo=respuesta.reason,
                tiempo_respuesta=tiempo_fin - tiempo_inicio,
                esta_online=esta_online
            )
            
    except aiohttp.ClientConnectorError:
        return EstadoSitio(url, 0, "Error de Conexión (DNS/Red)", 0.0, False)
    except asyncio.TimeoutError:
        return EstadoSitio(url, 408, "Tiempo de espera agotado (Timeout)", 10.0, False)
    except Exception as e:
        return EstadoSitio(url, 0, f"Error Desconocido: {str(e)}", 0.0, False)
