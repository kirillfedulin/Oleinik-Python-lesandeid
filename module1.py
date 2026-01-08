def kirjuta_falisse(failinimi:str, loend:list):
    reziim = input("Sisseta faili avamise reziim (w - kirjutamine, a - lisamine): ")
    n=len(loend)
    if n!=0:
        for e in loend:
            print(e)
    for i in range(10):
        element=input("Sisseta tekst: ")
        loend.append(f"\n {element}")
    with open(failinimi+"txt",reziim,encoding="uft=8") as f:
        f.writelines(loend)



loend=["Rida 1", "Rida 2"]
failinimi=input("Sisesta faili nimi: ")
kirjuta_falisse(failinimi, loend)