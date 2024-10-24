"""
najst frekvenciu vyskytov pismeniek v tej ebook
"""

from string import ascii_lowercase as pismenka

# tabulka = {i: 0 for i in pismenka}

with open("pg215.txt", "r") as file:
    subor = file.read().lower()

    # for i in subor:
    #     if i in pismenka:
    #         tabulka[i] += 1

    # t = [tabulka[i] for i in subor if i in pismenka]
    tabulka = {pismenko: subor.count(pismenko) for pismenko in pismenka}

    '''
    zoraduje dict
    key = na zaklade coho za bude zoradovat - my chceme podla momentalneho itemu[1] = druhy element = pocet daneho pismenka
    '''
    sorted_tabulka = sorted(tabulka.items(), key=lambda i: i[1], reverse=True)

    (print(i) for i in sorted_tabulka)


# print(f'tabulka vyskytu pismenok: {i for i in tabulka}')

# za mna velmi neefektivne riesenie vytvarania tabulky ale tak whatever
