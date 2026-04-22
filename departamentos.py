class departamentos:
    def __init__(self,nombre,descripcion,personacargo, cantidadpersonas):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__personacargo = personacargo
        self.__cantidadpersonas = cantidadpersonas

    def set_nombre(self,nombre):
        self.__nombre = nombre  
    def get_nombre(self):
        return self.__nombre

    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion  
    def get_descripcion(self):
        return self.__descripcion

    def set_personacargo(self,personacargo):
        self.__personacargo = personacargo 
    def get_personacargo(self):
        return self.__personacargo

    def set_cantidadpersonas(self,cantidadpersonas):
        self.__cantidadpersonas = cantidadpersonas  
    def get_cantidadpersonas(self):
        return self.__cantidadpersonas     
