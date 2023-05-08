from claseEmail import Email

if __name__ == '__main__':
    
    nombre = input("Ingresar nombre: ")
    mail = input("Ingresar correo: ")
    contraseña = input("Ingresar conraseña: ")
    cuenta = Email.crearCuenta(mail, contraseña)
    UnEmail = Email(cuenta)
    print(f"Estimado {nombre}, te enviaremos tus mensajes a la direccion {UnEmail.retornaEmail()}")
    
    print("Modificar contraeña:")
    ban = False
    while ban == False:
        actual = input("Ingrese contraseña actual: ")
        if actual == UnEmail.__contraseña:
            nueva = input("Ingrese nueva contraseña: ")
            UnEmail.__contraseña = nueva
            ban = True
        else:
            print("Contraseña incorrecta")
    
    nmail = input("Ingresar correo: ")
    ncontraseña = input("Ingresar conraseña: ")
    nuevoEmail = Email.crearCuenta(nmail, ncontraseña)
    

        
    

