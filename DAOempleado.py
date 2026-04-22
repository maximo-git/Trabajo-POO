from conexion import conexion
from empleado import empleado

class DAOempleado:
    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, e: empleado):
        try:
            self.__conexion.conectar()
            sql = "INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario) VALUES (%s, %s, %s, %s, %s, %s)"
            param = (e.get_nombre(), e.get_direccion(), e.get_telefono(), e.get_email(), e.get_fecha_inicio(), e.get_salario())
            self.__conexion._conexion__cursor.execute(sql, param)
            self.__conexion._conexion__conexion.commit()
            return "Empleado registrado exitosamente."
        except Exception as ex:
            return f"Error al registrar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def actualizar(self, e: empleado, id_empleado):
        try:
            self.__conexion.conectar()
            sql = "UPDATE empleados SET nombre=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio=%s, salario=%s WHERE idempleado=%s"
            param = (e.get_nombre(), e.get_direccion(), e.get_telefono(), e.get_email(), e.get_fecha_inicio(), e.get_salario(), id_empleado)
            self.__conexion._conexion__cursor.execute(sql, param)
            self.__conexion._conexion__conexion.commit()
            return "Empleado actualizado exitosamente."
        except Exception as ex:
            return f"Error al actualizar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def eliminar(self, id_empleado):
        try:
            self.__conexion.conectar()
            sql = "DELETE FROM empleados WHERE idempleado = %s"
            self.__conexion._conexion__cursor.execute(sql, (id_empleado,))
            self.__conexion._conexion__conexion.commit()
            return "Empleado eliminado exitosamente."
        except Exception as ex:
            return f"Error al eliminar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def lista(self):
        try:
            self.__conexion.conectar()
            sql = "SELECT * FROM empleados"
            self.__conexion._conexion__cursor.execute(sql)
            resultado = self.__conexion._conexion__cursor.fetchall()
            return resultado
        except Exception as ex:
            print(f"Error al listar empleados: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()