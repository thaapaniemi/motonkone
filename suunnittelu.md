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
	*selvitä paljonko tehohukkaa
* Ei rajoituksia lähtö- ja kohdearkkitehtuureilla
	* X86-ohjelmia ARM-arkkitehtuurilla (pienempi tehonkulutus, koko)

