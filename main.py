# Requerimiento 1: Registrar datos básicos de una solicitud
def registrar_datos_basicos():
    codigo = input("Ingrese el código de estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    tipo_consulta = input("Ingrese el tipo de consulta: ")
    descripcion = input("Ingrese una descripción breve: ")
    return {"codigo": codigo, "nombre": nombre, "tipo_consulta": tipo_consulta, "descripcion": descripcion}

if __name__ == "__main__":
    registrar_datos_basicos()