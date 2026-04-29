from conexion import conexion
from empleado import empleado

class DAOempleado:
    def __init__(self):
        self.__conexion = conexion()

    def registrar(self, e: empleado):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio, salario) VALUES (%s, %s, %s, %s, %s, %s)"
            param = (e.get_nombre(), e.get_direccion(), e.get_telefono(), e.get_email(), e.get_fecha_inicio(), e.get_salario())
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Empleado registrado exitosamente."
        except Exception as ex:
            return f"Error al registrar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def actualizar(self, e: empleado, id_empleado):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "UPDATE empleado SET nombre=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio=%s, salario=%s WHERE idempleado=%s"
            param = (e.get_nombre(), e.get_direccion(), e.get_telefono(), e.get_email(), e.get_fecha_inicio(), e.get_salario(), id_empleado)
            
            cursor.execute(sql, param)
            con.commit()
            # -------------------
            return "Empleado actualizado exitosamente."
        except Exception as ex:
            return f"Error al actualizar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def eliminar(self, id_empleado):
        try:
            self.__conexion.conectar()
            # --- CAMBIO AQUÍ ---
            cursor = self.__conexion.get_cursor()
            con = self.__conexion.get_conexion()
            
            sql = "DELETE FROM empleado WHERE idempleado = %s"
            cursor.execute(sql, (id_empleado,))
            con.commit()
            # -------------------
            return "Empleado eliminado exitosamente."
        except Exception as ex:
            return f"Error al eliminar empleado: {str(ex)}"
        finally:
            self.__conexion.desconectar()

    def lista(self):
        try:
            self.__conexion.conectar() # Agregué los dos guiones bajos 

            cursor = self.__conexion.get_cursor()

            sql = "SELECT * FROM empleado" 

            cursor.execute(sql)
            resultado = cursor.fetchall()

            return resultado # Esto devuelve el diccionario que usaremos en el main.py
        except Exception as ex:
            print(f"Error al listar: {str(ex)}")
            return []
        finally:
            self.__conexion.desconectar()
