Juego de Robot y Obstáculos
🎮 Descripción del Juego
Este es un juego de rompecabezas donde controlas un robot (🤖) que debe navegar por un tablero lleno de obstáculos (💥) y espacios vacíos (🟩). El objetivo es mover el robot para cubrir todos los espacios vacíos del tablero.

🛠️ Tecnologías Utilizadas
Python 3.x

Biblioteca estándar de Python (os)

Archivos de texto para los tableros de juego
📂Estructura de Archivos

.
├── board.py          # Lógica para leer y procesar tableros
├── juego.py          # Lógica principal del juego
├── movimiento.py     # Constantes de movimiento
└── nivel_1.board     # Archivo de tablero (ejemplo)

🕹️ Cómo Jugar
Controles:
W: Mover hacia arriba (↑)

A: Mover hacia izquierda (←)

S: Mover hacia abajo (↓)

D: Mover hacia derecha (→)

X: Salir del juego

Mecánicas:
El robot (🤖) puede moverse a espacios vacíos (🟩)
🤖 = Robot (tu personaje)
💥 = Obstáculo (no se puede pasar)
🟩 = Espacio vacío (objetivo a cubrir)
Al moverse, el robot deja un obstáculo (💥) en su posición anterior

Ganas cuando todos los espacios vacíos se convierten en obstáculos

🖥️ Interfaz del Juego

    1 2 3 
1 | 🤖 💥 🟩 | 1
2 | 🟩 💥 🟩 | 2
3 | 💥 🟩 💥 | 3
    1 2 3 
 🚀 Cómo Ejecutar
Clona el repositorio o descarga los archivos

Asegúrate de tener Python instalado

Ejecuta el juego con:   
python juego.py


🌎 Idiomas Disponibles

El juego tiene soporte para:

Español (es)

Inglés (en)

Puedes seleccionar el idioma al iniciar el juego.

🏆 Condición de Victoria
Ganas el juego cuando no quedan espacios vacíos (🟩) en el tablero. ¡El robot debe cubrir todo el terreno!

📝 Archivos de Tablero
Los tableros se definen en archivos .board con el formato:


# VARIABLES
r --> ROBOT
s --> ESPACIO
o --> MURO

# TABLERO
o o o o
o s r o
o s s o
o o o o

