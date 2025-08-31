# Proyecto 1: Generador de Cuestionarios Interactivo con respuestas de animales repartidas

def cargar_preguntas():
    preguntas = {
        "ciudades": [
            {"pregunta": "¿Cuál es la capital de Francia?",
             "opciones": ["A. Madrid", "B. Roma", "C. París", "D. Berlín"],
             "respuesta_correcta": "C"},
            {"pregunta": "¿Cuál es la capital de España?",
             "opciones": ["A. Madrid", "B. Lisboa", "C. Barcelona", "D. Valencia"],
             "respuesta_correcta": "A"},
            {"pregunta": "¿Cuál es la capital de Italia?",
             "opciones": ["A. Florencia", "B. Roma", "C. Milán", "D. Venecia"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Cuál es la capital de Alemania?",
             "opciones": ["A. Berlín", "B. Múnich", "C. Hamburgo", "D. Frankfurt"],
             "respuesta_correcta": "A"},
            {"pregunta": "¿Cuál es la capital de Argentina?",
             "opciones": ["A. Santiago", "B. Buenos Aires", "C. Montevideo", "D. Lima"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Cuál es la capital de México?",
             "opciones": ["A. Cancún", "B. Guadalajara", "C. Ciudad de México", "D. Monterrey"],
             "respuesta_correcta": "C"},
            {"pregunta": "¿Cuál es la capital de Japón?",
             "opciones": ["A. Tokio", "B. Kioto", "C. Osaka", "D. Hiroshima"],
             "respuesta_correcta": "A"},
            {"pregunta": "¿Cuál es la capital de Canadá?",
             "opciones": ["A. Toronto", "B. Vancouver", "C. Montreal", "D. Ottawa"],
             "respuesta_correcta": "D"},
            {"pregunta": "¿Cuál es la capital de Australia?",
             "opciones": ["A. Sidney", "B. Canberra", "C. Melbourne", "D. Perth"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Cuál es la capital de Egipto?",
             "opciones": ["A. El Cairo", "B. Alejandría", "C. Luxor", "D. Giza"],
             "respuesta_correcta": "A"}

        ],
        "animales": [
            {"pregunta": "¿Cuál es el animal más rápido del mundo?",
             "opciones": ["A. Tigre", "B. Guepardo", "C. León", "D. Antílope"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Qué animal es conocido por tener memoria excepcional?",
             "opciones": ["A. Delfín", "B. Gato", "C. Elefante", "D. Perro"],
             "respuesta_correcta": "C"},
            {"pregunta": "¿Cuál es el mamífero más grande del mundo?",
             "opciones": ["A. Elefante africano", "B. Ballena azul", "C. Rinoceronte", "D. Jirafa"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Qué animal puede vivir más tiempo?",
             "opciones": ["A. Loro", "B. Gato", "C. Perro", "D. Tortuga de Galápagos"],
             "respuesta_correcta": "D"},
            {"pregunta": "¿Cuál es el ave que no puede volar?",
             "opciones": ["A. Águila", "B. Loro", "C. Paloma", "D. Pingüino"],
             "respuesta_correcta": "D"},
            {"pregunta": "¿Cuál es el animal conocido como el rey de la selva?",
             "opciones": ["A. Tigre", "B. Gorila", "C. Elefante", "D. León"],
             "respuesta_correcta": "D"},
            {"pregunta": "¿Qué animal produce miel?",
             "opciones": ["A. Mariposa", "B. Hormiga", "C. Abeja", "D. Avispa"],
             "respuesta_correcta": "C"},
            {"pregunta": "¿Cuál es el animal más venenoso del mundo?",
             "opciones": ["A. Medusa caja", "B. Serpiente cobra", "C. Escorpión", "D. Rana venenosa"],
             "respuesta_correcta": "A"},
            {"pregunta": "¿Qué animal es conocido por cambiar de color?",
             "opciones": ["A. Pulpo", "B. Camaleón", "C. Lagartija", "D. Pavo real"],
             "respuesta_correcta": "B"},
            {"pregunta": "¿Cuál es el animal más grande de la tierra?",
             "opciones": ["A. Rinoceronte", "B. Hipopótamo", "C. Elefante africano", "D. Bisonte"],
             "respuesta_correcta": "C"}
        ]
    }
    return preguntas


def mostrar_pregunta(pregunta, numero, total):
    print(f"\nPregunta {numero} de {total}: {pregunta['pregunta']}")
    for opcion in pregunta["opciones"]:
        print(opcion)

def obtener_respuesta():
    respuesta = input("Tu respuesta (A, B, C o D): ").upper()
    while respuesta not in ["A", "B", "C", "D"]:
        print("Respuesta inválida. Intenta de nuevo.")
        respuesta = input("Tu respuesta (A, B, C o D): ").upper()
    return respuesta

def corregir_respuesta(respuesta, correcta):
    if respuesta == correcta:
        print("¡Correcto!")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era {correcta}.")
        return False

def cuestionario(preguntas_tema):
    aciertos = 0
    total = len(preguntas_tema)
    for i, pregunta in enumerate(preguntas_tema, start=1):
        mostrar_pregunta(pregunta, i, total)
        respuesta = obtener_respuesta()
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            aciertos += 1
    print(f"\nHas terminado el cuestionario. Aciertos: {aciertos} de {total}")
    porcentaje = (aciertos / total) * 100
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")
    if porcentaje >= 80:
        print("!Enhorabuena crack¡")
    elif porcentaje >= 50:
        print("Muy bien aunque se puede mejorar.")
    else:
        print("Hay que practicar más...")

def main():
    preguntas = cargar_preguntas()
    while True:
        print("\n Bienvenido al cuestionario")
        print("\n--- MENÚ ---")
        print("1 - Empezar cuestionario")
        print("2 - Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print("\nElige un tema:")
            print("1 - Ciudades")
            print("2 - Animales")
            tema = input("Selecciona un tema (1 o 2): ")
            if tema == "1":
                cuestionario(preguntas["ciudades"])
            elif tema == "2":
                cuestionario(preguntas["animales"])
            else:
                print("Tema inválido. Regresando al menú.")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

main()

