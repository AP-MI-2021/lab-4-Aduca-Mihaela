def print_menu():
    print ("1. Citirea unei liste de numere intregi.")
    print ("2. Afisarea tuturor numerelor negative nenule din lista.")
    print ("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print ("4. Afișarea tuturor numerelor din listă care sunt superprime.")
    print ("5. Afișarea listei obținute dupa inlocuirile cerute.")
    print ("6. Iesire.")


def citire_lista():
    """
    :return: lista citita de utilizator
    """
    lista = []
    givenString = input("Dati nr., separate prin virgule: ")
    numAsString = givenString.split(",")
    for x in numAsString:
        lista.append(int(x))
    return lista


def negativ_nenule(l):
    """
    Afiseaza totalitatea nr negative nenule din lista.
    :param l: lista de numere intregi.
    :return: numerele negative nenule.
    """
    rezultat = []
    for x in l:
        if x < 0:
            rezultat.append(x)
    return rezultat


def test_negativ_nenule():
    assert negativ_nenule([12, 4, -1, 0, -5]) == [-1, -5]
    assert negativ_nenule([]) == []
    assert negativ_nenule([-2, -3, 4, 5, 6]) == [-2, -3]


def cel_mai_mic(l, nrdat):
    """
    Afiseaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param l: lista de numere intregi.
    :param nrdat: nr intreg
    :return: Cel mai mic numar care are ultima cifra egala cu o cifra citita.
    """
    min = float('inf')
    for x in l:
        if x % 10 == nrdat:
            if x < min or min == float('inf'):
                min = x
    return min

def test_cel_mai_mic():
    assert cel_mai_mic([12, 16, 22, 32, 5], 2) == 12
    assert cel_mai_mic([13, 3, 24, 64, 784], 4) == 24


def is_prime(x):
    """
    Determina daca un numar este prim.
    :param x: nr intreg
    :return: True daca numarul este prim sau False in caz contrar.
    """
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
    return True

def test_is_prime():
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(2) is True

def supraprim(l):
    """
    Afiseaza toate numerele din listă care sunt superprime.
    :param l: lista de numere intregi.
    :return: numerele din lista care sunt supraprime.
    """
    rez = []
    for x in l:
        while x > 0:
            rez.append(x)
            if is_prime(x):
                x = x % 10
            else:
                x = -1
        if x == 0:
            print(rez[x])


def test_supraprim():
    assert supraprim([239, 173, 235]) == 239, 235
    assert supraprim([1, 215, 325]) == 325


def cmmdc(m, n):
    """
    Calculeaza CMMDC a doua numere.
    :param m: nr intreg.
    :param n: nr. intreg.
    :return: CMMDC
    """
    m = int(input("m="))
    n = int(input("n="))

    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m


def lista_noua(l):
    """
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor.
    :param l: lista de numere intregi
    :return: o lista noua, in care nr pozitive si nenule au fost inlocuite cu CMMDC ul lor.
    """
    ln = []
    lnou = []
    for x in l:
        if x > 0:
            ln.append(x)
    #for i in range(ln):
        #for j in  range(i,ln):
            lnou.append(cmmdc(i,j))


def main():
    test_negativ_nenule()
    test_cel_mai_mic()

    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        if optiune == "2":
            print(negativ_nenule(l))
        if optiune == "3":
            nrdat = input("Introduceti valoarea: ")
            print(cel_mai_mic(l,nrdat))
        if optiune == "4":
            print(supraprim(l))
        if optiune == "5":
            print(lista_noua(l))
        elif optiune == "6":
            break
        else:
            print ("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()