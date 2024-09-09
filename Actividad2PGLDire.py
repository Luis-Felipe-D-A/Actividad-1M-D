class Usuario:
    def __init__(self, nombrecompleto, nickname, clave, tipo, fecha_creacion):
        self.datos = {
            "Nombrecompleto": nombrecompleto,
            "nickname": nickname,
            "clave": clave,
            "tipo": tipo,
            "fecha_creacion": fecha_creacion
        }

    def imprimir_datos(self):
        for key, value in self.datos.items():
            print(f"{key}: {value}")

    def buscar(self, value):
        return value in self.datos.values()

def agregar_usuario():
    nombrecompleto = input("Ingrese el nombre completo: ")
    nickname = input("Ingrese el nickname: ")
    clave = input("Ingrese la clave: ")
    tipo = input("Ingrese el tipo: ")
    fecha_creacion = input("Ingrese la fecha de creación: ")
    usuario = Usuario(nombrecompleto, nickname, clave, tipo, fecha_creacion)
    usuarios.append(usuario)
    print("Usuario agregado ")

def buscar_usuario(value):
    for usuario in usuarios:
        if usuario.buscar(value):
            return usuario
    return None

def eliminar_usuario(value):
    global usuarios
    usuarios = [usuario for usuario in usuarios if not usuario.buscar(value)]
    print("Usuario eliminado ")

def menu():
    while True:
        print("\nMenu:"
              "\n1. Agregar Usuario"
              "\n2. Buscar Usuario"
              "\n3. Eliminar Usuario")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            value = input("Puede Ingresar el nombre completo o nickname o el tipo o la fecha de creación del usuario para buscar: ")
            usuario = buscar_usuario(value)
            if usuario:
                print("Usuario encontrado:")
                usuario.imprimir_datos()
            else:
                print("Usuario no encontrado.")
        elif opcion == '3':
            value = input("Puede Ingresar el nombre completo o nickname o el tipo del usuario para eliminar: ")
            eliminar_usuario(value)
        else:
            print("Opcion no válida.")

usuarios = []

menu()
