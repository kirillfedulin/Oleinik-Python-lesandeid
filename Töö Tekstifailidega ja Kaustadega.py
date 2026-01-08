def kirjuta_falisse(failinimi:str, loend:list):
    reziim = input("Sisseta faili avamise reziim (w - kirjutamine, a - lisamine): ")
    for i in range(5):
        element=input("Sisseta tekst: ")
        loend.append(element)
    with open(failinimi+"txt",reziim,encoding="uft=8") as f:
        for rida in loend:
            f.write(rida + "\n")

def loe_failist(failinimi: str)->list:
    leond = []
    with open(failinimi+".txt", "r", encoding="utf=8") as f:
        for rida in f:
            loend.append(rida.strip())
        return loend



loend=["Rida 1", "Rida 2"]
failinimi=input("Sisesta faili nimi: ")
kirjuta_falisse(failinimi, loend)
sisu = loe_failist(failinimi)
print("Faili sisu: ")
print(sisu)
for rida in sisu:
    print(rida)
