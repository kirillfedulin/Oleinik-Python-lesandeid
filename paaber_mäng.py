import random

valikud = ["kivi", "käärid", "paber"]

score = 0
cpu_score = 0

player_results = []
cpu_results = []
rounds = []

while True:
    print("Vali käik:")
    print("1 - kivi")
    print("2 - käärid")
    print("3 - paber")
    print("0 - stop")

    user_input = input("\nSinu valik: ")

    try:
        choice_num = int(user_input)

        if choice_num == 0:
            break

        if choice_num < 1 or choice_num > 3:
            raise ValueError  

        player = valikud[choice_num - 1]

    except ValueError:
        print("\nViga! Palun sisesta number 1 kuni 3 või 0 lõpetamiseks.\n")
        continue

    robot = random.choice(valikud)
    print("\nCPU valik:", robot)

    if player == robot:
        print("Viik!\n")
        winner = "Viik"
    elif (player == "paber" and robot == "kivi") or \
         (player == "kivi" and robot == "käärid") or \
         (player == "käärid" and robot == "paber"):
        print("Sa võitsid!\n")
        score += 1
        winner = "Mängija"
    else:
        print("CPU võitis!\n")
        cpu_score += 1
        winner = "CPU"

    rounds.append((player, robot, winner))
    player_results.append(score)
    cpu_results.append(cpu_score)

print("\n--- Mängu tulemused ---\n")
vooru_number = 1

for player_choice, cpu_choice, winner in rounds:
    print(f"Voor {vooru_number}: Mängija valik: {player_choice}, CPU valik: {cpu_choice}, Võitja: {winner}")
    vooru_number += 1
