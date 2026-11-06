from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn = get_connection()

        if conn is None:
            return None

        cursor = None

        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM strumento"
            cursor.execute(query)

            risultati = cursor.fetchall()

            strumenti = []

            for riga in risultati:
                strumento = Strumento(
                    riga["codice"],
                    riga["tipo"],
                    riga["marca"],
                    riga["anno_acquisto"],
                    riga["valore"],
                    riga["disponibile"]
                )
                strumenti.append(strumento)

            return strumenti

        except Exception as e:
            print(f"Errore durante il recupero degli strumenti: {e}")
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conn.close()

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        conn = get_connection()

        if conn is None:
            return None

        cursor = None

        try:
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM strumento WHERE tipo = %s"
            cursor.execute(query, (tipo,))

            risultati = cursor.fetchall()

            strumenti = []

            for riga in risultati:
                strumento = Strumento(
                    riga["codice"],
                    riga["tipo"],
                    riga["marca"],
                    riga["anno_acquisto"],
                    riga["valore"],
                    riga["disponibile"]
                )

                strumenti.append(strumento)

            return strumenti

        except Exception as e:
            print(f"Errore durante la ricerca degli strumenti: {e}")
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
