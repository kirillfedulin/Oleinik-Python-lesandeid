from Mooduli_fail import *

print("Lanedamine mitu arvutehet!")
for i in range(5):
    while True:
        try:
            arv1 = float(input("Sisseta esimene arv: "))
            break
        except ValueError:
            print("Plaun sisseta arv!")
    while True:
        try:
            arv2 = float(input("Sisseta teine arv: "))
            break
        except ValueError:
            print("Plaun sisseta arv!")
t=input("Sisseta tehe (+ , - , * , /)")
tulemus=arithmetic(arv1, arv2, t)
print(f"{arv1}{t}{arv2}={tulemus}")