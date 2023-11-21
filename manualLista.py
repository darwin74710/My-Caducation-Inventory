class Lista:
    def __init__(self, idPosicion,
                 identidicadorimagen,
                 idtexto,
                 titulo):
        self.idPosicion = idPosicion
        self.identidicadorimagen = identidicadorimagen
        self.idtexto = idtexto
        self.titulo = titulo



    # Al imprimir el objeto de tipo Lista se dira solo el nombre.
    def __str__(self):
        return f"Nombre: {self.titulo} ID: {self.idPosicion}"