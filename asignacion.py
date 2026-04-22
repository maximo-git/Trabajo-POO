class Asignacion:

    def __init__(self, nombre_empleado, nombre_departamento):
        self.__nombre_empleado = nombre_empleado
        self.__nombre_departamento = nombre_departamento

    def get_trabajador(self):
        return self.__nombre_empleado

    def get_departamento(self):
        return self.__nombre_departamento