# Serial Repeater

Serial repeater (SRPT) on ohjelmisto sarjaliikenteen tallentamiseen ja toistoon. Sen
tarkoitus on mahdollistaa sarjaliikenteen tallennus aikariippuvaisesti helposti
toistettavaan muotoon.

## Formaatti

SRPT käyttää SQLite-tietokantaa datan tallennukseen. Datasta tallennetaan
header-tauluun nopeustieto, sekä muut otsikkotason tieto (metadata, kommentit yms.).
Data-tauluun tallennetaan aikaleima tallennuksen alusta, sekä varsinainen vastaanotettu data.

Yhden tietueen (sarakkeen) datan maksimipituus on riippuvainen käytetystä
sarjaportin nopeudesta. Tietueeseen tallennetaan maksimissaan yksi sekunti dataa
(esim. 8-N-1 -konfiguraatiola 9600 bps nopeudella 1200 merkkiä).

header-taulu:
  * id (Integer)
  * speed (Integer)
  * parity (Char(1)), None,Even,Odd
  * stop_bits (Integer)

data-taulu:
  * id (Integer) (rajoittaa maksimitallennuksen 136v joten riittävästi)
  * data (Blob)

## Ohjelmat
* srpt-record.py
    * srpt-record.py -f <filename> -d <serial device> -s <speed> -p <parity> -sb <stop_bits> -t <duration> -z <size>
    * srpt-recordin avulla tallennetaan sarjalaitteelta (Sarjaportilta) annetuilla parametreillä halutun pituinen tallennus tiedostoon.

* srpt-replay.py
  * srpt-replay.py -d <serial device> <filename>
  * srpt-replayn avulla toistetaan tallennettu tiedosto sarjalaitteelle. Oletuksena käytettään tallennusvaiheessa käytettyjä sarjaportin konfigutaatiota.

* srpt-info.py
  * srpt-info näyttää tiedot tallennuksesta (header-tiedot, tallennuksen pituuden ja koon)
