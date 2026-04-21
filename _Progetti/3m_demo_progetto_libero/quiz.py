import random

QUESTIONS = [
    {
        'question': 'Qual è il tipo di dato usato per testo in Python?',
        'options': ['int', 'str', 'bool', 'list'],
        'answer': 2
    },
    {
        'question': 'Quale istruzione si usa per un ciclo ripetuto?',
        'options': ['if', 'while', 'def', 'import'],
        'answer': 2
    },
    {
        'question': 'Quale simbolo è usato per commentare una riga?',
        'options': ['//', '#', '/*', '<!--'],
        'answer': 2
    },
    {
        'question': 'Qual è il risultato di 5 + 3 * 2 in Python?',
        'options': ['16', '11', '13', '10'],
        'answer': 2
    },
    {
        'question': 'Quale funzione legge un valore da tastiera?',
        'options': ['print()', 'input()', 'len()', 'type()'],
        'answer': 2
    },
]


def run_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    points = 0
    correct = 0

    for index, item in enumerate(questions[:5], start=1):
        print(f"Domanda {index}: {item['question']}")
        for option_index, option in enumerate(item['options'], start=1):
            print(f"  {option_index}) {option}")

        answer = None
        while answer is None:
            try:
                answer = int(input("Risposta (numero): "))
                if answer < 1 or answer > len(item['options']):
                    raise ValueError
            except ValueError:
                answer = None
                print(f"Inserisci un numero valido tra 1 e {len(item['options'])}.")

        if answer == item['answer']:
            print("Corretto! +10 punti")
            points += 10
            correct += 1
        else:
            print(f"Sbagliato. Risposta corretta: {item['options'][item['answer'] - 1]}")
        print()

    return points, correct
