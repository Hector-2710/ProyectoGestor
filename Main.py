import json
import random
import string


class GestionArchivo:
    @staticmethod
    def guardar_contraseñas(contraseñas, filename="contraseñas.json"):
        contraseñas_dict = {contr.plataforma: contr.contraseña for contr in contraseñas}
        with open(filename, "w") as file:
            json.dump(contraseñas_dict, file, indent=4)

    @staticmethod
    def cargar_contraseñas(filename="contraseñas.json"):
        try:
            with open(filename, "r") as file:
                contraseñas_dict = json.load(file)
                return [Contraseña(plataforma, contraseña) for plataforma, contraseña in contraseñas_dict.items()]
        except FileNotFoundError:
            print(f"El archivo {filename} no fue encontrado\n")
            return []


class Contraseña:
    def __init__(self, plataforma, contraseña):
        self.plataforma = plataforma
        self.contraseña = contraseña


class GestorContraseñas:
    def __init__(self):
        self.contraseñas = GestionArchivo.cargar_contraseñas()

    def agregar_contraseña(self, plataforma, contraseña):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}\n")
                return
        self.contraseñas.append(Contraseña(plataforma, contraseña))
        print(f"Contraseña para {plataforma} agregada con exito")
        print(f"Plataforma: {plataforma}, Contraseña: {contraseña}\n")

    def buscar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print("Contraseña encontrada")
                print(f"Plataforma: {plataforma}, Contraseña: {contr.contraseña}\n")
                return
        print(f"No se encontro la contraseña de {plataforma}\n")

    def actualizar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print("1. Actualizar con una nueva contraseña manual")
                print("2. Actualizar con una contraseña aleatoria")
                opcion = input("Seleccione una opcion:\n")
                if opcion == "1":
                    nueva_contraseña = input(f"Ingrese la nueva contraseña para {plataforma}:\n")
                    contr.contraseña = nueva_contraseña
                    print(f"Contraseña para {plataforma} actualizada con exito")
                    print(f"Plataforma: {plataforma}, Contraseña: {nueva_contraseña}\n")
                    return
                elif opcion == "2":
                    while True:
                        try:
                            largo = int(input("Seleccione un largo mayor o igual que 4:\n"))
                            if largo < 4:
                                print("La contraseña debe tener un largo mayor o igual que 4 caracteres\n")
                            else:
                                nueva_contraseña = self._generar_contraseña_aleatoria(largo)
                                contr.contraseña = nueva_contraseña
                                print(f"Contraseña para {plataforma} actualizada con exito")
                                print(f"Plataforma: {plataforma}, Contraseña: {nueva_contraseña}\n")
                                return
                        except ValueError:
                            print("Debe ingresar un numero valido para el largo de la contraseña")
                else:
                    print("Opcion no valida, intente de nuevo")
                    return
        print(f"No se encontro contraseña para {plataforma}\n")

    def eliminar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                self.contraseñas.remove(contr)
                print(f"Contraseña para {plataforma} eliminada con exito\n")
                return
        print(f"No se encontro la contraseña de {plataforma}")

    def mostrar_contraseñas(self):
        if self.contraseñas:
            print("Contraseñas almacenadas:\n")
            for contr in self.contraseñas:
                print(f"Plataforma: {contr.plataforma}, Contraseña: {contr.contraseña}\n")
        else:
            print("No hay contraseñas almacenadas\n")

    def generar_contraseña_aleatoria(self, plataforma, largo):
        if largo < 4:
            print("La contraseña debe tener un largo mayor o igual que 4 caracteres\n")
            return
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}")
                return
        contraseña = self._generar_contraseña_aleatoria(largo)
        print(f"Contraseña aleatoria generada con exito")
        print(f"Plataforma: {plataforma}, Contraseña: {contraseña}\n")
        self.contraseñas.append(Contraseña(plataforma, contraseña))

    def _generar_contraseña_aleatoria(self, largo):
        simbolos = "!@#$%^&*"
        contraseña = random.sample(string.ascii_letters + string.digits + simbolos, largo)
        random.shuffle(contraseña)
        return ''.join(contraseña)

    def menu(self):
        while True:
            print("------ MENU ------\n")
            print("1. Agregar contraseña")
            print("2. Buscar contraseña")
            print("3. Actualizar contraseña")
            print("4. Eliminar contraseña")
            print("5. Mostrar contraseñas")
            print("6. Salir y guardar datos")
            opcion = input("Selecciona una opcion:")

            if opcion == "1":
                plataforma = input("Ingrese plataforma:\n")
                while True:
                    print("1. Agregar contraseña manual")
                    print("2. Agregar contraseña aleatoria")
                    sub_opcion = input("Seleccione una opcion:\n")
                    if sub_opcion == "1":
                        contraseña = input(f"Ingrese contraseña para {plataforma}:\n")
                        self.agregar_contraseña(plataforma, contraseña)
                        break
                    elif sub_opcion == "2":
                        try:
                            largo = int(input("Ingrese el largo de la contraseña (debe ser mayor o igual que 4):\n"))
                            if largo < 4:
                                print("Debe ser mayor o igual que 4 caracteres\n")
                            else:
                                self.generar_contraseña_aleatoria(plataforma, largo)
                                break
                        except ValueError:
                            print("Debe ingresar un numero valido para el largo de la contraseña\n")
                    else:
                        print("Opcion no valida, intente de nuevo\n")
            elif opcion == "2":
                plataforma = input("Ingrese plataforma:\n")
                self.buscar_contraseña(plataforma)
            elif opcion == "3":
                plataforma = input("Ingrese la plataforma que desea actualizar:\n")
                self.actualizar_contraseña(plataforma)
            elif opcion == "4":
                plataforma = input("Ingrese la plataforma que desea eliminar:\n")
                self.eliminar_contraseña(plataforma)
            elif opcion == "5":
                self.mostrar_contraseñas()
            elif opcion == "6":
                GestionArchivo.guardar_contraseñas(self.contraseñas)
                print("Guardando contraseñas y saliendo...\n")
                break
            else:
                print("Opcion no valida, intente de nuevo\n")

gestor = GestorContraseñas()
gestor.menu()
