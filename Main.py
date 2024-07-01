import json
import random
import string


class Gestion_Archivo:
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
            print(f"El archivo {filename} no fue encontrado.")
            return []


class Contraseña:
    def __init__(self, plataforma, contraseña):
        self.plataforma = plataforma
        self.contraseña = contraseña


class GestorContraseñas:
    def __init__(self):
        self.contraseñas = Gestion_Archivo.cargar_contraseñas()

    def agregar_contraseña(self, plataforma, contraseña):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}")
                return
        self.contraseñas.append(Contraseña(plataforma, contraseña))
        print(f"Contraseña para {plataforma} agregada con éxito.")
        print(f"Plataforma: {plataforma}, Contraseña: {contraseña}")

    def buscar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print("Contraseña encontrada")
                print(f"Plataforma: {plataforma}, Contraseña: {contr.contraseña}")
                return
        print(f"No se encontró la contraseña de {plataforma}")

    def actualizar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print("1. Actualizar con una nueva contraseña manual")
                print("2. Actualizar con una contraseña aleatoria")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    nueva_contraseña = input(f"Ingrese la nueva contraseña para {plataforma}:\n")
                    contr.contraseña = nueva_contraseña
                    print(f"Contraseña para {plataforma} actualizada con éxito.")
                    print(f"Plataforma: {plataforma}, Contraseña: {nueva_contraseña}")
                    return
                elif opcion == "2":
                    try:
                        largo = int(input("Seleccione un largo de 4, 6, 8 o mayor que 10: "))
                        if largo not in [4, 6, 8] and largo < 10:
                            print("La contraseña debe tener un largo de 4, 6, 8 o ser mayor o igual a 10 caracteres.")
                            return
                        nueva_contraseña = self._generar_contraseña_aleatoria(largo)
                        contr.contraseña = nueva_contraseña
                        print(f"Contraseña para {plataforma} actualizada con éxito.")
                        print(f"Plataforma: {plataforma}, Contraseña: {nueva_contraseña}")
                    except ValueError:
                        print("Debe ingresar un número válido para el largo de la contraseña.")
                        return
                else:
                    print("Opción no válida, intente de nuevo.")
                    return
        print(f"No se encontró contraseña para {plataforma}")

    def eliminar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                self.contraseñas.remove(contr)
                print(f"Contraseña para {plataforma} eliminada con éxito.")
                return
        print(f"No se encontró la contraseña de {plataforma}")

    def mostrar_contraseñas(self):
        if self.contraseñas:
            print("Contraseñas almacenadas:\n")
            for contr in self.contraseñas:
                print(f"Plataforma: {contr.plataforma}, Contraseña: {contr.contraseña}")
        else:
            print("No hay contraseñas almacenadas")

    def generar_contraseña_aleatoria(self, plataforma, largo):
        if largo not in [4, 6, 8] and largo < 10:
            print("La contraseña debe tener un largo de 4, 6, 8 o ser mayor o igual a 10 caracteres.")
            return
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}.")
                return
        contraseña = self._generar_contraseña_aleatoria(largo)
        print(f"Contraseña aleatoria generada con éxito.")
        print(f"Plataforma: {plataforma}, Contraseña: {contraseña}")
        self.contraseñas.append(Contraseña(plataforma, contraseña))

    def _generar_contraseña_aleatoria(self, largo):
        simbolos = "!@#$%^&*"
        if largo in [4, 6, 8]:
            contraseña = random.sample(string.ascii_letters + string.digits + (simbolos if largo > 4 else ''), largo)
        elif largo > 10:
            contraseña = random.sample(simbolos, 2) + random.sample(string.digits, 4) + random.sample(string.ascii_letters, 4)
            digitos_adicionales = random.choices(string.ascii_letters + string.digits + simbolos, k=largo - 10)
            contraseña.extend(digitos_adicionales)
        else:
            raise ValueError("La longitud de la contraseña debe ser 4, 6, 8 o mayor que 10 caracteres.")
        random.shuffle(contraseña)
        return ''.join(contraseña)

    def menu(self):
        while True:
            print("------ MENU ------")
            print("1. Agregar contraseña")
            print("2. Buscar contraseña")
            print("3. Actualizar contraseña")
            print("4. Eliminar contraseña")
            print("5. Mostrar contraseñas")
            print("6. Salir y guardar datos\n")
            opcion = input("Selecciona una opción:")

            if opcion == "1":
                plataforma = input("Ingrese plataforma:\n")
                while True:
                    print("1. Agregar contraseña manual")
                    print("2. Agregar contraseña aleatoria")
                    sub_opcion = input("Seleccione una opción:\n")
                    if sub_opcion == "1":
                        contraseña = input(f"Ingrese contraseña para {plataforma}:\n")
                        self.agregar_contraseña(plataforma, contraseña)
                        break
                    elif sub_opcion == "2":
                        try:
                            largo = int(input("Ingrese el largo de la contraseña (debe ser 4, 6, 8 o mayor que 10):\n"))
                            if largo not in [4, 6, 8] and largo < 10:
                                print("Debe ser 4, 6, 8 o mayor o igual a 10 caracteres.")
                            else:
                                self.generar_contraseña_aleatoria(plataforma, largo)
                                break
                        except ValueError:
                            print("Debe ingresar un número válido para el largo de la contraseña.")
                    else:
                        print("Opción no válida, intente de nuevo.")
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
                Gestion_Archivo.guardar_contraseñas(self.contraseñas)
                print("Guardando contraseñas y saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

gestor = GestorContraseñas()
gestor.menu()
