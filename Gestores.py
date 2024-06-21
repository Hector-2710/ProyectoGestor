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
                print(f"Ya existe una contraseña para {plataforma}.")
                return
        self.contraseñas.append(Contraseña(plataforma, contraseña))
        print(f"Contraseña para {plataforma} agregada con éxito.")

    def buscar_contraseña(self, plataforma):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print("contraseña encontrada")
                print(f"Plataforma:{plataforma} / Contraseña:{contr.contraseña}")
                return
        print(f"No se encontró contraseña para {plataforma}.")

    def actualizar_contraseña(self, plataforma, nueva_contraseña):
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                contr.contraseña = nueva_contraseña
                print(f"---Contraseña para {plataforma} actualizada con éxito---")
                return
        print(f"---No se encontró contraseña para {plataforma}---")

    def eliminar_contraseña(self, plataforma): #revisar porque creo que deveriamos eliminar la plataforma y no la contraseña    
        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                self.contraseñas.remove(contr)
                print(f"Contraseña para {plataforma} eliminada con éxito.")
                return
        print(f"No se encontró contraseña para {plataforma}.")

    def mostrar_contraseñas(self):
        if self.contraseñas:
            print("Contraseñas almacenadas:\n")
            for contr in self.contraseñas:
                print(f"Plataforma:{contr.plataforma} / Contraseña:{contr.contraseña}")
        else:
            print("---No hay contraseñas almacenadas---")
        
    def generar_contraseña_aleatoria(self, plataforma, largo): #contraseña para diferentes tipos de largo menores a 10.

        for contr in self.contraseñas:
            if contr.plataforma == plataforma:
                print(f"Ya existe una contraseña para {plataforma}.")
                return
            
        if largo < 10:
            print("La contraseña debe contener un mínimo de 10 caracteres.")
            return 
    
        simbolos = "!@#$%^&*()-_+="
        contraseña = []
    
        contraseña.extend(random.sample(simbolos, 2))
        contraseña.extend(random.sample(string.digits, 4))
        contraseña.extend(random.sample(string.ascii_letters, 4))
    
        if largo > 10:
            digitos_adicionales = random.choices(string.ascii_letters + string.digits + simbolos, k=largo-10)
            contraseña.extend(digitos_adicionales)
    
        random.shuffle(contraseña)
        contraseña = ''.join(contraseña)
        print(f"Contraseña aleatoria para {plataforma} generada con éxito: {contraseña}")
        self.contraseñas.append(Contraseña(plataforma, contraseña))
    


    def menu(self):
        while True:
            print("\n------ MENU ------")
            print("1. Agregar contraseña")
            print("2. Buscar contraseña")
            print("3. Actualizar contraseña")
            print("4. Eliminar contraseña")
            print("5. Mostrar contraseñas")
            print("6. Salir y guardar datos \n")
            opcion = input("Selecciona una opción:")

            if opcion == "1":
                plataforma = input("Ingrese plataforma:\n")

                while True:
                    print("1. Agregar contraseña manual")
                    print("2. Agregar contraseña aleatoria")
                    opcion = input("Seleccione una opcion:\n")
                    
                    if opcion == "1":
                        contraseña = input(f"Ingrese contraseña para {plataforma}:\n")
                        self.agregar_contraseña(plataforma, contraseña)
                        break
                        
                    if opcion ==  "2":
                        try:
                            largo = int(input("Ingrese el largo de la contraseña:\n"))
                            self.generar_contraseña_aleatoria(plataforma, largo)
                            break
                        except ValueError:
                            print("---Debe ingresar un número válido para el largo de la contraseña---")
                    else:
                        print("Opción no válida, intente de nuevo..")

            elif opcion == "2":
                plataforma = input("Ingrese plataforma:\n")
                self.buscar_contraseña(plataforma)
            elif opcion == "3":
                plataforma = input("Ingrese la plataforma que desea buscar:\n")
                nueva_contraseña = input("Ingrese la nueva contraseña:\n") 
                print("\n")                                                #no deberia preguntar la nueva contraseña, primero deberia verificar si existe alguna contraseña para esa plataforma
                self.actualizar_contraseña(plataforma, nueva_contraseña)  #deberia dar la opcion de actualizar a contraseña aleatoria
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
                print("Opción no válida, intente de nuevo..")

gestor = GestorContraseñas()
gestor.menu()