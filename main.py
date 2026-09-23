def validar_codigo_estudiante():
    """Valida que el código del estudiante no esté vacío y cumpla con la longitud mínima."""
    while True:
        codigo = input("Ingrese el código de estudiante (mínimo 5 caracteres): ")
        if len(codigo) >= 5:
            return codigo
        print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")


def validar_tipo_consulta():
    """Valida que el tipo de consulta pertenezca estrictamente a la lista permitida."""
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    
    while True:
        print(f"Tipos permitidos: {', '.join(tipos_validos)}")
        tipo = input("Ingrese el tipo de consulta: ")
        if tipo in tipos_validos:
            return tipo
        print("Error: Tipo de consulta no válido. Intente nuevamente.")


def mostrar_menu():
    """Muestra el menú principal del sistema (función sin retorno)."""
    print("\n========================================")
    print("  SISTEMA DE ORIENTACIÓN Y REGISTRO")
    print("========================================")
    print("1. Registrar nueva solicitud")
    print("2. Salir")
    print("----------------------------------------")


def registrar_datos_basicos():
    """Registra los datos aplicando las validaciones anteriores."""
    print("\n--- REGISTRO DE SOLICITUD ---")
    codigo = validar_codigo_estudiante()
    
    nombre = input("Ingrese el nombre del estudiante: ")
    tipo_consulta = validar_tipo_consulta()
    descripcion = input("Ingrese una descripción breve del caso: ")
    
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }
    return solicitud


def main():
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        mi_solicitud = registrar_datos_basicos()
        print("\n¡Solicitud registrada con éxito!", mi_solicitud)
    else:
        print("Saliendo del sistema...")


if __name__ == "__main__":
    main()