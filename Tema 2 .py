paev = input("Sisesta nädalapäev => ")
if paev == "neljapäev":
    print("täna on minu lemmik programmrimine!")
else:
    print("Ma tahan programerida teha!")

if paev == "laupäev" or paev == "pühapäev":
    print("Hurra")
else:
    print("Tuleb kooli minna")