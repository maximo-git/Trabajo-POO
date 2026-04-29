from conexion import conexion
from departamentos import departamentos

class DAOdepartamento:

    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, d: departamentos):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "INSERT INTO departamentos (nombre, descripcion, personacargo, cantidadpersonas) VALUES (%s, %s, %s, %s)"
            param = (d.get_nombre(), d.get_descripcion(), d.get_personacargo(), d.get_cantidadpersonas())
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Departamento registrado exitosamente."
        except Exception as ex:
            return f"Error: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def actualizar(self, d: departamentos):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "UPDATE departamentos SET nombre=%s, descripcion=%s, personacargo=%s, cantidadpersonas=%s WHERE iddepartamento=%s"
            param = (d.get_nombre(), d.get_descripcion(), d.get_personacargo(), d.get_cantidadpersonas())
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Departamento actualizado exitosamente."
        except Exception as ex:
            return f"Error: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def eliminar(self, nombre):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "DELETE FROM departamentos WHERE nombre = %s"
            cursor.execute(sql, (nombre,))
            con.commit()
            # -------------------
            return "Departamento eliminado exitosamente."
        except Exception as ex:
            return f"Error: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def lista(self):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            sql = "SELECT * FROM departamentos"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            # -------------------
            return resultado
        except Exception as ex:
            print(f"Error al listar: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()
