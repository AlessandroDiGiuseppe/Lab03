class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return (f"{self.id} - strumento {self.id_strumento} prestato a "
                f"{self.cognome_allievo} in data {self.data}")

    def __repr__(self):
        return (f"Prestito({self.id!r}, {self.data!r}, "
                f"{self.id_strumento!r}, {self.cognome_allievo!r})")