from Mooduli_fail import *

print("Lanedamine mitu arvutehet!")
for i in range(5):
    arv1 = float_kontroll(input("Sisesta esimene arv: "))
    arv2 = float_kontroll(input("Sisesta teine arv: "))

    t=input("Sisseta tehe (+ , - , * , /)")
    tulemus=arithmetic(arv1, arv2, t)
    print(f"{arv1} {t} {arv2} = {tulemus}")