#base del menu

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
                self.agregar_contraseña(plataforma, contraseña) #funcion por agregar
            elif opcion == "2":
                plataforma = input("Ingrese plataforma: ")
                self.buscar_contraseña(plataforma) #funcion por agregar
            elif opcion == "3":
                plataforma = input("Ingrese plataforma: ")
                nueva_contraseña = input("Ingrese nueva contraseña: ")
                self.actualizar_contraseña(plataforma, nueva_contraseña) #funcion por agregar
            elif opcion == "4":
                plataforma = input("Ingrese plataforma: ")
                self.eliminar_contraseña(plataforma)#funcion por agregar
            elif opcion == "5":
                self.mostrar_contraseñas() #funcion por agregar
            elif opcion == "6":
                print("Guardando contraseñas y saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")