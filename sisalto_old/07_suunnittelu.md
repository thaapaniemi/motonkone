# Suunnittelu

## Ohjelmiston toteutusvaihtoehdot
Tarkoituksena olisi löytää projektille sopiva vaihtoehto, missä alkuperäiset ohjelmistot saataisiin toimimaan käyttäjäystävällisesti ja vakaasti uuden laitteiston kanssa.

### Natiivi ympäristö
Vaihtoehdossa tietokoneeseen asennettaan uusin käyttöjärjestelmä, mitä käytössä oleva laitteisto ja ohjelmat tukevat. Vaihtoehto on haasteellinen, koska ohjelmistot ovat vanhoja ja laitteisto uutta. Uusien laitteiden tuki vanhoilla käyttöjärjestelmillä on puutteellinen tai puuttuva.

## Ohjelmistojen rajapintojen yhteensopivuuskerros
Vaihtoehdossa käytetään käyttöjärjestelmän ja ohjelman välissä sopivia rajapintakerroksia, jolloin saadaan käyttöjärjestelmän kanssa yhteensopimattomat ohjelmat toimimaan keskenään. Vaihtoehto vaatii yhteensopivan laitteistoarkkitehtuurin alkuperäisen järjestelmän kanssa. Nykyiset Windows-versiot (Windows XP+) sisältävät jo valmiiksi yhteensopivuustilan, joka mahdollistaa vanhempien ohjelmien käyttämisen uudemmissa käyttöjärjestelmissä. Linuxissa Wine-rajapintatoteutus mahdollistaa kaikenikäisten Windows-sovellusten ajamisen Linuxissa.

## Virtualisointi
Vaihtoehdossa alkuperäisiä ohjelmistoja+käyttöjärjestelmää ajetaan virtuaalikoneessa toisen käyttöjärjestelmän päällä. Näin saavutetaan varmin yhteensopivuus ohjelmistotasolla. Oheislaitteiden siirtämisessä virtualisoidun koneen käyttöön on rajoituksia, jotka pitää huomioida virtualisointiohjelmistoja valittaessa. Vaihtoehto kuluttaa muistia enemmän ja on hieman hitaampi kuin natiivi toteutus, hyötysuhteen ollessa ~90% natiivista [virtnat_anadtech].

[virtnat_anadtech](http://www.anandtech.com/show/2770/10)

## Järjestelmäemulointi
Vaihtoehdossa alkuperäisiä ohjelmistoja+käyttöjärjestelmä ajetaan emulaattorissa toisen järjestelmän päällä. Emuloimalla saavutetaan laitteistoarkkitehtuuririippumattomuus isäntäkoneen ja emuloitavan järjestelmän välillä. Emuloinnin haittapuolena on hitaus. Nyrkkisääntönä on 20% hyötysuhde [tinycc], parhaat emulaattorit pääsevät n. 40% hyötysuhteeseen [40pperf]

[40pperf](http://www.embedded.com/electronics-news/4397737/X86-emulation-coming-to-ARM-processors)
[rpi_emu](http://www.raspberrypi.org/forums/viewtopic.php?f=56&t=13161)
[rpi_emu2](http://rpix86.patrickaalto.com/index.html)
[pearpc](http://pearpc.sourceforge.net/about.html)

## Ohjelmistojen emulointi
Vaihtoehdossa emuloidaan vain ohjelmat koko pc:n sijasta. Tämä onnistuu tietyillä ohjelmilla tiettyjen ohjelmistoarkkitehtuurien välillä [qemu_use],[tinycc]. Vaihtoehdolla voi ajaa x86-ohjelmia ARM-prosessoreilla.
[qemu_use](http://wiki.qemu.org/download/qemu-doc.html#Supported-Operating-Systems)
[tinycc](http://landley.net/aboriginal/presentation.html#cross_advantages)


## Valinta
Toteutustavan valinnassa mietittiin kahden vaihtoehdon välillä. Ensimmäinen vaihtoehto oli pieni vähävirtainen ARM-arkkitehtuurinen laite (Raspberry Pi [raspi], CuBox[cubox]) ja emuloida x86-järjestelmä QEMU:lla. Toinen vaihtoehto oli käyttää x86-arkkitehtuurin kannettavaa aihiona, jossa tarvittavat ohjelmat pyörivät osittain Wine-rajapinnan kautta ja osittain DOSEMU-emulaattorissa. Sekä Wine- että DOSEMU mahdollistavat isäntäkoneen sarjaporttien mappaamisen kohdeohjelmien käyttöön.

[raspi](http://www.raspberrypi.org/)
[cubox](http://www.solid-run.com/products)