# Simple Serial Repeater

Simple Serial Repeater (SRPT) on ohjelmisto sarjaliikenteen tallentamiseen ja toistoon. Sen tarkoitus on mahdollistaa sarjaliikenteen helppo tallennus ja toisto sekä virtuaalisille, että fyysisille sarjaporteille. SRPT kehitettiin testauksen avuksi, jotta pystyttiin testaamaan tiedonsiirron toimivuus, ilman että testausta tarvitsisi mennä tekemään joka kerralla työn kohteena olevan moton luokse. Tässä tarkoituksessa SRPT toimikin hyvin ja projektin edetessä pantiin merkille muutamia kehitysideoita, joilla testaustyökalua saataisiin vielä monikäyttöisemmäksi.

SRPT on tarkoituksella pidetty suht. yksinkertaisena, mutta tarvittaessa helposti laajennettavana. Ohjelmiston jako useisiin ohjelmiin, sekä käytettävä tiedostomuoto tukevat tätä. Ohjelmisto on pidetty tarkoituksella komentorivipohjaisena, koska graafiselle käyttöliittymälle ei ole nähty tarvetta.

## Käytettävä tiedostomuoto
SRPT käyttää SQLite-tietokantaa datan tallennukseen. Jokaiseen tallennukseen tallennetaan käytetyt sarjaportin asetukset (nopeus, databittien määrä, pariteetti, stop-bittien määrä), sekä lisäksi mahdolliset metatiedot tallenteesta (kommentit, päiväys, tallennuslaite). Sarjadatasta tallennetaan vain vastaanotettua tietoa. 

Vastaanotettu data tallennetaan vastaanottojoukkoina, joiden koon määrittää ajallinen ero edelliseen lähetykseen, sekä joukon maksimipituus (1s ajan tallennusta).


### SQL-taulut ja tietotyypit
Header-taulu:
  * id (Integer)
  * speed (Integer)
  * parity (Char(1)), None,Even,Odd
  * stop_bits (Integer)
  * meta_comment (Text)
  * meta_timestamp (Datetime)
  * meta_device (Text)

Data-taulu:
  * id (Integer) (rajoittaa maksimitallennuksen 136v joten riittävästi)
  * data (Blob)

### SRPT-Ohjelmat
* Tallennus: srpt-record.py
    * srpt-record.py -f <filename> -d <serial device> -s <speed> -p <parity> -sb <stop_bits> -t <duration> -z <size>
    * srpt-recordin avulla tallennetaan sarjalaitteelta (Sarjaportilta) annetuilla parametreillä halutun pituinen tallennus tiedostoon.

* Toisto: srpt-replay.py
  * srpt-replay.py -d <serial device> <filename>
  * srpt-replayn avulla toistetaan tallennettu tiedosto sarjalaitteelle. Oletuksena käytettään tallennusvaiheessa käytettyjä sarjaportin konfigutaatiota.

* Tiedot: srpt-info.py
  * srpt-info näyttää tiedot tallennuksesta (header-tiedot, tallennuksen pituuden ja koon)

## SRPT:n käyttö
Projektin testausta varten SRPT:llä tallennettiin moton tuottamaa sarjaliikenettä (alkuperäinen, sekä motomit) 5 minuutin pituiset näytteet, jota sitten toistettiin testattaville ympäristöille. Näin saatiin alustavasti testattua tiedonsiirto korvaavalle tietokoneelle.