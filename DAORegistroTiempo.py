class DAORegistroTiempo:
    def __init__(self):
        self.__registros = []

    def registrar(self, registro, lista_empleados, lista_proyectos):
        try:
            empleado_existe = any(emp.get_nombre() == registro.get_id_empleado() for emp in lista_empleados)
            proyecto_existe = any(proy.get_nombre() == registro.get_id_proyecto() for proy in lista_proyectos)

            if not empleado_existe:
                return "Error: El empleado no existe."
            if not proyecto_existe:
                return "Error: El proyecto no existe."
            
            self.__registros.append(registro)
            return "Registro de tiempo guardado exitosamente."

        except Exception as e:
            return f"Error inesperado al registrar: {str(e)}"

    def listar(self):
        return self.__registros

    def eliminar(self, id_empleado, fecha):
        for reg in self.__registros:
            if reg.get_id_empleado() == id_empleado and reg.get_fecha() == fecha:
                self.__registros.remove(reg)
                return "Registro eliminado."
        return "No se encontró el registro para eliminar."