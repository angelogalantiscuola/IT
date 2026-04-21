import random
import time


def dice_challenge():
    player_score = 0
    computer_score = 0

    for round_number in range(1, 4):
        print(f"Turno {round_number}")
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        print(f"Tu: {player_roll} - Computer: {computer_roll}")

        if player_roll > computer_roll:
            player_score += 1
            print("Hai vinto questo turno!")
        elif player_roll < computer_roll:
            computer_score += 1
            print("Hai perso questo turno.")
        else:
            print("Pareggio in questo turno.")

        time.sleep(0.5)
        print()

    if player_score > computer_score:
        return 20
    elif player_score < computer_score:
        return -10
    return 0
