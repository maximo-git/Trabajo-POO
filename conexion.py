import pymysql
from credencial import credencial as c

class conexion:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def conectar(self):
        try:
            self.__conexion = pymysql.connect(
                host=c["host"],
                user=c["user"],
                password=c["password"],
                database=c["database"],
                cursorclass=pymysql.cursors.DictCursor
            )
            self.__cursor = self.__conexion.cursor()
            return True
        except Exception as e:
            print(f"Error al conectar: {e}")
            return False

  
    def get_cursor(self):
        return self.__cursor

    def get_conexion(self):
        return self.__conexion
        
    def desconectar(self):
        if self.__conexion is not None:
            self.__conexion.close()
