class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return (f"{self.id} - {self.tipo} {self.marca} "
                f"(acquistato nel {self.anno_acquisto}, valore: {self.valore:.2f} euro)")

    def __repr__(self):
        return (f"Strumento({self.id!r}, {self.tipo!r}, {self.marca!r}, "
                f"{self.anno_acquisto!r}, {self.valore!r})")