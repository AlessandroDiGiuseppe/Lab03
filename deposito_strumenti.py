from strumento import Strumento
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self._responsabile = responsabile
        self._strumenti = {}  # id_strumento -> Strumento
        self._prestiti = {}  # id_prestito -> Prestito
        self._contatore_prestiti = 0  # ultimo numero di prestito assegnato

        # --- responsabile (getter/setter) ---

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        self._responsabile = nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if not riga:
                    continue
                id_s, tipo, marca, anno, valore = [c.strip() for c in riga.split(",")]
                self._strumenti[id_s] = Strumento(id_s, tipo, marca, int(anno), float(valore))

    def _prossimo_id_strumento(self):
        numeri = [int(id_s[1:]) for id_s in self._strumenti if id_s[1:].isdigit()]
        return f"S{max(numeri, default=0) + 1}"

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        id_s = self._prossimo_id_strumento()
        strumento = Strumento(id_s, tipo, marca, anno_acquisto, valore)
        self._strumenti[id_s] = strumento
        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self._strumenti.values(), key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        if id_strumento not in self._strumenti:
            raise Exception(f"Lo strumento {id_strumento} non è presente nel sistema.")
        for p in self._prestiti.values():
            if p.id_strumento == id_strumento:
                raise Exception(f"Lo strumento {id_strumento} è già in prestito.")

        self._contatore_prestiti += 1
        id_prestito = f"P{self._contatore_prestiti}"
        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self._prestiti[id_prestito] = prestito
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        if id_prestito not in self._prestiti:
            raise Exception(f"Il prestito {id_prestito} non esiste.")
        del self._prestiti[id_prestito]