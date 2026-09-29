# Configuración de los Columnas:

COLUMNAS = {
    "PONDERA": {
        "tipo": "int",
        "completitud": 100
    },
    "ESTADO": {
        "tipo": "int",
        "completitud": 98
    },
    "CAT_OCUP": {
        "tipo": "int",
        "completitud":   85
    },
    "EDAD": {
        "tipo": "int",
        "completitud": 99
    },
    "CH04": {
    "tipo": "int",
    "completitud": 95
    },
    "REGION": {
        "tipo": "int",
        "completitud": 100
    },
    "AGLOMERADO": {
        "tipo": "int",
        "completitud": 97
    },
    "ANO4": {
        "tipo": "int",
        "completitud": 100
    },
    "TRIMESTRE": {
        "tipo": "int",
        "completitud": 100
    },
    "ITF": {
        "tipo": "int",
        "completitud": 78
    },
    "MAS_500": {
        "tipo": "str",
        "completitud": 96
    },
    "GDECCFR": {
        "tipo": "int",
        "completitud": 82
    }
}

# Configuración de los roles:
ROLES = {
    "docente": {
        "columnas": ["EDAD", "ESTADO", "CAT_OCUP", "REGION"],
        "criterio": "nombre",
        "orden": "A",
        "minimo_completitud": 80
    },

    "investigador": {
        "columnas": ["EDAD", "ESTADO", "CAT_OCUP", "ITF","CH04", "GDECCFR"],
        "criterio": "completitud",
        "orden": "B",
        "minimo_completitud": 60
    },

    "analista": {
        "columnas": ["PONDERA", "REGION", "AGLOMERADO", "ANO4",
                     "TRIMESTRE", "ITF", "MAS_500"],
        "criterio": "completitud",
        "orden": "A",
        "minimo_completitud": 40
    },

    "economista": {
        "columnas": ["PONDERA", "ESTADO", "CAT_OCUP", "REGION",
                     "AGLOMERADO", "ANO4", "TRIMESTRE", "ITF", "GDECCFR"],
        "criterio": "nombre",
        "orden": "A",
        "minimo_completitud": 90
    }
}


#FUNCIONES 

def mostrar_columnas(columnas):
    """
    Muestra el nombre, tipo y completitud de las columnas.
    """

    print("INFORME DE COLUMNAS")
    print("-------------------")

    for columna in columnas:
        tipo = COLUMNAS[columna]["tipo"]
        completitud = COLUMNAS[columna]["completitud"]

        print(f"{columna} | Tipo: {tipo} | Completitud: {completitud}%")

def filtrar_columnas(rol):
    """
    Devuelve las columnas del rol que cumplen con el porcentaje mínimo de completitud.
    """

    datos_rol = ROLES[rol]

    columnas_filtradas = filter(
        lambda columna: COLUMNAS[columna]["completitud"] >= datos_rol["minimo_completitud"],
        datos_rol["columnas"]
    )
    return list(columnas_filtradas)

def ordenar_columnas(columnas, rol=None):
    """
    Ordena las columnas según el criterio y el orden configurados para el rol.
    Si no se indica un rol, ordena por completitud de forma descendente.
    """

    if rol is None:
        columnas.sort(
            key=lambda columna: COLUMNAS[columna]["completitud"],
            reverse=True
        )

    else:
        datos_rol = ROLES[rol]
        criterio = datos_rol["criterio"]
        orden = datos_rol["orden"]

        descendente = orden == "B"

        if criterio == "nombre":
            columnas.sort(reverse=descendente)

        elif criterio == "completitud":
            columnas.sort(
                key=lambda columna: COLUMNAS[columna]["completitud"],
                reverse=descendente
            )

        else:
            print("El criterio de ordenamiento no es válido.")
            return []

    return columnas

def generar_informe(rol=None):
    """
    Genera un informe de columnas según el rol indicado.
    """

    if rol is None:
        columnas = list(COLUMNAS.keys())
        columnas = ordenar_columnas(columnas)

    else:
        if rol not in ROLES:
            print("El rol indicado no existe.")
            return

        columnas = filtrar_columnas(rol)
        columnas = ordenar_columnas(columnas, rol)

    mostrar_columnas(columnas)