SPACE = '🟩'
ROBOT = '🤖'
OBSTA = '💥'

def leer_tablero(nivel):

    tablero = []
    seccion = ""
    variables = {}

    with open(f"{nivel}.board","r") as f:
        lineas = f.readlines()
        
        for linea in lineas:
            linea = linea [:-1].strip()

            if linea in ("", "\n"):
                continue 

            if linea in ("# VARIABLES", "# TABLERO"):
                seccion = linea
                continue

            if seccion == "# VARIABLES":
                linea = linea.split("-->")
                var = linea[0].strip()
                tipo = linea[1].strip()

                if tipo == "ESPACIO":
                    tipo = SPACE
                elif tipo == "ROBOT":
                    tipo = ROBOT
                elif tipo == "MURO":
                    tipo = OBSTA


                variables [var] = tipo

            elif seccion == "# TABLERO":
                
                for var, tipo in variables.items():
                    linea = linea.replace(var, tipo)

            #linea = linea.replace("s", SPACE)
            #linea = linea.replace("r", ROBOT)
            #linea = linea.replace("o", OBSTA)

                linea = list(linea)
                tablero.append(linea)

    return tablero

if __name__=="__main__":
    tab = leer_tablero("nivel_1")        
