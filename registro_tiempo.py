class RegistroTiempo:
    def __init__(self, id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion):
        self.__id_empleado = id_empleado
        self.__id_proyecto = id_proyecto
        self.__fecha = fecha
        self.__horas_trabajadas = horas_trabajadas
        self.__descripcion = descripcion

    def get_id_empleado(self):
        return self.__id_empleado
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def get_id_proyecto(self):
        return self.__id_proyecto
    def set_id_proyecto(self, id_proyecto):
        self.__id_proyecto = id_proyecto

    def get_fecha(self):
        return self.__fecha
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
    def set_horas_trabajadas(self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas

    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion