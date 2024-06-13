import json
import random

class Contraseña:
    def __init__(self, plataforma, contraseña):
        self.plataforma = plataforma
        self.contraseña = contraseña

class Contraseña_aleatoria:
    def __init__(self,numeros, letras, simbolos):
        self.numeros = numeros
        self.letras = letras
        self.simbolos = simbolos










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
        
class GestorContraseñas:
    def __init__(self):
        self.contraseñas = Gestion_Archivo.cargar_contraseñas()

    def agregar_contraseña(self, plataforma, contraseña):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}.")
                return
        self.contraseñas.append(Contraseña(plataforma, contraseña))
        print(f"Contraseña para {plataforma} agregada con éxito.")

    def buscar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"La contraseña de {plataforma} es {contr.contraseña}.")
                return
        print(f"No se encontró contraseña para {plataforma}.")

    def actualizar_contraseña(self, plataforma, nueva_contraseña):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                contr.contraseña = nueva_contraseña
                print(f"Contraseña para {plataforma} actualizada con éxito.")
                return
        print(f"No se encontró contraseña para {plataforma}. No se realizó ninguna actualización.")

    def eliminar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                self.contraseñas.remove(contr)
                print(f"Contraseña para {plataforma} eliminada con éxito.")
                return
        print(f"No se encontró contraseña para {plataforma}. No se realizó ninguna eliminación.")

    def mostrar_contraseñas(self):
        if self.contraseñas:
            print("Contraseñas almacenadas:")
            for contr in self.contraseñas:
                print(f"Plataforma: {contr.plataforma}, Contraseña: {contr.contraseña}")
        else:
            print("No hay contraseñas almacenadas.")

    def generar_contraseña_aleatoria(self):
        caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
        contraseña = "".join(random.choice(caracteres) for _ in range(12))
        return contraseña

    def menu(self):
        while True:
            print("\n------ MENU ------")
            print("1. Agregar contraseña")
            print("2. Buscar contraseña")
            print("3. Actualizar contraseña")
            print("4. Eliminar contraseña")
            print("5. Mostrar contraseñas")
            print("6. Salir y guardar datos")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                plataforma = input("Ingrese plataforma: ")
                contraseña = input("Ingrese contraseña: ")
                self.agregar_contraseña(plataforma, contraseña)
            elif opcion == "2":
                plataforma = input("Ingrese plataforma: ")
                self.buscar_contraseña(plataforma)
            elif opcion == "3":
                plataforma = input("Ingrese plataforma: ")
                nueva_contraseña = input("Ingrese nueva contraseña: ")
                self.actualizar_contraseña(plataforma, nueva_contraseña)
            elif opcion == "4":
                plataforma = input("Ingrese plataforma: ")
                self.eliminar_contraseña(plataforma)
            elif opcion == "5":
                self.mostrar_contraseñas()
            elif opcion == "6":
                Gestion_Archivo.guardar_contraseñas(self.contraseñas)
                print("Guardando contraseñas y saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

gestor = GestorContraseñas()
gestor.menu()
