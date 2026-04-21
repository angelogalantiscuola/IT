import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def safe_int_input(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Inserisci un numero valido.")
            continue

        if minimum is not None and value < minimum:
            print(f"Il valore deve essere almeno {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Il valore deve essere al massimo {maximum}.")
            continue
        return value


def print_section(title):
    print('\n' + '=' * 40)
    print(title)
    print('=' * 40)


def print_progress(value, scale=50):
    bar_length = scale
    normalized = max(0, min(value, bar_length))
    bar = '#' * normalized + '-' * (bar_length - normalized)
    print(f"Progressione punti: [{bar}] {normalized}/{bar_length}")
