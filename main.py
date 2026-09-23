def validar_codigo_estudiante():
    """Valida que el código del estudiante no esté vacío y cumpla con la longitud mínima.
    Requerimiento atendido: Validación de datos de entrada.
    """
    while True:
        codigo = input("Ingrese el código de estudiante (mínimo 5 caracteres): ")
        if len(codigo) >= 5:
            return codigo
        print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")


def validar_tipo_consulta():
    """Valida que el tipo de consulta pertenezca estrictamente a la lista permitida.
    Requerimiento atendido: Control de restricciones y opciones autorizadas.
    """
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    
    while True:
        print(f"Tipos permitidos: {', '.join(tipos_validos)}")
        tipo = input("Ingrese el tipo de consulta: ")
        if tipo in tipos_validos:
            return tipo
        print("Error: Tipo de consulta no válido. Intente nuevamente.")


def validar_texto_obligatorio(mensaje_prompt):
    """Valida y retorna un texto obligatorio que no esté vacío.
    Requerimiento atendido: Validación de campos obligatorios sin cadenas vacías.
    """
    while True:
        texto = input(mensaje_prompt)
        if len(texto) > 0:
            return texto
        print("Error: Este campo no puede estar vacío.")


def calcular_prioridad(tipo_consulta):
    """Calcula y retorna la prioridad de atención según el tipo de consulta.
    Requerimiento atendido: Reglas de negocio y procesamiento lógico.
    """
    if tipo_consulta == "pagos" or tipo_consulta == "matricula":
        return "Alta"
    else:
        return "Baja"


def mostrar_menu():
    """Muestra el menú principal del sistema.
    Requerimiento atendido: Interfaz de usuario (UI) en consola.
    """
    print("\n========================================")
    print("  SISTEMA DE ORIENTACIÓN Y REGISTRO")
    print("========================================")
    print("1. Registrar nueva solicitud")
    print("2. Salir")
    print("----------------------------------------")


def mostrar_resumen_solicitud(solicitud):
    """Muestra de manera ordenada el resumen de la solicitud registrada.
    Requerimiento atendido: Req. 7 (Generación de reportes y resúmenes).
    """
    print("\n========================================")
    print("        RESUMEN DE LA SOLICITUD")
    print("========================================")
    print(f" Código de estudiante: {solicitud['codigo']}")
    print(f" Nombre del estudiante: {solicitud['nombre']}")
    print(f" Tipo de consulta:     {solicitud['tipo_consulta']}")
    print(f" Descripción del caso: {solicitud['descripcion']}")
    print(f" Prioridad asignada:   {solicitud['prioridad']}")
    print("========================================")


def registrar_datos_basicos():
    """Registra los datos aplicando las validaciones y asignando la prioridad.
    Requerimiento atendido: Req. 8 y 9 (Modularidad, control de alcance y paso de parámetros).
    """
    print("\n--- REGISTRO DE SOLICITUD ---")
    codigo = validar_codigo_estudiante()
    nombre = validar_texto_obligatorio("Ingrese el nombre del estudiante: ")
    tipo_consulta = validar_tipo_consulta()
    descripcion = validar_texto_obligatorio("Ingrese una descripción breve del caso: ")
    
    prioridad = calcular_prioridad(tipo_consulta)
    
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion,
        "prioridad": prioridad
    }
    return solicitud


def main():
    """Función principal que gestiona el flujo del programa.
    Requerimiento atendido: Req. 10 (Estructura de control múltiple para al menos tres registros sin usar break).
    """
    solicitudes = []
    contador_registros = 0
    
    while contador_registros < 3:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mi_solicitud = registrar_datos_basicos()
            mostrar_resumen_solicitud(mi_solicitud)
            solicitudes.append(mi_solicitud)
            contador_registros += 1
            print(f"\n[Progreso] Solicitudes registradas: {contador_registros}/3")
        elif opcion == "2":
            print("Saliendo del sistema...")
            contador_registros = 3  # Control de salida sin break
        else:
            print("Opción no válida. Intente nuevamente.")
            
    print("\n--- FIN DEL PROCESO DE REGISTRO ---")
    print(f"Total de solicitudes procesadas en esta ejecución: {len(solicitudes)}")


if __name__ == "__main__":
    main()