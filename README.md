# Juego de la vida
Implementación del famoso _Juego de la vida_ en Python. El programa depende de _gamepy_ y _numpy_. Se genera un tablero con unas formas predefinidas. Hay control con teclas del teclado y del ratón. 

# Funcionamiento
Lanzar el programa. Si se pulsa una tecla del teclado se para hasta que se vuelva a pulsar otra. Si se pulsa un botón distinto del izquierdo, se borra la celda pulsada en caso de estar _viva_. Si se pulsa el izquierdo, entonces revive. 

# Reglas del juego
1. Si la celda está muerta y tiene tres vecinos vivos, entonces revive. 
2. Si la celda está viva, pero tiene menos de dos vecinos o más de tres, entonces muere. 
