import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        strumenti = self._model.get_strumenti()

        self._view.lista_strumenti.controls.clear()

        if strumenti is None:
            self._view.show_alert("Errore nel recupero degli strumenti.")
            return

        if len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento presente nel deposito.")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(
                ft.Text(str(strumento)))

        self._view.update()

    def cerca_strumenti(self, e):
        tipo = self._view.input_tipo_strumento.value.strip()

        self._view.lista_strumenti_ricerca.controls.clear()

        if not tipo:
            self._view.show_alert("Inserisci un tipo di strumento.")
            self._view.update()
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        if strumenti is None:
            self._view.show_alert("Errore durante la ricerca.")
            self._view.update()
            return

        if len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento trovato.")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(str(strumento)))

        self._view.update()