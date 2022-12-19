# %%
# lanciare_una_moneta_fino_a_che_non_esce_testa_2_volte_di_fila.py

# codifica
# 0 = testa
# 1 = croce
import random

primo_lancio = True

while (True):
    print(f'')

    esito_lancio = random.randint(0,1)

    # lancia la moneta
    if esito_lancio == 0:
        print(f'testa\t lancio corrente')
    else:
        print(f'croce\t lancio corrente')

    # al primo lancio non effettuare nessun controllo
    if primo_lancio:
        primo_lancio = False
    # per tutti i lanci tranne il primo
    else:
        # stampa l'esito del lancio precedente
        if esito_lancio_precedente == 0:
            print(f'testa\t lancio precedente')
        else:
            print(f'croce\t lancio precedente')

        # controlla se la condizione e' verificata
        if esito_lancio == 0 and esito_lancio_precedente == 0:
            print(f'\nuscita testa 2 volte di fila\n\n')
            break

    # salva il valore del lancio corrente in lancio precedente per l'iterazione successiva
    esito_lancio_precedente = esito_lancio


