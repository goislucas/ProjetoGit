class Professor:
    def __init__(self, nome, matriculaSIAPE, cargaHoraria):
        self.__nome = nome
        self.__matriculaSIAPE = matriculaSIAPE
        self.__cargaHoraria = cargaHoraria
    
    def getNome(self):
        return self.__nome
    def getMatriculaSIAPE(self):
        return self.__matriculaSIAPE
    def getCargaHoraria(self):
        return self.__cargaHoraria
    
    def setNome(self, nome):
        self.__nome = nome
    def setMatriculaSIAPE(self, matriculaSIAPE):
        self.__matriculaSIAPE = matriculaSIAPE
    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def maisHoras (self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
    def menosHoras (self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
    
