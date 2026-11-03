# Espressioni Booleane: costruire le condizioni

Una **espressione booleana** è un'espressione che, una volta valutata, produce uno dei due valori booleani di Python: `True` (vero) oppure `False` (falso). Le condizioni di `if` e `while` sono espressioni booleane.

```python
temperatura: float = 28.5
fa_caldo: bool = temperatura > 25

print(fa_caldo)  # True
```

## 1. Confrontare i valori

Gli operatori di confronto mettono a confronto due valori e restituiscono `True` oppure `False`:

| Operatore | Significato | Esempio |
|---|---|---|
| `==` | uguale a | `eta == 18` |
| `!=` | diverso da | `colore != "rosso"` |
| `<` | minore di | `temperatura < 30` |
| `<=` | minore o uguale a | `punteggio <= 100` |
| `>` | maggiore di | `prezzo > 10` |
| `>=` | maggiore o uguale a | `eta >= 18` |

Non confondere `=` e `==`: `=` assegna un valore a una variabile, mentre `==` controlla se due valori sono uguali.

```python
eta: int = 18  # Assegna 18 a eta
print(eta == 18)  # Controlla l'uguaglianza: True
print(eta != 18)  # Controlla la differenza: False
```

I confronti si possono usare direttamente come condizioni:

```python
eta: int = 16

if eta >= 18:
    print("Puoi accedere")
else:
    print("Accesso non consentito")
```

## 2. Combinare le condizioni

Gli operatori logici permettono di combinare o modificare espressioni booleane:

| Operatore | Significato | Quando il risultato è `True` |
|---|---|---|
| `and` | e | Quando entrambe le condizioni sono vere |
| `or` | oppure | Quando almeno una delle condizioni è vera |
| `not` | non | Quando la condizione viene invertita |

### `and`: entrambe le condizioni devono essere vere

Per accedere a un contenuto riservato, una persona deve avere almeno 18 anni **e** avere un'autorizzazione:

```python
eta: int = 20
ha_autorizzazione: bool = True

puo_accedere: bool = eta >= 18 and ha_autorizzazione
print(puo_accedere)  # True
```

Se anche una sola delle due condizioni è falsa, il risultato di `and` è `False`.

### `or`: basta una delle condizioni vere

Un museo applica uno sconto a chi ha meno di 12 anni **oppure** ha almeno 65 anni:

```python
eta: int = 70

ha_diritto_allo_sconto: bool = eta < 12 or eta >= 65
print(ha_diritto_allo_sconto)  # True
```

Con `or`, il risultato è `False` solo quando entrambe le condizioni sono false.

### `not`: invertire una condizione

L'operatore `not` trasforma `True` in `False` e viceversa:

```python
piove: bool = False
non_piove: bool = not piove

print(non_piove)  # True
```

## 3. Scrivere condizioni leggibili

Le condizioni possono essere raggruppate con le parentesi, proprio come nelle espressioni matematiche. Le parentesi rendono chiaro quali controlli vanno considerati insieme:

```python
eta: int = 16
ha_accompagnatore: bool = True

puo_entrare: bool = (eta >= 18) or (eta >= 14 and ha_accompagnatore)
```

In questo esempio si può entrare se si hanno almeno 18 anni, **oppure** se si hanno almeno 14 anni **e** si è accompagnati. Le parentesi aiutano a leggere l'alternativa senza ambiguità.

Quando una condizione diventa difficile da leggere, assegnale un nome descrittivo o suddividila:

```python
eta_sufficiente: bool = eta >= 14
accompagnamento_valido: bool = ha_accompagnatore
puo_entrare: bool = eta >= 18 or (eta_sufficiente and accompagnamento_valido)
```

> **Attenzione:** in Python i valori booleani si scrivono `True` e `False`, con la prima lettera maiuscola. `true` e `false` minuscoli non sono i valori booleani di Python.

## 4. Prova a ragionare sulle condizioni

Senza eseguire il codice, stabilisci se ciascuna espressione vale `True` o `False`:

```python
numero: int = 12

numero > 10 and numero < 20
numero == 12 or numero == 0
not (numero < 10)
```

Poi verifica le risposte assegnando le espressioni a variabili booleane e stampandole. Queste stesse espressioni possono essere usate come condizioni in `if` e `while`.
