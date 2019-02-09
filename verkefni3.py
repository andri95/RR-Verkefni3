#Skilaverkefni 3 - Andri Fannar


#Föll fyrir lið 4 í verkefni
def allarMogulegarEinn(stafir, n):

    k = len(stafir)
    allarMogulegarTveir(stafir, "", k, n)


def allarMogulegarTveir(stafir, tmp, k, n):
    listitest = []
    if n == 0:
        print(tmp)
        return listitest

    for x in range(k):
        if len(tmp) > 0:
            if stafir[x] in tmp:
                #print("sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
                continue
            #else:
                #print("ekki sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
        newTmp = tmp + stafir[x]
        listitest.append(tmp)
        allarMogulegarTveir(stafir, newTmp, k, n - 1)

#Föll fyrir lið 5 í verkefni
def allarMogulegarA(stafir, n):

    allarMogulegarB(stafir, [], n)


def allarMogulegarB(stafir, listi, n):
    if n == 0:
        print(listi)
        return

    for x in range(len(stafir)):
        if len(listi) > 0:
            if stafir[x] in listi[x]:
                #print("sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
                continue
            #else:
                #print("ekki sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
        allarMogulegarTveir(stafir, listi, n - 1)


val = ""
while val != "3":
    print("1 - Fall úr lið 4")
    print("2 - Forrit úr lið 5")
    print("3 - Hætta keyrslu")
    val = input("Veldu lið: ")

    if val == "1":
        stafir = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        n = int(input("Hvað á strengurinn að vera langur? "))
        allarMogulegarEinn(stafir, n)

    elif val == "2":

        stafir = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        n = int(input("Hvað eiga strengirnir að innihalda marga stafi? "))
        m = int(input("Hvað viltu að listinn innihaldi marga strengi? "))

        allarMogulegarA(stafir, n)

        print(listi)

    elif val == "3":
        print("Takk fyrir komuna!")

    else:
        print("Rangur innsláttur")

