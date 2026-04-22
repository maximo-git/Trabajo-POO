class proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio