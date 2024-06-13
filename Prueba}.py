
import json
import random

class Contraseña:
    def __init__(self, plataforma, contraseña):
        self.plataforma = plataforma
        self.contraseña = contraseña

    def __str__(self):
        return f"Plataforma: {self.plataforma}, Contraseña: {self.contraseña}"

class Gestion_Archivo:
    @staticmethod
    def guardar_contraseñas(contraseñas, filename="contraseñas.json"):
        # Convertir lista de Contraseña a diccionario
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
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON en {filename}: {str(e)}")
            return []
        except Exception as e:
            print(f"Error inesperado al cargar contraseñas: {str(e)}")
            return []


class GestorContraseñas:
    def __init__(self):
        self.contraseñas = Gestion_Archivo.cargar_contraseñas()

    def guardar_contraseñas(self):
        Gestion_Archivo.guardar_contraseñas(self.contraseñas)

    def agregar_contraseña(self, plataforma, contraseña):
        if any(contr.plataforma == plataforma for contr in self.contraseñas):
            print(f"¡Ya existe una contraseña para {plataforma}!")
        else:
            nueva_contraseña = Contraseña(plataforma, contraseña)
            self.contraseñas.append(nueva_contraseña)
            print(f"Contraseña para {plataforma} agregada correctamente.")
            self.guardar_contraseñas() 

    def generar_contraseña_aleatoria(self):
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(caracteres) for _ in range(12))

    def buscar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                return contr.contraseña
        return None

    def actualizar_contraseña(self, plataforma, nueva_contraseña):
        contraseña_actualizada = False
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                contr.contraseña = nueva_contraseña
                print(f"Contraseña para {plataforma} actualizada correctamente.")
                contraseña_actualizada = True
                break
        
        if contraseña_actualizada:
            self.guardar_contraseñas()  # Guardar después de actualizar
        else:
            print(f"No se encontró una contraseña para {plataforma}.")

    def eliminar_contraseña(self, plataforma):
        contraseña_eliminada = False
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                self.contraseñas.remove(contr)
                print(f"Contraseña para {plataforma} eliminada correctamente.")
                contraseña_eliminada = True
                break
        
        if contraseña_eliminada:
            self.guardar_contraseñas()  # Guardar después de eliminar
        else:
            print(f"No se encontró una contraseña para {plataforma}.")

    def mostrar_contraseñas(self):
        if self.contraseñas:
            print("Contraseñas actuales:")
            for contr in self.contraseñas:
                print(contr)
        else:
            print("No hay contraseñas almacenadas.")

    def menu(self):
        while True:
            print("\n------MENU------")
            print("Selecciona una opción:")
            print("1. Agregar contraseña")
            print("2. Buscar contraseña")
            print("3. Actualizar contraseña")
            print("4. Eliminar contraseña")
            print("5. Mostrar contraseñas")
            print("6. Salir y guardar datos")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                plataforma = input("Ingrese la plataforma: ")
                opcion_contraseña = input("¿Desea ingresar manualmente la contraseña (1) o generar una aleatoria (2)?: ")
                if opcion_contraseña == "1":
                    contraseña = input("Ingrese la contraseña: ")
                elif opcion_contraseña == "2":
                    contraseña = self.generar_contraseña_aleatoria()
                    print(f"Contraseña generada aleatoriamente: {contraseña}")
                self.agregar_contraseña(plataforma, contraseña)

            elif opcion == "2":
                plataforma = input("Ingrese la plataforma: ")
                contraseña = self.buscar_contraseña(plataforma)
                if contraseña:
                    print(f"La contraseña de {plataforma} es: {contraseña}")
                else:
                    print(f"No se encontró una contraseña para {plataforma}.")

            elif opcion == "3":
                plataforma = input("Ingrese la plataforma cuya contraseña desea actualizar: ")
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                self.actualizar_contraseña(plataforma, nueva_contraseña)

            elif opcion == "4":
                plataforma = input("Ingrese la plataforma cuya contraseña desea eliminar: ")
                self.eliminar_contraseña(plataforma)

            elif opcion == "5":
                self.mostrar_contraseñas()

            elif opcion == "6":
                self.guardar_contraseñas()
                print("Datos guardados. Saliendo del programa...")
                break

            else:
                print("Opción no válida. Inténtelo nuevamente.")


gestor = GestorContraseñas()
gestor.menu()
