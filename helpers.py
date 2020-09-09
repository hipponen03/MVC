elemendid = []


# lisame ELEMENDI juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        print("Element {} on juba olemas" .format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})


# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri


# lisame ELEMENDID korraga, aga nii, et tagastame iga kord ühe elemendi
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid


# loeme konkreetse elemendi
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    print(nimetused)
    if nimetus not in nimetused:
        return "Elementi {} ei eksisteeri" .format(nimetus)
    else:
        return elemendid[nimetused.index(nimetus)]


# uuendame konkreetset elementi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("Elementi {} ei saa uuendada, kuna ta ei eksisteeri" .format(nimetus))
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

# loome main funktsiooni
def main():
    # loome katseandmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]

    # testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    # testime üksikute elementide lisamist
    lisa_element("kohupiim", 0.90, 12)
    lisa_element("leib", 0.80, 5)

    # testime elementide lugemist
    print(loe_elemendid())

    # testime elemendi lugemist
    print(loe_element("vein"))

    # testime elemendi uuendamist
    uuenda_element("vein", 10.0, 10)
    print(loe_element("vein"))


# käivitamine
if __name__ == "__main__":
    main()

