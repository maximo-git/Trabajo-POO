import pymysql
from credencial import credencial as c
class conexion:
    def __inst__(self):
        self .__conexion = None
        self .__cursor = None

    def conectar(self):
        self.__connection = pymysql.connect(
        host= c["host"],
        user= c["user"],
        password= c["password"],
        database= c["database"],
        cursorclass=pymysql.cursors.DictCursor
        )
        self.__cursor = self.__conexion.cursor()

    def desconectar(self):
        self.__conexion.close()    
    