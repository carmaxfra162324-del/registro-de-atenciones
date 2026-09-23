# Requerimiento 1 y 2: Registro con validaciones modulares 
def validar_codigo_estudiante():
    """Valida que el código del estudiante no esté vacío y cumpla con la longitud mínima."""
    while True:
        codigo = input("Ingrese el código de estudiante (mínimo 5 caracteres): ")
        if len(codigo) >= 5:
            return codigo
        print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")


def registrar_datos_basicos():
    """Registra los datos básicos de la solicitud aplicando validaciones."""
    print("\n--- REGISTRO DE SOLICITUD ---")
    codigo = validar_codigo_estudiante()
    
    nombre = input("Ingrese el nombre del estudiante: ")
    tipo_consulta = input("Ingrese el tipo de consulta: ")
    descripcion = input("Ingrese una descripción breve del caso: ")
    
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }
    return solicitud


def main():
    print("Iniciando Sistema de Orientación y Registro de Atenciones...")
    mi_solicitud = registrar_datos_basicos()
    print("\n¡Solicitud registrada con éxito!", mi_solicitud)


if __name__ == "__main__":
    main()