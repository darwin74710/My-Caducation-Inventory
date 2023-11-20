class Lista:
    def __init__(self, nombre,
                 idPosicion,
                 identificadorFiltro,
                 descripcion,
                 numeroDia,
                 numeroMes,
                 numeroAno,
                 numeroCantidad,
                 espacio):
        self.nombre = nombre
        self.idPosicion = idPosicion
        self.identificadorFiltro = identificadorFiltro
        self.descripcion = descripcion
        self.numeroDia = numeroDia
        self.numeroMes = numeroMes
        self.numeroAno = numeroAno
        self.numeroCantidad = numeroCantidad
        self.espacio = espacio

    # Al imprimir el objeto de tipo Lista se dira solo el nombre.
    def __str__(self):
        return f"{self.nombre}"