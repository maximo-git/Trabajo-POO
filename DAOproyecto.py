from conexion import conexion
from proyecto import proyecto

class DAOproyecto:
    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, p: proyecto):
        try:
            self.__conexion.conectar()
            sql = "INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
            param = (p.get_nombre(), p.get_descripcion(), p.get_fecha_inicio())
            self.__conexion._conexion__cursor.execute(sql, param)
            self.__conexion._conexion__conexion.commit()
            return "Proyecto registrado exitosamente."
        except Exception as ex:
            return f"Error al registrar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def actualizar(self, p: proyecto, id_proyecto):
        try:
            self.__conexion.conectar()
            sql = "UPDATE proyectos SET nombre=%s, descripcion=%s, fecha_inicio=%s WHERE idproyecto=%s"
            param = (p.get_nombre(), p.get_descripcion(), p.get_fecha_inicio(), id_proyecto)
            self.__conexion._conexion__cursor.execute(sql, param)
            self.__conexion._conexion__conexion.commit()
            return "Proyecto actualizado exitosamente."
        except Exception as ex:
            return f"Error al actualizar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def eliminar(self, id_proyecto):
        try:
            self.__conexion.conectar()
            sql = "DELETE FROM proyectos WHERE idproyecto = %s"
            self.__conexion._conexion__cursor.execute(sql, (id_proyecto,))
            self.__conexion._conexion__conexion.commit()
            return "Proyecto eliminado exitosamente."
        except Exception as ex:
            return f"Error al eliminar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def lista(self):
        try:
            self.__conexion.conectar()
            sql = "SELECT * FROM proyectos"
            self.__conexion._conexion__cursor.execute(sql)
            resultado = self.__conexion._conexion__cursor.fetchall()
            return resultado
        except Exception as ex:
            print(f"Error al listar proyectos: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()