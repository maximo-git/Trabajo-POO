class Asignacion:

    def __init__(self, nombre_trabajador, nombre_departamento):
        self.__nombre_trabajador = nombre_trabajador
        self.__nombre_departamento = nombre_departamento

    def get_trabajador(self):
        return self.__nombre_trabajador

    def get_departamento(self):
        return self.__nombre_departamento