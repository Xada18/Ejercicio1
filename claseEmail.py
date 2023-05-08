class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDeDominio = ""
    __contraseña = ""

    def __init__(self, cuenta):
        self.__idCuenta = cuenta[0]
        self.__dominio = cuenta[1]
        self.__tipoDeDominio = cuenta[2]
        self.__contraseña = cuenta[3]

    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDeDominio}"
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(correo, contraseña):
        data1 = correo.split("@")
        data2 = data1[1].split(".")

        cuenta = [data1[0], data2[0], data2[1], contraseña]
        return cuenta
