\section{Simple Serial Repeater}

Simple Serial Repeater (SRPT) on ohjelmisto sarjaliikenteen tallentamiseen ja toistoon. Sen tarkoitus on mahdollistaa sarjaliikenteen helppo tallennus ja toisto sekä virtuaalisille, että fyysisille sarjaporteille. SRPT kehitettiin testauksen avuksi, jotta pystyttiin testaamaan tiedonsiirron toimivuus, ilman että testausta tarvitsisi mennä tekemään joka kerralla työn kohteena olevan moton luokse. Tässä tarkoituksessa SRPT toimikin hyvin ja projektin edetessä pantiin merkille muutamia kehitysideoita, joilla testaustyökalua saataisiin vielä monikäyttöisemmäksi.

SRPT on tarkoituksella pidetty suht. yksinkertaisena, mutta tarvittaessa helposti laajennettavana. Ohjelmiston jako useisiin ohjelmiin, sekä käytettävä tiedostomuoto tukevat tätä. Ohjelmisto on pidetty tarkoituksella komentorivipohjaisena, koska graafiselle käyttöliittymälle ei ole nähty tarvetta.

SRPT on ohjelmoitu Python2/3 -ohjelmointikielellä, PySerial-moduulia hyväksikäyttäen. SRPT oli allekirjoittaneella käytössä Linux-ympäristössä, mutta py/pyserialista löytyy myös Windows-paketit, eikä toiminnassa pitäisi olla esteitä muille käyttöjärjestelmille. Python valittiin ohjelmointikieleksi, koska se oli minulle tutuin, se on varsin hyvin käyttöjärjestelmäriippumaton, eikä SRPT vaadi erityistä tehokkuutta käytettävältä kieleltä. 

\subsection{Käytettävä tiedostomuoto}
SRPT käyttää SQLite-tietokantaa datan tallennukseen. Jokaiseen tallennukseen tallennetaan käytetyt sarjaportin asetukset (nopeus, databittien määrä, pariteetti, stop-bittien määrä), sekä lisäksi mahdolliset metatiedot tallenteesta (kommentit, päiväys, tallennuslaite). Sarjadatasta tallennetaan vain vastaanotettua tietoa. 

SQlite valittiin käytettävän tiedostoformaatin pohjalle, koska se on laajasti tuettu, laajat ominaisuudet sisältävä, helposti laajennettava ja hyvällä tehokkuudella oleva tiedostopohjainen SQL-moottori. SQLite:n tarjoamat ominaisuudet (ref:sqlite_appfileformat https://www.sqlite.org/appfileformat.html) tarjoavat luotettavan pohjan tiedon tallentamiseen. SQLite-tietokannat voivat olla kooltaan X tavua (lisäksi huomioitava tiedostojärjestelmän rajoitukset), joten tallenteiden koko ei tuota formaatille ongelmaa.

Vastaanotettu data tallennetaan vastaanottojoukkoina, joiden koon määrittää ajallinen ero edelliseen lähetykseen, sekä joukon maksimipituus (1s ajan tallennusta). Tallenteita ei pakata millään tavoin käytetyssä tiedostomuodossa, joten tiedostokoko on vahvasti riippuvainen lähetetystä datan määrästä (tiedostokoot esimerkiksi: 115200 bps: 843,75 kb/min; 9600 bps: 70,31 kb/min;). Johtuen sarjaväylän (varsinkin RS-232) suhteellisesta hitaudesta, tiedostokoot eivät silti ole kovin suuria nykytietokoneiden mittapuussa.


\subsubsection{SQL-taulut ja tietotyypit}
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

\subsubsection{[SRPT-Ohjelmat]}
Tallennukseen käytetään srpt-record ohjelmaa, joka annetaan parametreiksi tiedostonimi, käytettävä laitetiedosta, sekä nopeus. Tarvittaessa myös muita sarjaväylän asetuksia (bittimäärä, paritetti, stop-bittien määrä, tallennuksen pituus/koko) voidaan vaihtaa. Oletusasetuksina ovat yleisin 8-N-1 (8bittiä, ei pariteettia, 1 stop-bitti), sekä rajoittamaton tallennus.

Toistoon käytetään srpt-play -ohjelmaa, jolle annetaan parametreiksi käyettävä tiedostolaite. Tarvittaessa myös muita sarjaportin asetuksia saa säädettyä, kuten myös toiston aloituskohtaa ja kestoa.

Tallennuksen tietoja voi tarkastella sprt-info -ohjelmalla. Ohjelma näyttää tallennuksen metatiedot, sekä pituuden ja koon.

\subsection{SRPT:n käyttö}
Projektin testausta varten SRPT:llä tallennettiin moton tuottamaa sarjaliikenettä (alkuperäinen, sekä motomit) 5 minuutin pituiset näytteet, jota sitten toistettiin testattaville ympäristöille. Näin saatiin alustavasti testattua tiedonsiirto korvaavalle tietokoneelle.

\subsection{Kehitysideat}

SRPT:n ensimmäisiä versioita käytettäessä tuli ideoituja mahdollisia lisäkehityshankkeita ohjelmistolle:

Tallennukseen voisi lisätä vaihtoehdon tehdä skannauksen eri tiedonsiirtonopeuksilla ja/tai asetuksilla, ja saada täten tietoa tuntemattomien järjestelmien mahdollisista asetuksista. Tämä vaatisi pieniä muutoksia käytetyihin tauluihin, jotta eri asetukset saadaan tallennettua jokaiselle datatietueelle erikseen.

SRPT:n voisi rakentaa myös omaksi laitteekseen, jolla tallennus/toisto onnistuisi helposti. Tälläiselle laitteelle tallennusvaihtoehtoina olisi lisätä laitteeseen näyttö ja ohjaus asetusten valintaan, automaattinen nopeudentunnistus, tai sarjaväylän ohittaminen kokonaan ja sen sijaan näytteistettäisiin liikennettä riittävällä taajuudella, jolloin sarjaväylän asetuksista ei tarvitsisi välittää. Näytteistys vaatii kuitenkin huomattavasti enemmän tallennustilaa kuin pelkän sarjadatan tallennus. Laitteistaminen vaatisikin lisätutkimusta ja suunnittelua.

Tallennetava data voitaisiin myös pakata jo vastaanottovaiheessa esimerkiksi jollain yleisimmistä pakkausmetodeista (DEFLATE, LZ-variantit). Sopivalla pakkausalgoritmillä pakkaaminen ja purkaminen olisivat myös suht. nopeita hitaamallakin tietokoneella, joten pakkaaminen tuskin aiheuttaisi ongelmia tallenteiden käytössä. Tallenteet ovat tosin valmiiksi jo varsin pieniä, joten tiedon pakkaamiselle ei varsinaisesti ole tarvetta.

* erillinen \"yhden/kahden napin\" laite, jolla tallennus/toisto onnistuisi helposti
* Käyttöliittymä (GUI)
* Tallenteen pakkaus vastaanottovaiheessa
* passthrough

