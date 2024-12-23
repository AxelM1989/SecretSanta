import streamlit as st
import random
import time


# Configuración de la página
st.set_page_config(
    page_title="Secret Santa",
    page_icon="🎅",
    layout="wide",
)

# Inicialización del estado global
if "pista_actual" not in st.session_state:
    st.session_state.pista_actual = 1
if "rinconcito_visible" not in st.session_state:
    st.session_state.rinconcito_visible = False
if "intentos_restantes" not in st.session_state:
    st.session_state.intentos_restantes = 3
if "historial_intentos" not in st.session_state:
    st.session_state.historial_intentos = []
if "siguiente_pista" not in st.session_state:
    st.session_state.siguiente_pista = False
if "pistas_adivinadas" not in st.session_state:
    st.session_state.pistas_adivinadas = []
if "nombre_adivinado" not in st.session_state:
    st.session_state.nombre_adivinado = False
if "omitido" not in st.session_state:
    st.session_state.omitido = False


# Función para avanzar de pista
def avanzar_pista():
    st.session_state.pista_actual += 1

# Configuración del menú
menu = ["My Secret Santa"]
if st.session_state.rinconcito_visible:
    menu.append("El Rinconcito de Tin")
opcion = st.sidebar.radio("Menú", menu)

# Nombre correcto
nombre_correcto = "Agustin Ferreiro"



# Página principal
if opcion == "My Secret Santa":
    # Título y bienvenida
    st.markdown(
        """
        <h1 style="text-align: center; color: #228B22;">
            🎅🏻 🎁 Bienvenidos a mi Secret Santa 🎁 🎅🏻
        </h1>
        <h3 style="text-align: center; color: #FF6347;">
            ¡Prepárate para una experiencia navideña única y divertida!
        </h3>
        """,
        unsafe_allow_html=True,
    )

# Imagen de bienvenida
st.image(
    "Secret Santa.webp",

    caption="¿Puedes descubrir quién es mi amigo invisible? 🎄",
    use_container_width=True,  # Ajuste para usar el ancho del contenedor
)

# Texto de introducción
st.write(
    """
    ### 👋 ¿Qué es Secret Santa? 🎅 🎄
    Secret Santa es un juego donde el objetivo principal es sorprender a alguien especial. 
    En esta app, tendrás pistas, juegos y sorpresas únicas diseñadas para hacer tu experiencia más interactiva y memorable.
    """
)

