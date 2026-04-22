from conexion import conexion

class DAOAsignacion:

    def __init__(self):
        self.__conexion = conexion()

    def asignar(self, nombre_empleado, nombre_departamento):
        self.__conexion.conectar()
        sql = "UPDATE empleados SET iddepartamento = (SELECT iddepartamento FROM departamentos WHERE nombre = %s) WHERE nombre = %s"
        self.__conexion._conexion__cursor.execute(sql, (nombre_departamento, nombre_empleado))
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def eliminar(self, nombre_empleado):
        self.__conexion.conectar()
        sql = "UPDATE empleados SET iddepartamento = NULL WHERE nombre = %s"
        self.__conexion._conexion__cursor.execute(sql, (nombre_empleado,))
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def lista(self):
        self.__conexion.conectar()
        #revisar
        sql = "SELECT t.nombre, d.nombre FROM empleados t LEFT JOIN departamentos d ON t.iddepartamento = d.iddepartamento"
        self.__conexion._conexion__cursor.execute(sql)
        resultado = self.__conexion._conexion__cursor.fetchall()
        self.__conexion.desconectar()
        return resultado