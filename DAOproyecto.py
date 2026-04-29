from conexion import conexion
from proyecto import proyecto

class DAOproyecto:
    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, p: proyecto):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
            param = (p.get_nombre(), p.get_descripcion(), p.get_fecha_inicio())
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Proyecto registrado exitosamente."
        except Exception as ex:
            return f"Error al registrar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def actualizar(self, p: proyecto, id_proyecto):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "UPDATE proyecto SET nombre=%s, descripcion=%s, fecha_inicio=%s WHERE idproyecto=%s"
            param = (p.get_nombre(), p.get_descripcion(), p.get_fecha_inicio(), id_proyecto)
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Proyecto actualizado exitosamente."
        except Exception as ex:
            return f"Error al actualizar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def eliminar(self, id_proyecto):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "DELETE FROM proyecto WHERE idproyecto = %s"
            cursor.execute(sql, (id_proyecto,))
            con.commit()
            # -------------------
            return "Proyecto eliminado exitosamente."
        except Exception as ex:
            return f"Error al eliminar proyecto: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def lista(self):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            sql = "SELECT * FROM proyecto"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            # -------------------
            return resultado
        except Exception as ex:
            print(f"Error al listar proyectos: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()