st.markdown(
    """
    <h1 style="text-align: center; color: #FF6347;">
        🎁 Bienvenidos al Desafío 🎄
    </h1>
    <br>
    <h3 style="text-align: center; color: #228B22;">
        ¡Desafíate a adivinar quién me tocó como amigo invisible!
    </h3>
    <p style="text-align: justify; font-size: 18px;">
        El objetivo del juego es simple: <strong>ir resolviendo las pistas</strong> para adivinar quién es mi Secret Santa. 
        Pero hay una regla muy importante: <strong>¡no puedes elegirte a ti mismo!</strong> Si te das cuenta de que eres tú, 
        <em>shhh 🤫</em>, no lo digas y deja que los demás sigan jugando.  
    </p>
    <p style="text-align: justify; font-size: 18px;">
        Cada pista te acercará más al secreto, pero cuidado, ¡no será tan fácil! Prepárate para un desafío lleno de risas, deducciones y sorpresas navideñas 🎄.
    </p>
    <p style="text-align: justify; font-size: 18px;">
        Serán 6 pistas que te brindarán información sobre la persona correcta. En 2 de ellas se deberá adivinar la respuesta correcta, y en las restantes no será necesario.
        Hay 2 caminos: Si se aciertan estas 2 pistas, el nombre de mi Secret Santa se develará de manera autumática. También se pueden omitir las pistas, pero en este caso, solo el juego estará terminado si se escribe el nombre correcto manualmente.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()




# --------- PISTA 1: Múltiple Choice con botón omitir ----------
if st.session_state.pista_actual == 1:
    # Descripción introductoria
    st.markdown(
        """
        <h3 style="color: #FF6347; text-align: center;">
            ¡Comencemos con la primera pista! 🕵️‍♂️
        </h3>
        <p style="text-align: justify; font-size: 16px;">
            En esta simple pista, debes analizar un fragmento de código DAX y descubrir que está calculando. 
            ¡Presta atención, es el primer paso clave para resolver el desafío! El resultado será la primer pista 💡
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.title("🧩 Código DAX - Pista #1")

    # Mostrar el código DAX
    codigo_dax = """
    Genero_Mas_Probable = 
    MAXX(
        TOPN(
            1,
            VALUES(EmpleadosBI[Genero]),
            CALCULATE(COUNTROWS(EmpleadosBI)),
            DESC
        ),
        EmpleadosBI[Genero]
    )
    """
    st.code(codigo_dax, language="r")
    st.write("Selecciona el género con mayor probabilidad:")

    # Radio button
    genero_seleccionado = st.radio(
        "¿Cuál crees que es el género más frecuente?",
        options=["Femenino", "Masculino"],
        index = None
    )

    # Botón omitir
    if st.button("Omitir"):
        st.session_state.omitido = True
        avanzar_pista()
        st.info("Has omitido esta pista. ¡Pasemos a la siguiente!")
        st.rerun()

    # Botón continuar si es correcto
    if genero_seleccionado == "Masculino" and not st.session_state.omitido:
        st.success("¡Correcto! Has adivinado la pista. 🎉")
        st.session_state.pistas_adivinadas.append(1)
        avanzar_pista()
        # Mostrar botón para avanzar si está desbloqueada la siguiente pista
        if st.button("Continuar a la siguiente pista ➡️"):
                st.success("¡Bien hecho! Ahora puedes avanzar a la siguiente pista. 🎉")
    elif genero_seleccionado =="Femenino":
        st.error("La respuesta es incorrecta.")

# --------- PISTA 2: Adivinar la Edad ----------
elif st.session_state.pista_actual == 2:
    st.title("Pista 2: Adivina la Edad 🎯")
    st.write("Intenta adivinar si el número que ingresas está dentro del rango correcto. No necesitas saber la edad exacta, solo si se encuentra en el rango. Usa tus intentos inteligentemente, tendrás solo 3.")


    # Parámetros
    rango_min = 25
    rango_max = 35

    # Inicializar variables si no existen
    if "intentos_restantes" not in st.session_state:
        st.session_state.intentos_restantes = 3
    if "historial_intentos" not in st.session_state:
        st.session_state.historial_intentos = []

    # Mostrar intentos restantes
    st.write(f"Tienes **{st.session_state.intentos_restantes} intentos restantes**.")

    # Input de número
    if st.session_state.intentos_restantes > 0:
        respuesta = st.number_input(
            "Introduce una edad para adivinar:", min_value=0, max_value=100, step=1
        )

        # Botón para intentar
        if st.button("Intentar"):
            if respuesta is not None:
                # Registrar intento
                st.session_state.historial_intentos.append(respuesta)
                st.session_state.intentos_restantes -= 1

                # Mensaje si está dentro del rango o no
                if rango_min <= respuesta <= rango_max:
                    st.success("La edad está dentro del rango. ¡Bien hecho! 🎉")
                else:
                    st.warning("La edad **no está dentro del rango**. Sigue intentando.")
        # Botón omitir
        if st.button("Omitir"):
            st.session_state.omitido = True
            avanzar_pista()
            st.info("Has omitido esta pista. ¡Pasemos a la siguiente!")
            st.rerun()

    # Mostrar historial de intentos
    if st.session_state.historial_intentos:
            st.write("### 📜 Historial de Intentos")
            for i, intento in enumerate(st.session_state.historial_intentos, 1):
                st.write(f"**Intento {i}:** {intento}")
    # Mostrar resultados solo cuando se completan los 3 intentos
    if st.session_state.intentos_restantes == 0:
        menor_intento = min(st.session_state.historial_intentos)
        mayor_intento = max(st.session_state.historial_intentos)

        # Avanzar a la siguiente pista
        avanzar_pista()
        # Avanzar automáticamente a la siguiente pista

        if st.button("Continuar a la siguiente pista ➡️"):
            st.success("¡Bien hecho! Ahora puedes avanzar a la siguiente pista. 🎉")



# --------- PISTA 3: Reemplazo de función SQL ----------
elif st.session_state.pista_actual == 3:
    st.title("Pista 3: Completa la consulta SQL 💻")
    st.write(
        "Hay una función de SQL que reemplazandola por `FUNCIONSQL` en la consulta siguiente, podemos traer la carrera estudiada (en inglés) por dicha persona:"
    )

    # Mostrar el código SQL
    codigo_sql = '''
    SELECT nombre, apellido, carrera_estudiada
    FROM Infracommerce.Empleados.Data_BI
    WHERE carrera_estudiada LIKE "%FUNCIONSQL%"
    '''
    st.code(codigo_sql, language='sql')

    # Input de función SQL
    funcion_sql = st.text_input("¿Cuál es la función SQL que completa la consulta? Click enter para tomar el nombre").strip()
    # Botón omitir
    if st.button("Omitir"):
        st.session_state.omitido = True
        avanzar_pista()
        st.info("Has omitido esta pista. ¡Pasemos a la siguiente!")
        st.rerun()

    if funcion_sql.upper() == "COUNT":
        st.success("¡Correcto! La función es `COUNT`. 🎉")
        st.session_state.pistas_adivinadas.append(1)
        if st.button("Continuar a la siguiente pista ➡️"):
            avanzar_pista()
            st.rerun()


    elif funcion_sql:
        st.warning("Respuesta incorrecta. Intenta nuevamente.")


# Nueva pista - Código Python para contar caracteres de la ciudad
elif st.session_state.pista_actual == 4:
    st.title("Pista 4: Datos sobre donde vive actualmente🏠")
    st.write("*Información complementaria:* 'Ciudad' es una variable con el nombre real de su ciudad")

# Mostrar el código Python como pista
    st.code("""
    
print(len(ciudad))
= 6
""", language="python")
    if st.button("Continuar a la siguiente pista ➡️"):
        avanzar_pista()
        st.rerun()


# --------- PISTA 5: Nota musical en Python ----------
elif st.session_state.pista_actual == 5:
    st.subheader("Pista 5: ¿Notas algo musical? 🎶")
    st.write(
        "Descifrando este código encontrarás otra pista:"
    )

    # Mostrar el código Python
    codigo_pista_5 = """
    empleados = [ "nombre&apellido"]

    notas_musicales = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

    resultados = [
        emp for emp in empleados if any(nota.lower() in emp["nombre&apellido"].lower() for nota in notas_musicales)
    ]

    if resultados:
        for res in resultados:
            print(f"Nombre completo: {res['nombre&apellido']}")
    else:
        print("No se encontraron coincidencias con notas musicales.")
    """
    st.code(codigo_pista_5, language="python")
    if st.button("Continuar a la siguiente pista ➡️"):
        avanzar_pista()
        st.rerun()

# --------- RESULTADO FINAL: Adivinar el nombre ----------

elif st.session_state.pista_actual == 6:


    if len(st.session_state.pistas_adivinadas) >= 3:
        st.title("👏 Eres el/la **** amo/a 👨‍🎓👩‍🎓 🤴")
        st.subheader("Sherlock te está buscando 🕵️ 👀 ")
        st.success(f"¡Felicidades! Al adivinar todas las pistas, has descubierto el misterio: {nombre_correcto} es mi Secret Santa🎉")
        st.session_state.rinconcito_visible = True
        st.session_state.nombre_adivinado = True
        if st.checkbox("Click para continuar"):
            st.write(
                "Has completado el desafío con éxito. En el menú de la izquierda puedes acceder a El Rinconcito de Tin")



    else:
        st.title("¡Adivina el nombre! 🎅")
        st.write("Debido a que omitiste pistas, debes acertar el nombre exacto para ganar.")
        # Input para ingresar el nombre
        nombre_input = st.text_input("Ingresa el nombre exacto:").strip()
    # Verificación del nombre
        if nombre_input.lower() == nombre_correcto.lower():
            st.success(f"¡Felicidades! Has descubierto el nombre: {nombre_correcto} es mi Secret Santa🎉")
            st.session_state.rinconcito_visible = True
            st.session_state.nombre_adivinado = True
            if st.checkbox("Desbloquear el Rinconcito de Tin"):
                st.write(
                 "Has completado el desafío con éxito. En el menú de la izquierda puedes acceder a El Rinconcito de Tin")


        elif nombre_input:
            st.error("¡Incorrecto! Intenta nuevamente.")
            if 'intentos' not in st.session_state:
                st.session_state.intentos = 0
            if 'rinconcito_visible' not in st.session_state:
                st.session_state.rinconcito_visible = False
            st.session_state.intentos += 1
            # Proveer pistas dependiendo del intento
            if st.session_state.intentos == 1:
                st.info("Pista extra#1: Está asociado con un animal.")
            elif st.session_state.intentos == 2:
                st.info("Pista extra#2: Vamos a irnos a Argentina a buscar la respuesta correcta.✈️")

            else:
                st.error("Basta. ¿De verdad vas a seguir intentando?.")


# --------- MENSAJE FINAL ----------

if st.session_state.rinconcito_visible and opcion == "El Rinconcito de Tin":

    st.markdown("---")
    st.markdown(

        """
        <h1 style="text-align: center; color: #FFD700;">
            🎉 Bienvenidos a El Rinconcito de Tin 🎉
        </h1>
        <p style="text-align: center;">
            Aquí encontrarás contenido especial dedicado a Agustin.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.image(
        "Goat.webp",

        use_container_width=True,  # Ajuste para usar el ancho del contenedor
    )


    st.image(
        "Tipaso.jpg",


    )

    st.markdown("----")
    st.markdown("### 🎶 Escucha esta canción personalizada para él 🎧")
    st.audio("El Gran Tin.mp3")

    st.markdown("----")

    # Título del juego
    st.markdown("<h1 style='color:  #1E3A8A;'>Sección juegos: 🎮🎯🎲🎰</h1>", unsafe_allow_html=True)

    st.markdown("")
    st.subheader("❓0️ Adivina el Número 🔢")
    st.markdown("")
    st.write("Debes elegir un número random del 1 al 100 y te dirá si el número es alto o bajo. Lo podes intentar hasta que lo resuelvas."
             "El puntaje se calcula de acuerdo con la cantidad de intentos. La fórmula es simple: el puntaje máximo es 100 y se reduce en 10 puntos por cada intento fallido. De esta forma, si el jugador adivina el número en el primer intento, obtiene un puntaje máximo. Si tarda más, el puntaje disminuye.")

    # Inicializar las variables en st.session_state si no están definidas
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.score = 0  # Puntaje inicial

    # Solicitar al usuario que ingrese un número
    user_guess = st.number_input("Ingresa un número entre 1 y 100:", min_value=1, max_value=100)

    # Botón para enviar la respuesta
    if st.button("Adivinar"):
        st.session_state.attempts += 1

        # Verificar si la respuesta es correcta
        if user_guess < st.session_state.number:
            st.write("Demasiado bajo. ¡Intenta de nuevo!")
        elif user_guess > st.session_state.number:
            st.write("Demasiado alto. ¡Intenta de nuevo!")
        else:
            st.write(
                f"¡Felicidades! Adivinaste el número {st.session_state.number} en {st.session_state.attempts} intentos.")

            # Calcular el puntaje (ejemplo: mayor puntaje si menos intentos)
            st.session_state.score = max(0, 100 - st.session_state.attempts * 10)  # Reduce puntaje con cada intento

            # Mostrar el puntaje final
            st.write(f"Tu puntaje es: {st.session_state.score}")

            # Reiniciar el juego
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.score = 0  # Reiniciar el puntaje

    st.info("Después de adivinar correctamente el número, el juego se reinicia con un nuevo número aleatorio y el puntaje se muestra.")


    st.markdown("----")
    st.markdown("")

    # Título del juego
    st.subheader("Piedra🦪, Papel📄 o Tijera✂️" )

    # Opciones de elección
    options = ["Piedra", "Papel", "Tijera"]

    # Elección del usuario
    user_choice = st.selectbox("Elige: Piedra, Papel o Tijera", options)

    # Elección de la computadora
    computer_choice = random.choice(options)

    # Mostrar las elecciones
    st.write(f"Tú elegiste: {user_choice}")
    st.write(f"La computadora eligió: {computer_choice}")

    # Determinar el resultado
    if user_choice == computer_choice:
        st.write("¡Es un empate!")
    elif (user_choice == "Piedra" and computer_choice == "Tijera") or \
            (user_choice == "Papel" and computer_choice == "Piedra") or \
            (user_choice == "Tijera" and computer_choice == "Papel"):
        st.write("¡Ganaste!")
    else:
        st.write("¡Perdiste!")

    st.markdown("----")
    st.markdown("")

   # Lista de palabras
palabras = [
    "Python", "SQL", "Power BI", "Tableau", "Looker", "Qlik Sense", "Streamlit",
    "Business Intelligence", "Data Analysis", "Data Science", "Data Engineering",
    "Data Visualization", "Primary Key", "Foreign Key", "Key Performance Indicator",
    "ETL", "ELT", "Data Mining", "Datawarehouse", "Data Lake", "Data Governance",
    "Data Mart", "Database", "NO SQL", "Fact Table", "Dimension Table",
    "Artificial Intelligence", "API", "Big Data", "Business Analytics", "Clustering",
    "Cardinality", "Dashboard", "Data Modeling", "Data Source", "Data Transformation",
    "Entity", "Exploratory Data Analysis", "Forecast", "Hierarchy", "Histogram",
    "Hadoop", "Index", "Insights", "Internet Of Things", "JSON", "CSV", "Parquet",
    "Avro", "Key", "Logical Model", "Machine Learning", "Measure", "Metric",
    "Metadata", "Normalization", "Outlier", "Predictive Analysis", "Descriptive Analysis",
    "Query", "Relationship", "Relational Database", "Report", "Row", "Schema",
    "Segmentation", "Snowflake Model", "Star Model", "Stored Procedure",
    "Structured Data", "Table", "Left Join", "Inner Join", "Unique Key",
    "Web Analytics"
]

# Estado inicial del juego
if "palabra_secreta" not in st.session_state:
    st.session_state.palabra_secreta = random.choice(palabras).lower()
    st.session_state.palabra_oculta = [
        "_" if c != " " else " " for c in st.session_state.palabra_secreta
    ]
    st.session_state.intentos = 5
    st.session_state.letras_usadas = set()

st.title("Adivina la palabra")
st.write("Debes colocar letras hasta poder adivinar la palabra oculta. Tienes hasta 5 intentos fallidos. Las palabras son todas relacionadas al área de BI y dado que muchas de ellas son en inglés, para unificar criterios, todas las palabras incluidas que puedan aparecer, son en inglés")

# Mostrar progreso de la palabra
progreso = "".join(
    [
        c.upper() if c in st.session_state.letras_usadas else "_" if c != " " else "[ ]"
        for c in st.session_state.palabra_secreta
    ]
)
st.write(f"Palabra: {progreso}")
st.write(f"Intentos restantes: {st.session_state.intentos}")

# Botón para reiniciar el juego
if st.button("🔄 Reiniciar Juego"):
    st.session_state.palabra_secreta = random.choice(palabras).lower()
    st.session_state.palabra_oculta = [
        "_" if c != " " else " " for c in st.session_state.palabra_secreta
    ]
    st.session_state.intentos = 5
    st.session_state.letras_usadas = set()
    st.rerun()

# Verificar si el usuario ha ganado o perdido
if "_" not in progreso.replace("[ ]", " "):
    st.success(f"¡Felicidades! Has adivinado la palabra: {st.session_state.palabra_secreta.title()}")
elif st.session_state.intentos <= 0:
    st.error(f"¡Has perdido! La palabra era: {st.session_state.palabra_secreta.title()}")
else:
    # Entrada del usuario
    letra = st.text_input("Ingresa una letra:", max_chars=1).lower()

    if letra and letra.isalpha() and letra not in st.session_state.letras_usadas:
        st.session_state.letras_usadas.add(letra)

        # Actualizar la palabra oculta si la letra es correcta
        if letra in st.session_state.palabra_secreta:
            st.success(f"¡Correcto! La letra '{letra.upper()}' está en la palabra.")
        else:
            st.session_state.intentos -= 1
            st.warning(f"La letra '{letra.upper()}' no está en la palabra.")

        st.rerun()

# Mostrar letras usadas
if st.session_state.letras_usadas:
    letras_usadas = ", ".join(sorted(st.session_state.letras_usadas)).upper()
    st.write(f"Letras usadas: {letras_usadas}")

    # Título principal
    st.title("🔢 Juego de Memorización Numérica")
    st.markdown(
        """
        Memoriza la secuencia de números que aparece por unos segundos y luego escríbela en el mismo orden. 
        ¡Pon a prueba tu memoria y sube de nivel! 🧠
        """
    )

    # Inicialización de variables en la sesión
    if 'nivel' not in st.session_state:
        st.session_state.nivel = 1
    if 'secuencia' not in st.session_state:
        st.session_state.secuencia = [random.randint(0, 9) for _ in range(st.session_state.nivel + 4)]
    if 'mostrar' not in st.session_state:
        st.session_state.mostrar = True
    if 'puntuacion' not in st.session_state:
        st.session_state.puntuacion = 0

    # Mostrar la secuencia de números
    if st.session_state.mostrar:
        st.subheader(f"🕒 Nivel {st.session_state.nivel}: Memoriza esta secuencia:")
        st.markdown(
            f"<h2 style='color: blue;'>{' '.join(map(str, st.session_state.secuencia))}</h2>",
            unsafe_allow_html=True
        )
        # Botón para ocultar la secuencia y continuar
        if st.button("🕶️ Ocultar y continuar"):
            st.session_state.mostrar = False
            time.sleep(2)
            st.rerun()
    else:
        # Entrada del usuario para verificar la secuencia
        respuesta = st.text_input("✍️ Escribe la secuencia (separa los números con comas):")
        if st.button("✅ Verificar"):
            try:
                entrada = list(map(int, respuesta.split(',')))
                if entrada == st.session_state.secuencia:
                    st.success(f"🎉 ¡Correcto! Avanzas al siguiente nivel.")
                    st.session_state.nivel += 1
                    st.session_state.puntuacion += 10
                else:
                    st.error(
                        f"❌ Incorrecto. La secuencia era: "
                        f"<h2 style='color: red;'>{' '.join(map(str, st.session_state.secuencia))}</h2>",
                        icon="💔",
                    )
                    st.session_state.puntuacion = max(0, st.session_state.puntuacion - 5)

                # Generar nueva secuencia para el próximo nivel
                st.session_state.secuencia = [random.randint(0, 9) for _ in range(st.session_state.nivel + 4)]
                st.session_state.mostrar = True
                st.rerun()
            except ValueError:
                st.error("⚠️ Asegúrate de escribir números separados por comas.")

    # Mostrar puntuación y nivel al final del juego
    st.subheader("📊 Progreso del Juego")
    st.write(f"**Nivel Actual:** {st.session_state.nivel}")
    st.write(f"**Puntuación:** {st.session_state.puntuacion}")

    # Botón para reiniciar el juego
    if st.button("🔄 Reiniciar Juego"):
        st.session_state.nivel = 1
        st.session_state.secuencia = [random.randint(0, 9) for _ in range(5)]
        st.session_state.mostrar = True
        st.session_state.puntuacion = 0
        st.rerun()
        
    st.subdivider()
    st.subheader("Para mi amigo Tin")
    st.image(
        "Carta.png",

        use_container_width=True,  # Ajuste para usar el ancho del contenedor
    )

    st.image(
        "GOAT2.webp",

        use_container_width=True,  # Ajuste para usar el ancho del contenedor
    )

