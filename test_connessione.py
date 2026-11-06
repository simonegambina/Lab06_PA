from model.model import DepositoStrumenti

deposito = DepositoStrumenti(
    "Deposito Strumenti Musicali",
    "Alessandro Visconti"
)

strumenti = deposito.cerca_strumenti_per_tipo("Chitarra")

if strumenti is not None:
    print(f"Strumenti trovati: {len(strumenti)}")

    for strumento in strumenti:
        print(strumento)
else:
    print("Errore durante la ricerca.")