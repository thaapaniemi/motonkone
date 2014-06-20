# Suunnittelu

## Ohjelmiston toteutusvaihtoehdot
Tarkoituksena olisi löytää projektille sopiva vaihtoehto, missä alkuperäiset ohjelmistot saataisiin toimimaan käyttäjäystävällisesti ja vakaasti uuden laitteiston kanssa.

### Suora toteutus, "Natiivi"
Suorassa toteutuksessa tietokoneeseen asennettaan uusin käyttöjärjestelmä, mitä käytössä oleva laitteisto ja ohjelmat tukevat. Koska käytössä on kohtalaisen uutta laitteistoa (max ~5v vanhaa) ja käytössä olevat ohjelmistot ovat vuosituhannen vaihteesta, asettaa tämä haasteita löytää toimiva yhdistelmä. Vaihtoehto vaatii yhteensopivan laite- ja ohelmistoarkkitehtuurin vanhan järjestelmän kanssa.

* Laitteisto
	* Windows XP+ toimii
	* Windows 9x pitää testata
* Ohjelmistot
	* Windows 9x toimii
	* Windows XP ehkä jos löytää sopivan sarjaporttiajurin (tai sitten ei)


## Ohjelmistojen rajapintojen yhteensopivuuskerros
Käyttöjärjestelmän ja ohjelman välissä sopivia rajapintakerroksia, jolloin saadaan käyttöjärjestelmän kanssa yhteensopimattomat ohjelmat toimimaan keskenään. Vaihtoehto vaatii yhteensopivan laitteistoarkkitehtuurin alkuperäisen järjestelmän kanssa.
* ~Natiivinopeus
* ~Natiivimuistinkulutus
* eivät täydellisiä (nykyään kuitenkin varsin hyviä) joten yhteensopivuus pitää testata


## Virtualisointi
Alkuperäisiä ohjelmistoja+käyttöjärjestelmää ajetaan virtuaalikoneessa toisen käyttöjärjestelmän päällä. Näin saavutetaan varmin yhteensopivuus ohjelmistotasolla. Oheislaitteiden kanssa esiintyy rajoituksia, jotka pitää huomioida. Vaihtoehto vaatii yhteensopivan laitteistoarkkitehtuurin alkuperäisen järjestelmän kanssa.
* Virtuaalikoneohjelmistojen rajoitukset
	* Virtualbox: 2 sarjaporttia
* Isompi muistinkulutus
	* Win98 64MB, joten ei käytännössä väliä
* Hyötysuhde pienenee
	* Virtualisoinnilla päästään kuitenkin ~90%+ natiivista suorituskyvystä [http://www.anandtech.com/show/2770/10]

## Järjestelmäemulointi
Alkuperäisiä ohjelmistoja+käyttöjärjestelmä ajetaan emulaattorissa toisen järjestelmän päällä. Vaihtoehto ei vaadi minkäänlaista laitteisto- tai ohjelmistoarkkitehtuurillista yhteensopivuutta.

* Emulaattorirajoitukset?
* Hidasta
	* sormisääntö: oleta ~20% hyötysuhdetta
	 	* QEMU's ARM emulation on a 2Ghz x86_64 is likely to be faster than a real 400mhz ARM920T.
	 	* RaspberryPi:n päällä x86-emulaatio vastaa n. 486:sta
	 		* [http://rpix86.patrickaalto.com/index.html]
	 		* The emulation runs at a speed of around 20MHz 80486
	 	* [http://www.raspberrypi.org/forums/viewtopic.php?f=56&t=13161]
	 		* It was just about usable
	* parhaat emulaattorit pääsevät/pääsivät ~40% hyötysuhteesen [2012-10-03 http://www.embedded.com/electronics-news/4397737/X86-emulation-coming-to-ARM-processors]

## Ohjelmistojen emulointi
Emuloidaan vain user-space tai koko pc:n sijasta. Vaihtoehto ei vaadi minkäänlaista laitteisto- tai ohjelmistoarkkitehtuurillista yhteensopivuutta. Lähes samat viat kuin järjestelmäemulaattoreissa.
* QEMU 5. QEMU User space emulator
* Ei kokemusta, selvitä asiaa
	*http://wiki.qemu.org/download/qemu-doc.html#Supported-Operating-Systems

* Fabrice Bellard's Tinycc project in 2003 originally as a way to run Wine on non-x86 hosts. 
	* QEMU conceptually forked off it
	* http://landley.net/aboriginal/presentation.html#cross_advantages
	* Good rule of thumb is 20% of native speed, 
* QEMU Application Emulation is nice but limited


* Ei rajoituksia lähtö- ja kohdearkkitehtuureilla
	* X86-ohjelmia ARM-arkkitehtuurilla (pienempi tehonkulutus, koko)

