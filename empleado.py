class empleado:
    def __init__(self, nombre, direccion, telefono, email, fecha_inicio, salario):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fecha_inicio = fecha_inicio
        self.__salario = salario

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_salario(self):
        return self.__salario

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_email(self, email):
        self.__email = email

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def set_salario(self, salario):
        self.__salario = salario