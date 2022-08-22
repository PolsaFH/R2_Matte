def Lage_Rekke():
    print("\nHa mellomrom mellom tall!")
    Rekke = input("Skriv inn en rekke: ")



    Summer_Rekke(Rekke)


def Summer_Rekke(Rekke):
    print('\nSkriv "alle" for å summere alle')
    ganger = input("Hvor mange ledd skal summeres? ")

    try:
        Rekke = Rekke.split(' ')
    except:
        1+1

    if ganger == "alle":
        ganger = int(len(Rekke))
    else:
        ganger = int(ganger)

    while len(Rekke) < int(ganger):
        ganger = int(input("Du skrev lenger enn det Rekka er. Skriv inn på nytt: a"))

    sum = 0

    for i in range(ganger):
        if "^" in Rekke[i]:
            opphoyd = str(Rekke[i]).split("^")
            sum += int(opphoyd[0]) ** int(opphoyd[1])
        else:
            sum += int(Rekke[i])

    print(f"Summen av tallene er: {sum}")

    fortsette(Rekke)


def fortsette(Rekke):

    print("\n1. Skriv en ny rekke\n2. Regne ut ny n\n3. Avslutte programmet")
    valg = input("Skriv inn et av valgene over: ")

    if valg == "1":
        Lage_Rekke()
    elif valg == "2":
        Summer_Rekke(Rekke)
    else:
        exit()

Lage_Rekke()



