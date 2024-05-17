"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Anežka Kinclová

email: kanciobora@centrum.cz

discord: asmile0478
"""

import csv
import requests
from bs4 import BeautifulSoup
import sys

def main():
    # Kontrola správného počtu argumentů
    if len(sys.argv) != 3:
        print("Nesprávný počet argumentů.")
        print("Použití: python election-scraper.py <odkaz> <výstupní_soubor>")
        return

    # Získání odkazu a názvu výstupního souboru z argumentů
    odkaz = sys.argv[1]
    vystupni_soubor = sys.argv[2]

    print("STAHUJI DATA Z VYBRANEHO URL", odkaz)

    # Načtení HTML obsahu stránky
    response = requests.get(odkaz)
    html = response.text

    # Vytvoření objektu BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Najít všechny tabulky se třídou "table"
    tables = soup.find_all('table', class_='table')

    # Inicializace seznamu pro ukládání výsledků
    results = []

    # Seznam pro ukládání názvů stran
    parties = []

    # Procházení jednotlivých řádků tabulky
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            kod_obce = None
            nazev_obce = None

            # Najít buňky v řádku s kod_obce
            kod_cell = row.find('td', class_='cislo')
            if kod_cell:
                a_tag = kod_cell.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    kod_obce = a_tag.text

            # Najít buňky v řádku s názvem obce
            nazev_cell = row.find('td', class_='overflow_name')
            if nazev_cell:
                nazev_obce = nazev_cell.text.strip()

            # Pokud jsme našli oba kod_obce a nazev_obce, přidáme je do výsledků
            if kod_obce and nazev_obce:
                results.append([kod_obce, nazev_obce])  # Použití seznamu místo tuple

            # Získání čísla obce a odkazu na detail výsledků
            if kod_cell:
                cell = kod_cell.find('a')
                if cell and 'href' in cell.attrs:
                    detail_url = "https://volby.cz/pls/ps2017nss/" + cell.get('href')

                    # Načtení HTML obsahu stránky s detailními výsledky pro danou obec
                    response_detail = requests.get(detail_url)
                    html_detail = response_detail.text
                    soup_detail = BeautifulSoup(html_detail, 'html.parser')

                    # Získání informací o voličích v seznamu
                    volici_v_seznamu = soup_detail.find('td', class_='cislo', headers='sa2').text.strip()
                    results[-1].append(volici_v_seznamu)

                    # Získání informací o odevzdaných obálkách
                    odevzdane_obalky = soup_detail.find('td', class_='cislo', headers='sa5').text.strip()
                    results[-1].append(odevzdane_obalky)

                    # Získání informací o platných hlasech
                    platne_hlasy = soup_detail.find('td', class_='cislo', headers='sa6').text.strip()
                    results[-1].append(platne_hlasy)

                    # Najdeme všechny tabulky na detailnější stránce
                    detail_tables = soup_detail.find_all('table', class_='table')

                    # Procházíme všechny tabulky na detailnější stránce
                    for detail_table in detail_tables:
                        # Najdeme všechny řádky v tabulce
                        rows = detail_table.find_all('tr')
                        for row in rows:
                            # Pokud chceme najít buňky s názvy stran, můžeme například kontrolovat třídu nebo další charakteristiky
                            party_cells = row.find_all('td', class_='overflow_name')  # Všechny buňky s názvy stran
                            vote_cells1 = row.find_all('td', class_='cislo', headers='t1sa2 t1sb3')  # Všechny buňky s počtem hlasů
                            vote_cells2 = row.find_all('td', class_='cislo', headers='t2sa2 t2sb3')  # Všechny buňky s počtem hlasů

                            vote_cells = vote_cells1 + vote_cells2

                            # Procházíme názvy stran a jejich hlasů
                            for party_cell, vote_cell in zip(party_cells, vote_cells):
                                party_name = party_cell.text.strip()
                                if party_name not in parties:
                                    parties.append(party_name)
                                party_vote = vote_cell.text.strip()
                                results[-1].append(party_vote)

    # Seznam záhlaví souboru CSV
    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + parties

    # Uložení výsledků do CSV souboru
    with open(vystupni_soubor, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Přidání řádku pro Excel
        file.write('sep=,\n')

        # Zápis hlavičky tabulky do CSV souboru
        writer.writerow(header)

        # Zápis volebních výsledků do CSV souboru
        for result in results:
            writer.writerow(result)  # Zde jsou zapsány výsledky do CSV souboru

    print("UKLADAM DO SOUBORU", vystupni_soubor)
    print("UKONCUJI election-scraper")

if __name__ == "__main__":
    main()

