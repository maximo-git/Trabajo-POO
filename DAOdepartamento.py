from conexion import conexion
from departamentos import departamentos

class DAOdepartamento:

    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, d: departamentos):
        self.__conexion.conectar()
        sql = "INSERT INTO departamento (nombre, descripcion, personacargo, cantidadpersonas) VALUES (%s, %s, %s, %s)"
        param = (d.get_nombre(), d.get_descripcion(), d.get_personacargo(), d.get_cantidadpersonas())
        self.__conexion._conexion__cursor.execute(sql, param)
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def actualizar(self, d: departamentos):
        self.__conexion.conectar()
        sql = "UPDATE departamento SET nombre=%s, descripcion=%s, personacargo=%s, cantidadpersonas=%s WHERE iddepartamento=%s"
        param = (d.get_nombre(), d.get_descripcion(), d.get_personacargo(), d.get_cantidadpersonas())
        self.__conexion._conexion__cursor.execute(sql, param)
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def eliminar(self, nombre):
        self.__conexion.conectar()
        sql = "DELETE FROM departamento WHERE nombre = %s"
        self.__conexion._conexion__cursor.execute(sql, (nombre,))
        self.__conexion._conexion__conexion.commit()
        self.__conexion.desconectar()

    def lista(self):
        self.__conexion.conectar()
        sql = "SELECT * FROM departamento"
        self.__conexion._conexion__cursor.execute(sql)
        resultado = self.__conexion._conexion__cursor.fetchall()
        self.__conexion.desconectar()
        return resultado    



               

