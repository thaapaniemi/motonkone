<!-- 05:Toteutus !-->

# Toteutus

Projektissa päädyttiin käyttämään käyttöjärjestelmänä Linux-distribuutiota Xubuntu 14.04. Alkuperäiset ohjelmistot Motomit PC ja Terman sovitettiin käyttöön Wine-rajapinnan ja Dosbox/Dosemu DOS-emulaattorin avulla. Järjestelmä asennettiin testausta varten vanhaan Fujitsu-Siemensin kannettavaan. Johtuen rankoista olosuhteita, tavallista kannettavaa käytetään vain käyttöjärjestelmän ja ohjelmien testaamiseksi yhdessä Moton kanssa.

## Tarvittavat asennukset
Perusasennuksella asennettavaan Xubuntu-käyttöjärjestelmään tarvitsee lisäksi asentaa seuraavat paketit, että alkuperäiset ohjelmistot saadaan toimimaan:
* Dosbox DOS-emulaattori Termania varten
* Wine -rajapinta Motomit PC:tä varten. MotomitPC tuli päivittää uusimpaan versioon, jotta ohjelmisto toimisi winen alla.


### Xubuntu
Käyttöjärjestelmäksi valittiin Xubuntusta pitkän tuen versio 14.04. Xubuntu asennettiin oletusasetuksilla testikoneeseen. Lisäksi Xubuntu laitettiin kirjautumaan sisään automaattisesti, sekä Dosbox ja MotomitPC laitettiin käynnistymään automaattisesti sisäänkirjautumisen yhteydessä.

Käytetylle USB-sarjaporttiadapterille lisättiin oma udev-sääntö, jonka ansiosta adapterin kaksi sarjaporttia tulevat näkyviin Linuxissa samoilla laitetiedosto (Device file)-nimillä. (ref:udev-sääntö)


###Wine
Wine on Windows-yhteensopivuuskerros Unixin kaltaisiin (mm. Unix/Linux/OS X/Solaris) käyttöjärjestelmiin, joka mahdollistaa Windows-ohjelmien käyttämisen käytetyssä käyttöjärjestelmässä. Vaikka Motomit sisältääkin taustajärjestelmänään Linuxin[ref:Motomit-manuaali], niin käyttöliittymäänä tomivasta MotomitPC -ohjelmasta on vain olemassa Windows-versio.

Jotta sarjaportit saa toimimaan Windowsin käyttämillä COM-porttinimillä Windows-ohjelmien puolella, tulee laitetiedostoista tehdä symboliset linkit ~/.wine/dosdevices/ -hakemistoon halutuilla nimillä (COM1 ja COM2).[ref Wine-manuaali]

###Dosbox
Dosbox on DOS-emulaattori, joka emuloi IBM PC-yhteensopivaa tietokonetta 286/386-prosessorilla, sekä monia kyseisen aikakauden laitteistoja. Dosbox sisältää lisäksi suoratuen sarjaportille, niin se on valittu käytettäväksi DOS-emulaattoriksi.

Koska Dosbox on emulaattori, niin siinä pystyy säätämään suoritusnopeutta, ruudun resoluutiota/kokoa, yms. varsin monipuolisesti. Asetin suoritusnopeuden maksimiin, ruudun koon ikkunamoodissa kokoon 800x600 ilman näppäinlukitusta, sekä poistin ääniemulaation käytöstä. Dosboxissa sarjaportit määritetään samasta asennustiedostosta kuin muutkin asetukset, joten sinne piti lisätä vähintään Termanin käyttämä sarjaportti käyttöön. (asetustiedosto liitteenä)[ref:http://www.dosbox.com/wiki/Dosbox.conf]




<!-- 05:EOF !-->