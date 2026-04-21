import pyjokes

from quiz import run_quiz
from game import dice_challenge
from utils import clear_screen, safe_int_input, print_section, print_progress


def main():
    total_points = 0
    quiz_rounds = 0
    game_rounds = 0

    while True:
        clear_screen()
        print("=== Demo 3M: Quiz & Mini-Game ===")
        print("1) Gioca al quiz")
        print("2) Sfida dei dadi")
        print("3) Raccontami una barzelletta")
        print("4) Statistiche")
        print("0) Esci")
        choice = safe_int_input("Scegli un'opzione: ", 0, 4)

        if choice == 1:
            print_section("Quiz")
            points, correct = run_quiz()
            total_points += points
            quiz_rounds += 1
            print(f"Hai totalizzato {points} punti. Risposte corrette: {correct}.")
            input("Premi Invio per tornare al menu...")

        elif choice == 2:
            print_section("Sfida dei dadi")
            result = dice_challenge()
            game_rounds += 1
            if result > 0:
                print(f"Hai vinto! Hai guadagnato {result} punti.")
            elif result < 0:
                print(f"Hai perso e perso {-result} punti.")
            else:
                print("Pareggio! Nessun punto guadagnato.")
            total_points += result
            input("Premi Invio per tornare al menu...")

        elif choice == 3:
            print_section("Barzelletta")
            joke = pyjokes.get_joke(language='en', category='all')
            print(joke)
            input("Premi Invio per tornare al menu...")

        elif choice == 4:
            print_section("Statistiche")
            print(f"Punti totali: {total_points}")
            print(f"Quiz giocati: {quiz_rounds}")
            print(f"Sfide giocate: {game_rounds}")
            print_progress(total_points, 50)
            input("Premi Invio per tornare al menu...")

        elif choice == 0:
            print("Grazie per aver giocato! Arrivederci.")
            break


if __name__ == '__main__':
    main()
