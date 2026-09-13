MAPA_HISTORIA_LOTE = {

    "inicio": {
        "texto": "Pepito despierta en los Backrooms. No recuerda cómo llegó allí. Frente a él hay dos caminos.",
        "opciones": {
            "A": "pasillo_oscuro",
            "B": "sala_luces"
        }
    },

    "pasillo_oscuro": {
        "texto": "Pepito avanza por un pasillo oscuro y encuentra una llave oxidada en el suelo.",
        "objeto": "llave",
        "opciones": {
            "A": "puerta_cerrada",
            "B": "habitacion_cajas"
        }
    },

    "sala_luces": {
        "texto": "Las luces parpadean constantemente. Pepito escucha un ruido extraño detrás de una puerta.",
        "opciones": {
            "A": "puerta_sonido",
            "B": "pasillo_amarillo"
        }
    },

    "habitacion_cajas": {
        "texto": "Pepito entra en una habitación llena de cajas. Mientras busca una salida, encuentra una linterna.",
        "objeto": "linterna",
        "opciones": {
            "A": "pasillo_estrecho",
            "B": "puerta_cerrada"
        }
    },

    "puerta_sonido": {
        "texto": "Pepito abre lentamente la puerta para descubrir de dónde viene el ruido.",
        "opciones": {
            "A": "habitacion_segura",
            "B": "pasillo_estrecho"
        }
    },

    "pasillo_amarillo": {
        "texto": "Pepito continúa por el largo pasillo amarillo. Después de caminar un rato encuentra una puerta con un lector electrónico.",
        "opciones": {
            "A": "puerta_seguridad",
            "B": "habitacion_cajas"
        }
    },

    "pasillo_estrecho": {
        "texto": "Pepito entra en un pasillo muy estrecho. Al mirar el suelo encuentra una tarjeta de acceso.",
        "objeto": "tarjeta",
        "opciones": {
            "A": "puerta_seguridad",
            "B": "puerta_sonido"
        }
    },

    "puerta_cerrada": {
        "texto": "Pepito encuentra una puerta cerrada con una antigua cerradura. Parece que la llave podría funcionar.",
        "requiere": "llave",
        "opciones": {
            "A": "habitacion_segura",
            "B": "pasillo_oscuro"
        }
    },

    "puerta_seguridad": {
        "texto": "Pepito llega a una puerta con un lector electrónico. Cuando acerca la tarjeta, escucha un ruido detrás de él.",
        "requiere": "tarjeta",
        "opciones": {
            "A": "salida_principal",
            "B": "zona_desconocida"
        }
    },

    "habitacion_segura": {
        "texto": "Pepito entra en una habitación tranquila. Encuentra dos puertas frente a él y no sabe cuál lleva a la salida.",
        "opciones": {
            "A": "puerta_blanca",
            "B": "puerta_roja"
        }
    },

    "zona_desconocida": {
        "texto": "Pepito se da la vuelta y descubre que una criatura lo ha estado siguiendo. Tiene muy poco tiempo para reaccionar.",
        "opciones": {
            "A": "corredor",
            "B": "habitacion_cerrada"
        }
    },

    "puerta_blanca": {
        "texto": "Pepito abre la puerta blanca y encuentra un pasillo completamente iluminado. Al final ve una salida.",
        "opciones": {}
    },

    "puerta_roja": {
        "texto": "Pepito abre la puerta roja y entra en una habitación que parece conocida. Después de unos segundos se da cuenta de que ha regresado al inicio.",
        "opciones": {}
    },

    "corredor": {
        "texto": "Pepito corre por el corredor y logra perder a la criatura. Sin embargo, termina frente a una escalera que desciende hacia la oscuridad.",
        "opciones": {
            "A": "escaleras",
            "B": "pasillo_sin_salida"
        }
    },

    "habitacion_cerrada": {
        "texto": "Pepito entra rápidamente en una habitación y cierra la puerta. Después de unos minutos todo queda en silencio.",
        "opciones": {
            "A": "puerta_pequeña",
            "B": "ventilacion"
        }
    },

    "salida_principal": {
        "texto": "Pepito atraviesa la puerta y finalmente encuentra una salida de los Backrooms. Ha conseguido escapar.",
        "opciones": {}
    },

    "escaleras": {
        "texto": "Pepito baja las escaleras y encuentra una puerta que lo lleva fuera de los Backrooms.",
        "opciones": {}
    },

    "pasillo_sin_salida": {
        "texto": "Pepito sigue por el pasillo, pero termina en una habitación sin salida. Las luces comienzan a apagarse.",
        "opciones": {}
    },

    "puerta_pequeña": {
        "texto": "Pepito abre una pequeña puerta y encuentra una salida. Después de todo lo que pasó, finalmente consigue escapar.",
        "opciones": {}
    },

    "ventilacion": {
        "texto": "Pepito entra por la ventilación y termina nuevamente en el mismo pasillo. Parece estar atrapado en un bucle.",
        "opciones": {}
    }
}

def avanzar_motor_narrativo(data):

    nodo = data.nodo_actual
    decision = data.decision_usuario
    inventario = data.inventario

    
    if nodo not in MAPA_HISTORIA_LOTE:
        raise ValueError("El nodo actual no existe")

    nodo_info = MAPA_HISTORIA_LOTE[nodo]

    
    if decision not in nodo_info["opciones"]:
        raise ValueError("Decisión inválida")

    siguiente_nodo = nodo_info["opciones"][decision]


    if siguiente_nodo not in MAPA_HISTORIA_LOTE:
        raise ValueError("El nodo siguiente no existe")

    siguiente_info = MAPA_HISTORIA_LOTE[siguiente_nodo]

    
    if "requiere" in siguiente_info:

        if siguiente_info["requiere"] not in inventario:

            return {
                "mensaje": "No tienes el objeto necesario para avanzar",
                "nodo_actual": nodo,
                "opciones": nodo_info["opciones"],
                "inventario": inventario
            }

    
    if "objeto" in siguiente_info:

        if siguiente_info["objeto"] not in inventario:
            inventario.append(siguiente_info["objeto"])

    return {
        "mensaje": siguiente_info["texto"],
        "nodo_actual": siguiente_nodo,
        "opciones": siguiente_info["opciones"],
        "inventario": inventario
    }

def obtener_opciones(nodo: str):

    if nodo not in MAPA_HISTORIA_LOTE:
        raise ValueError("El nodo no existe")

    nodo_info = MAPA_HISTORIA_LOTE[nodo]

    return {
        "nodo_actual": nodo,
        "texto": nodo_info["texto"],
        "opciones": nodo_info["opciones"]
    }