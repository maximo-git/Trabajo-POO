from conexion import conexion

class DAOAsignacionProyecto:
    def __init__(self):
        self.__conexion = conexion()

    def asignar_empleado(self, id_empleado, id_proyecto):
        try:
            self.__conexion.conectar()
            # Asumiendo que la tabla intermedia se llamara 'empleados_proyectos' o si ni cambiar 
            sql = "INSERT INTO empleados_proyectos (idempleado, idproyecto) VALUES (%s, %s)"
            self.__conexion._conexion__cursor.execute(sql, (id_empleado, id_proyecto))
            self.__conexion._conexion__conexion.commit()
            return "Empleado asignado al proyecto exitosamente."
        except Exception as ex:
            return f"Error al asignar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def desasignar_empleado(self, id_empleado, id_proyecto):
        try:
            self.__conexion.conectar()
            sql = "DELETE FROM empleados_proyectos WHERE idempleado = %s AND idproyecto = %s"
            self.__conexion._conexion__cursor.execute(sql, (id_empleado, id_proyecto))
            self.__conexion._conexion__conexion.commit()
            return "Empleado desasignado del proyecto exitosamente."
        except Exception as ex:
            return f"Error al desasignar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def listar_asignaciones(self):
        try:
            self.__conexion.conectar()
            #revisaaaar
            sql = """
                SELECT t.nombre as empleado, p.nombre as proyecto 
                FROM empleados 
                JOIN empleados_proyectos tp ON e.idempleado = ep.idempleado 
                JOIN proyectos p ON tp.idproyecto = p.idproyecto
            """
            self.__conexion._conexion__cursor.execute(sql)
            resultado = self.__conexion._conexion__cursor.fetchall()
            return resultado
        except Exception as ex:
            print(f"Error al listar asignaciones: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()