ENGETO Project_3
Project_3 v Python Akademii slouží k vyhledání výsledků parlamentních voleb z roku 2017. Odkaz k nahlédnutí najdete zde.

Instalace knihoven
Knihovny, které jsou v kódu používány jsou uloženy v souboru requirements.txt . Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
$ pip –version				            # overim verzi manazeru
$pip install -r requirements.txt		# nainstalujeme knihovny

Spuštění programu
Spuštění souboru election-scraper.py v rámci příkazového řádku požaduje 2 povinné argumenty	
python election-scraper.py ‘https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203‘ ‘vysledky_brnovenkov.csv‘
Následně se vám stáhnou výsledky jako soubor s příponou .csv 

Ukázka projektu
Výsledky hlasování pro okres Brno-venkov:
1.	argument:	https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
2.	argument:	vysledky_brnovenkov.csv 

Spuštění programu:
python election-scraper.py ‘https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203‘ ‘vysledky_brnovenkov.csv‘

Průběh stahování:
STAHUJI DATA Z VYBRANEHO URL https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
UKLADAM DO SOUBORU vysledky_brnovenkov.csv
UKONCUJI election-scraper

Částečný výstup:
code,location,registered,envelopes,valid,Občanská demokratická strana,
582794,Babice nad Svitavou,925,660,655,109,1,2,43,0,53,31,7,3,10,0,0,93,0,39,129,0,3,69,0,2,1,1,58,1,0
582808,Babice u Rosic,553,353,351,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93,0,1,25,5,4,1,1,49,0,0
581321,Běleč,160,131,130,13,0,0,25,0,8,14,0,1,0,0,0,11,1,1,30,0,0,14,0,0,0,0,12,0,0


