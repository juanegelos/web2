FILEPATH = "members1.txt"

def leer_archivo(pathfile=FILEPATH): #de esta forma defino el parametro por omision
    with open(pathfile, "r") as file_local: #Estas linea (10-11) reemplazan las lineas 7/8/9 comentadas y no es necesario cerrar el archivo
            todos_local = file_local.readlines()
    return todos_local        

def escribir_archivo(todos_arg, pathfile="members1.txt"):
    with open(pathfile, "w") as file:
            file.writelines(todos_arg)


