#190.5
def kerekito(a):
    szeletelo = str(a).split(".")
    if len(szeletelo[1]) == 1:                                          #1 tizedes jegy
        if int(szeletelo[1]) <= 4:
            szeletelo = int(szeletelo[0])
            masodik = 0
        elif int(szeletelo[1]) >= 5:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 2:                                     #2 tizedes jegy
        if int(szeletelo[1]) >= 51:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 3:                                  #3 tizedes jegy
        if int(szeletelo[1]) >= 501:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 4:                                  #4 tizedes jegy
        if int(szeletelo[1]) >= 5001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 5:                                  #5 tizedes jegy
        if int(szeletelo[1]) >= 50001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 6:                                  #6 tizedes jegy
        if int(szeletelo[1]) >= 500001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 7:                                  #7 tizedes jegy
        if int(szeletelo[1]) >= 5000001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 8:                                  #8 tizedes jegy
        if int(szeletelo[1]) >= 50000001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 9:                                  #9 tizedes jegy
        if int(szeletelo[1]) >= 500000001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    elif len(szeletelo[1]) == 10:                                  #10 tizedes jegy -vége-
        if int(szeletelo[1]) >= 5000000001:
            szeletelo = int(szeletelo[0]) + 1
            masodik = 0
        else:
            szeletelo = int(szeletelo[0])
            masodik = 0
        finomitas = str(szeletelo) + "." + str(masodik)
    return float(finomitas)
        
meghivo = kerekito(190.7878778)