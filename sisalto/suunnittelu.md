# Suunnittelu

## Ohjelmiston toteutusvaihtoehdot

### Suora toteutus, "Natiivi"
Suorassa toteutuksessa tietokoneeseen asennettaan uusin käyttöjärjestelmä, mitä käytössä oleva laitteisto ja ohjelmat tukevat. Koska käytössä on kohtalaisen uutta laitteistoa (max ~5v vanhaa) ja käytössä olevat ohjelmistot ovat vuosituhannen vaihteesta, asettaa tämä haasteita löytää toimiva yhdistelmä.

*Laitteisto
	* Windows XP+ toimii
	* Windows 9x pitää testata
*Ohjelmistot
	* Windows 9x toimii
	* Windows XP ehkä jos löytää sopivan sarjaporttiajurin (tai sitten ei)


## Ohjelmistojen virtualisointi/emulointi
Käyttöjärjestelmän päällä ajetaan tarvittaessa sopivia rajapintakerroksia, jolloin vältytään ajamasta kahta käyttöjärjestelmää päällekäin. Windows/DOS-ohjelmille Linuxilla WINE+dosemu ja ja windowsilla dosbox?.
* Pienempi muistinkulutus
* nopeampi käynnistys?
* toimivuus pitää varmistaa

## Virtualisointi
Alkuperäisiä ohjelmistoja+käyttöjärjestelmää ajetaan virtuaalikoneessa toisen käyttöjärjestelmän päällä. 
* Virtuaalikoneohjelmistojen rajoitukset
	*Virtualbox: 2 sarjaporttia
* Isompi muistinkulutus
	*Win98 64MB, joten ei käytännössä väliä

## Emulointi
Alkuperäisiä ohjelmistoja+käyttöjärjestelmä ajetaan emulaattorissa toisen järjestelmän päällä.
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
	Emuloidaan vain user-space koko pc:n sijasta
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

