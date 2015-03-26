<!-- 02:Johdanto -->

### Lyhenteet

x86: Yleisnimitys Intelin 1987 julkaisemalle CISC-prosessorikäskykannalle. Alkuperäiset 8086/80186/80286 olivat 16-bittisiä, mutta 80386:sta eteenpäin käskykantaa laajennettiin 32-bittiseksi.

PS/2: Sarjaväyläinen, alunperin IBM PS/2 koneessa ollut liitäntäprotokolla, joka yleistyi PC-koneiden standardiliitännäksi näppäimistölle ja hiirelle ennen USB-protokollaa. 5V, GND, data, clock. Suunniteltu 1987 [lähde?]

RS232: Alunperin v. 1962 esitelty asynkroninen sarjaliitäntäprotokolla, joka oli ennen USB-liitännän yleistymistä yleisin PC-koneiden oheislaitteiden liitäntäväylä.

USB: Universal Serial BUS, sarjaväyläinen liitäntä kaikkien oheislaitteiden liitäntään. (1996)

IDE/PATA:  Integrated Drive Electronics (Parallel AT Attachments), kiintolevyjen ja optisten asemien liittämiseen tarkoitettu 16-bittinen rinnakkainen liitäntäväylä (1986)

CAN:  Controller Area Network, vikasietoinen, differentiaalinen kaksijohtoinen automaatioväylä, jossa liikenne lähetetään priorisoituina sanomina. (1986)


### Johdanto

Tietokoneiden käyttöikä on varsinkin vaativissa kohteissa rajallinen. Kun järjestelmien ikä kasvaa niin varaosien saatavuus vähenee. Viimein ollaan pisteessä, missä ainoa vaihtoehto on korvata vanha järjestelmä uudella. Tämä saattaa vaatia mittavia päivitysprojekteja myös järjestelmää tukeviin kokonaisuuksiin ja vaihdon kannattavuus suhteessa hyötyyn on huono. 

Järjestelmänä on vuonna xxx valmistetun metsätraktori, eli tuttavallisemmin moto. Motolla on n. yy v käyttöikää jäljellä ja moton ajoneuvotietokone, jolla hallitaan koneen moottoriasetuksia, että myös puiden kadon hallintaa, alkaa olemaan elinikänsä loppupäässä. Alkuperäinen tietokone lakkaa toimimasta kokonaan kuumennettuaan liikaa, kiintolevy on hajonnyt useaan otteeseen ja akustot alkavat olemaan uusimisen tarpeessa. Jos laitteiston vaihtaisi kokonaan uudempaan olisi kyseessä sen verran kallis toimenpide(n. 20 000€), ettei sitä kannata tehdä enää kyseiseen metsätraktoriin. Tämän takia tutkimmekin vaihtoehtoisia ratkaisuita lisätä metsätraktorin käytössä olevalle tietokonejärjestelmälle elinikää.

Insinöörityön aiheena on löytää motossa käytetylle 15v vanhan Sunit Nero-ajoneuvotietokoneelle korvaava uudempi, mutta yhteensopiva tietokone. Tavoitteena on uuden laitteen yhteensopivuus vanhan kiinnitysjärjestelmän kanssa, liitinyhteensopivuus, sekä ohjelmallisen tason yhteensopivuus. Aluksi tutustutaan käytössä olevaan laitteistoon ja sen asettamiin vaatimuksiin. Seuraavaksi käydään läpi mahdollisia toteuttamisvaihtoehtoja ja niiden ominaisuuksia. Asennetaan uusi ohjelmisto testikannetavaan ja testataan järjestelmä tuotantoympäristössä. Lopuksi tutkitaan mahdolliset 


Haasteita työlle asettavat vanhat ohjelmistot, tärinää ja pölyä ja vaihtelevia lämpötiloja sisältävä työympäristö. Metsätraktori on huoltoja lukuunottamatta metsässä kesät talvet ja lämpötilat vaihtelevat talvella -20 asteesta +20 asteeseen ja kesäisin lämmöt voivat nousta ohjaamossa jopa +50-60 asteeseen.

<!-- 02:EOF -->