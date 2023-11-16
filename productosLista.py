class Lista:
    def __init__(self, idPosicion,
                 identificadorFiltro,
                 nombre,
                 descripcion,
                 numeroDia,
                 numeroMes,
                 numeroAno,
                 numeroCantidad):
        self.idPosicion = idPosicion
        self.identificadorFiltro = identificadorFiltro
        self.nombre = nombre
        self.descripcion = descripcion
        self.numeroDia = numeroDia
        self.numeroMes = numeroMes
        self.numeroAno = numeroAno
        self.numeroCantidad = numeroCantidad

    # Al imprimir el objeto de tipo Lista se dira solo el nombre.
    def __str__(self):
        return f"Nombre: {self.nombre} ID: {self.idPosicion}"