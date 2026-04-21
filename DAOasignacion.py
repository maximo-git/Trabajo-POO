from conexion import conexion

class DAOAsignacion:

    def __init__(self):
        self.__conexion = conexion()

    def asignar(self, nombre_trabajador, nombre_departamento):
        self.__conexion.conectar()
        sql = "UPDATE trabajadores SET iddepartamento = (SELECT iddepartamento FROM departamentos WHERE nombre = %s) WHERE nombre = %s"
        self.__conexion._conexion__cursor.execute(sql, (nombre_departamento, nombre_trabajador))
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def eliminar(self, nombre_trabajador):
        self.__conexion.conectar()
        sql = "UPDATE trabajadores SET iddepartamento = NULL WHERE nombre = %s"
        self.__conexion._conexion__cursor.execute(sql, (nombre_trabajador,))
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def lista(self):
        self.__conexion.conectar()
        sql = "SELECT t.nombre, d.nombre FROM trabajadores t LEFT JOIN departamentos d ON t.iddepartamento = d.iddepartamento"
        self.__conexion._conexion__cursor.execute(sql)
        resultado = self.__conexion._conexion__cursor.fetchall()
        self.__conexion.desconectar()
        return resultado