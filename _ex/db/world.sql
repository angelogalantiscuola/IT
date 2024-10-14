CREATE DATABASE IF NOT EXISTS `world`;
USE `world`;

-- MySQL dump 10.16  Distrib 10.1.33-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: gisq
-- ------------------------------------------------------
-- Server version	10.1.33-MariaDB
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO,ANSI' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table "world"
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE "world" (
  "name" varchar(50) NOT NULL,
  "continent" varchar(60) DEFAULT NULL,
  "area" decimal(10,0) DEFAULT NULL,
  "population" decimal(11,0) DEFAULT NULL,
  "gdp" decimal(14,0) DEFAULT NULL,
  "capital" varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  "tld" varchar(5) DEFAULT NULL,
  "flag" varchar(255) DEFAULT NULL,
  PRIMARY KEY ("name"),
  KEY "world" ("continent")
);
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "world"
--

INSERT INTO "world" VALUES ('Afghanistan','Asia',652230,25500100,20364000000,'Kabul','.af','//upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg');
INSERT INTO "world" VALUES ('Albania','Europe',28748,2821977,12044000000,'Tirana','.al','//upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg');
INSERT INTO "world" VALUES ('Algeria','Africa',2381741,38700000,207021000000,'Algiers','.dz','//upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg');
INSERT INTO "world" VALUES ('Andorra','Europe',468,76098,3222000000,'Andorra la Vella','.ad','//upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Andorra.svg');
INSERT INTO "world" VALUES ('Angola','Africa',1246700,19183590,116308000000,'Luanda','.ao','//upload.wikimedia.org/wikipedia/commons/9/9d/Flag_of_Angola.svg');
INSERT INTO "world" VALUES ('Antigua and Barbuda','Caribbean',442,86295,1176000000,'St. John\'s','.ag','//upload.wikimedia.org/wikipedia/commons/8/89/Flag_of_Antigua_and_Barbuda.svg');
INSERT INTO "world" VALUES ('Argentina','South America',2780400,42669500,477028000000,'Buenos Aires','.ar','//upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg');
INSERT INTO "world" VALUES ('Armenia','Eurasia',29743,3017400,9950000000,'Yerevan','.am','//upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_Armenia.svg');
INSERT INTO "world" VALUES ('Australia','Oceania',7692024,23545500,1564419000000,'Canberra','.au','//upload.wikimedia.org/wikipedia/commons/b/b9/Flag_of_Australia.svg');
INSERT INTO "world" VALUES ('Austria','Europe',83871,8504850,394458000000,'Vienna','.at','//upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Austria.svg');
INSERT INTO "world" VALUES ('Azerbaijan','Asia',86600,9477100,68727000000,'Baku','.az','//upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Azerbaijan.svg');
INSERT INTO "world" VALUES ('Bahamas','Caribbean',13878,351461,8043000000,'Nassau','.bs','//upload.wikimedia.org/wikipedia/commons/9/93/Flag_of_the_Bahamas.svg');
INSERT INTO "world" VALUES ('Bahrain','Asia',765,1234571,30362000000,'Manama','.bh','//upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bahrain_1972.svg');
INSERT INTO "world" VALUES ('Bangladesh','Asia',147570,156557000,127195000000,'Dhaka','.bd','//upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg');
INSERT INTO "world" VALUES ('Barbados','Caribbean',430,285000,4533000000,'Bridgetown','.bb','//upload.wikimedia.org/wikipedia/commons/e/ef/Flag_of_Barbados.svg');
INSERT INTO "world" VALUES ('Belarus','Europe',207600,9467000,63259000000,'Minsk','.by','//upload.wikimedia.org/wikipedia/commons/8/85/Flag_of_Belarus.svg');
INSERT INTO "world" VALUES ('Belgium','Europe',30528,11198638,483402000000,'City of Brussels','.be','//upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg');
INSERT INTO "world" VALUES ('Belize','North America',22966,349728,1554000000,'Belmopan','.bz','//upload.wikimedia.org/wikipedia/commons/e/e7/Flag_of_Belize.svg');
INSERT INTO "world" VALUES ('Benin','Africa',112622,9988068,7557000000,'Porto-Novo','.bj','//upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Benin.svg');
INSERT INTO "world" VALUES ('Bhutan','Asia',38394,749090,1861000000,'Thimphu','.bt','//upload.wikimedia.org/wikipedia/commons/9/91/Flag_of_Bhutan.svg');
INSERT INTO "world" VALUES ('Bolivia','South America',1098581,10027254,27035000000,'Sucre','.bo','//upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Bolivia.svg');
INSERT INTO "world" VALUES ('Bosnia and Herzegovina','Europe',51209,3791622,17319000000,'Sarajevo','.ba','//upload.wikimedia.org/wikipedia/commons/b/bf/Flag_of_Bosnia_and_Herzegovina.svg');
INSERT INTO "world" VALUES ('Botswana','Africa',582000,2024904,14410000000,'Gaborone','.bw','//upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_Botswana.svg');
INSERT INTO "world" VALUES ('Brazil','South America',8515767,202794000,2254109000000,'Brasília','.br','//upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg');
INSERT INTO "world" VALUES ('Brunei','Asia',5765,393162,16954000000,'Bandar Seri Begawan','.bn','//upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg');
INSERT INTO "world" VALUES ('Bulgaria','Europe',110879,7245677,50972000000,'Sofia','.bg','//upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Bulgaria.svg');
INSERT INTO "world" VALUES ('Burkina Faso','Africa',272967,17322796,10687000000,'Ouagadougou','.bf','//upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Burkina_Faso.svg');
INSERT INTO "world" VALUES ('Burundi','Africa',27834,9420248,2257000000,'Bujumbura','.bi','//upload.wikimedia.org/wikipedia/commons/5/50/Flag_of_Burundi.svg');
INSERT INTO "world" VALUES ('Cambodia','Asia',181035,15184116,14038000000,'Phnom Penh','.kh','//upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg');
INSERT INTO "world" VALUES ('Cameroon','Africa',475442,20386799,26094000000,'Yaoundé','.cm','//upload.wikimedia.org/wikipedia/commons/4/4f/Flag_of_Cameroon.svg');
INSERT INTO "world" VALUES ('Canada','North America',9984670,35427524,1585000000000,'Ottowa','.ca','//upload.wikimedia.org/wikipedia/en/c/cf/Flag_of_Canada.svg');
INSERT INTO "world" VALUES ('Cape Verde','Africa',4033,491875,1903000000,'Praia','.cv','//upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Cape_Verde.svg');
INSERT INTO "world" VALUES ('Central African Republic','Africa',622984,4709000,2184000000,'Bangui','.cf','//upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_the_Central_African_Republic.svg');
INSERT INTO "world" VALUES ('Chad','Africa',1284000,13211000,10183000000,'N\'Djamena','.td','//upload.wikimedia.org/wikipedia/commons/4/4b/Flag_of_Chad.svg');
INSERT INTO "world" VALUES ('Chile','South America',756102,17773000,268314000000,'Santiago','.cl','//upload.wikimedia.org/wikipedia/commons/7/78/Flag_of_Chile.svg');
INSERT INTO "world" VALUES ('China','Asia',9596961,1365370000,8358400000000,'Beijing','.cn','//upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg');
INSERT INTO "world" VALUES ('Colombia','South America',1141748,47662000,369813000000,'Bogotá','.co','//upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Colombia.svg');
INSERT INTO "world" VALUES ('Comoros','Africa',1862,743798,616000000,'Moroni','.km','//upload.wikimedia.org/wikipedia/commons/9/94/Flag_of_the_Comoros.svg');
INSERT INTO "world" VALUES ('Congo, Democratic Republic of','Africa',2345000,69360000,NULL,'Kinshasa','.cd','//upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg');
INSERT INTO "world" VALUES ('Congo, Republic of','Africa',342000,4559000,NULL,'Brazzaville','.cg','//upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_the_Republic_of_the_Congo.svg');
INSERT INTO "world" VALUES ('Costa Rica','North America',51100,4667096,45107000000,'San José','.cr','//upload.wikimedia.org/wikipedia/commons/f/f2/Flag_of_Costa_Rica.svg');
INSERT INTO "world" VALUES ('Côte d\'Ivoire','Africa',322483,23919000,34506000000,'Yamoussoukro','.ci','//upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_C%C3%B4te_d%27Ivoire.svg');
INSERT INTO "world" VALUES ('Croatia','Europe',56594,4290612,56447000000,'Zagreb','.hr','//upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Croatia.svg');
INSERT INTO "world" VALUES ('Cuba','Caribbean',109884,11167325,71017000000,'Havana','.cu','//upload.wikimedia.org/wikipedia/commons/b/bd/Flag_of_Cuba.svg');
INSERT INTO "world" VALUES ('Cyprus','Asia',9251,865878,22768000000,'Nicosia','.cy','//upload.wikimedia.org/wikipedia/commons/d/d4/Flag_of_Cyprus.svg');
INSERT INTO "world" VALUES ('Czech Republic','Europe',78865,10517400,196446000000,'Prague','.cz','//upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_Czech_Republic.svg');
INSERT INTO "world" VALUES ('Denmark','Europe',43094,5634437,314889000000,'Copenhagen','.dk','//upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Denmark.svg');
INSERT INTO "world" VALUES ('Djibouti','Africa',23200,886000,1361000000,'Djibouti','.dj','//upload.wikimedia.org/wikipedia/commons/3/34/Flag_of_Djibouti.svg');
INSERT INTO "world" VALUES ('Dominica','Caribbean',751,71293,499000000,'Roseau','.dm','//upload.wikimedia.org/wikipedia/commons/c/c4/Flag_of_Dominica.svg');
INSERT INTO "world" VALUES ('Dominican Republic','Caribbean',48671,9445281,58898000000,'Santo Domingo','.do','//upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_the_Dominican_Republic.svg');
INSERT INTO "world" VALUES ('Ecuador','South America',276841,15774200,87495000000,'Quito','.ec','//upload.wikimedia.org/wikipedia/commons/e/e8/Flag_of_Ecuador.svg');
INSERT INTO "world" VALUES ('Egypt','Asia',1002450,86736900,254671000000,'Cairo','.eg','//upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg');
INSERT INTO "world" VALUES ('El Salvador','North America',21041,6384000,23864000000,'San Salvador','.sv','//upload.wikimedia.org/wikipedia/commons/3/34/Flag_of_El_Salvador.svg');
INSERT INTO "world" VALUES ('Equatorial Guinea','Africa',28051,1622000,14491000000,'Malabo','.gq','//upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Equatorial_Guinea.svg');
INSERT INTO "world" VALUES ('Eritrea','Africa',117600,6536000,3108000000,'Asmara','.er','//upload.wikimedia.org/wikipedia/commons/2/29/Flag_of_Eritrea.svg');
INSERT INTO "world" VALUES ('Estonia','Europe',45227,1315819,22376000000,'Tallinn','.ee','//upload.wikimedia.org/wikipedia/commons/8/8f/Flag_of_Estonia.svg');
INSERT INTO "world" VALUES ('Ethiopia','Africa',1104300,87952991,41605000000,'Addis Ababa','.et','//upload.wikimedia.org/wikipedia/commons/7/71/Flag_of_Ethiopia.svg');
INSERT INTO "world" VALUES ('Fiji','Oceania',18272,858038,3999000000,'Suva','.fj','//upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Fiji.svg');
INSERT INTO "world" VALUES ('Finland','Europe',338424,5458038,247389000000,'Helsinki','.fi','//upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Finland.svg');
INSERT INTO "world" VALUES ('France','Europe',640679,65906000,2611221000000,'Paris','.fr','//upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg');
INSERT INTO "world" VALUES ('Gabon','Africa',267668,1711000,24076000000,'Libreville','.ga','//upload.wikimedia.org/wikipedia/commons/0/04/Flag_of_Gabon.svg');
INSERT INTO "world" VALUES ('Gambia','Africa',11295,1882450,NULL,'Banjul','.gm','//upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_The_Gambia.svg');
INSERT INTO "world" VALUES ('Georgia','Asia',69700,4490500,15830000000,'Tbilisi','.ge','//upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Georgia.svg');
INSERT INTO "world" VALUES ('Germany','Europe',357114,80716000,3425956000000,'Bonn','.de','//upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg');
INSERT INTO "world" VALUES ('Ghana','Africa',238533,27043093,40711000000,'Accra','.gh','//upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Ghana.svg');
INSERT INTO "world" VALUES ('Greece','Europe',131990,11123034,248941000000,'Athens','.gr','//upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Greece.svg');
INSERT INTO "world" VALUES ('Grenada','Caribbean',344,103328,783000000,'St. George\'s','.gd','//upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Grenada.svg');
INSERT INTO "world" VALUES ('Guatemala','North America',108889,15806675,50377000000,'Guatemala City','.gt','//upload.wikimedia.org/wikipedia/commons/e/ec/Flag_of_Guatemala.svg');
INSERT INTO "world" VALUES ('Guinea','Africa',245857,10824200,6092000000,'Conakry','.gn','//upload.wikimedia.org/wikipedia/commons/e/ed/Flag_of_Guinea.svg');
INSERT INTO "world" VALUES ('Guinea-Bissau','Africa',36125,1746000,849000000,'Bissau','.gw','//upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Guinea-Bissau.svg');
INSERT INTO "world" VALUES ('Guyana','South America',214969,784894,2851000000,'Georgetown','.gy','//upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_Guyana.svg');
INSERT INTO "world" VALUES ('Haiti','Caribbean',27750,10413211,7187000000,'Port-au-Prince','.ht','//upload.wikimedia.org/wikipedia/commons/5/58/Flag_of_Haiti_%281964-1986%29.svg');
INSERT INTO "world" VALUES ('Honduras','North America',112492,8555072,18564000000,'Tegucigalpa','.hn','//upload.wikimedia.org/wikipedia/commons/8/82/Flag_of_Honduras.svg');
INSERT INTO "world" VALUES ('Hungary','Europe',93028,9879000,124600000000,'Budapest','.hu','//upload.wikimedia.org/wikipedia/commons/c/c1/Flag_of_Hungary.svg');
INSERT INTO "world" VALUES ('Iceland','Europe',103000,326340,13579000000,'Reykjavík','.is','//upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Iceland.svg');
INSERT INTO "world" VALUES ('India','Asia',3166414,1246160000,1875213000000,'New Delhi','.in','//upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_India.svg');
INSERT INTO "world" VALUES ('Indonesia','Asia',1904569,252164800,878043000000,'Jakarta','.id','//upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg');
INSERT INTO "world" VALUES ('Iran','Asia',1648195,77552000,551588000000,'Tehran','.ir','//upload.wikimedia.org/wikipedia/commons/c/ca/Flag_of_Iran.svg');
INSERT INTO "world" VALUES ('Iraq','Asia',438317,36004552,149370000000,'Baghdad','.iq','//upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg');
INSERT INTO "world" VALUES ('Ireland','Europe',70273,4593100,210638000000,'Dublin','.ie','//upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Ireland.svg');
INSERT INTO "world" VALUES ('Israel','Asia',20770,8193900,241069000000,'Jerusalem','.il','//upload.wikimedia.org/wikipedia/commons/d/d4/Flag_of_Israel.svg');
INSERT INTO "world" VALUES ('Italy','Europe',301336,60782668,2013392000000,'Rome','.it','//upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg');
INSERT INTO "world" VALUES ('Jamaica','Caribbean',10991,2717991,14795000000,'Kingston','.jm','//upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Jamaica.svg');
INSERT INTO "world" VALUES ('Japan','Asia',377930,127090000,5960180000000,'Imperial Tokyo','.jp','//upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg');
INSERT INTO "world" VALUES ('Jordan','Asia',89342,6602190,30937000000,'Amman','.jo','//upload.wikimedia.org/wikipedia/commons/c/c0/Flag_of_Jordan.svg');
INSERT INTO "world" VALUES ('Kazakhstan','Europe',2724900,17244000,202656000000,'Astana','.kz','//upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kazakhstan.svg');
INSERT INTO "world" VALUES ('Kenya','Africa',580367,45546000,40697000000,'Nairobi','.ke','//upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg');
INSERT INTO "world" VALUES ('Kiribati','Oceania',811,106461,176000000,'South Tarawa','.ki','//upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kiribati.svg');
INSERT INTO "world" VALUES ('Kuwait','Asia',17818,3065850,183219000000,'Kuwait City','.kw','//upload.wikimedia.org/wikipedia/commons/a/aa/Flag_of_Kuwait.svg');
INSERT INTO "world" VALUES ('Kyrgyzstan','Asia',199951,5776570,6475000000,'Bishkek','.kg','//upload.wikimedia.org/wikipedia/commons/c/c7/Flag_of_Kyrgyzstan.svg');
INSERT INTO "world" VALUES ('Laos','Asia',236800,6580800,9100000000,'Vientiane','.la','//upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg');
INSERT INTO "world" VALUES ('Latvia','Europe',64559,1996500,28379000000,'Riga','.lv','//upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Latvia.svg');
INSERT INTO "world" VALUES ('Lebanon','Asia',10452,4966000,42490000000,'Beirut','.lb','//upload.wikimedia.org/wikipedia/commons/5/59/Flag_of_Lebanon.svg');
INSERT INTO "world" VALUES ('Lesotho','Africa',30355,2098000,2443000000,'Maseru','.ls','//upload.wikimedia.org/wikipedia/commons/c/c0/Flag_of_Lesotho_%281987-2006%29.svg');
INSERT INTO "world" VALUES ('Liberia','Africa',111369,4397000,1491000000,'Monrovia','.lr','//upload.wikimedia.org/wikipedia/commons/b/b8/Flag_of_Liberia.svg');
INSERT INTO "world" VALUES ('Libya','Africa',1759540,6253000,95802000000,'Tripoli','.ly','//upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Libya.svg');
INSERT INTO "world" VALUES ('Liechtenstein','Europe',160,37132,5827000000,'Vaduz','.li','//upload.wikimedia.org/wikipedia/commons/4/47/Flag_of_Liechtenstein.svg');
INSERT INTO "world" VALUES ('Lithuania','Europe',65300,2939431,42339000000,'Vilnius','.lt','//upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Lithuania.svg');
INSERT INTO "world" VALUES ('Luxembourg','Europe',2586,549700,55143000000,'Luxembourg','.lu','//upload.wikimedia.org/wikipedia/commons/d/da/Flag_of_Luxembourg.svg');
INSERT INTO "world" VALUES ('Macedonia','Europe',25713,2062294,NULL,'Skopje','.mk','//upload.wikimedia.org/wikipedia/commons/f/f8/Flag_of_Macedonia.svg');
INSERT INTO "world" VALUES ('Madagascar','Africa',587041,21263403,9968000000,'Antananarivo','.mg','//upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Madagascar.svg');
INSERT INTO "world" VALUES ('Malawi','Africa',118484,16829000,5653000000,'Lilongwe','.mw','//upload.wikimedia.org/wikipedia/commons/1/10/Flag_of_Malawi_%282010-2012%29.svg');
INSERT INTO "world" VALUES ('Malaysia','Asia',330803,30177000,304726000000,'Kuala Lumpur','.my','//upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg');
INSERT INTO "world" VALUES ('Maldives','Asia',300,317280,2606000000,'Malé','.mv','//upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Maldives.svg');
INSERT INTO "world" VALUES ('Mali','Africa',1240192,15768000,10262000000,'Bamako','.ml','//upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_Mali.svg');
INSERT INTO "world" VALUES ('Malta','Europe',316,416055,8775000000,'Valletta','.mt','//upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Malta.svg');
INSERT INTO "world" VALUES ('Marshall Islands','Oceania',181,56086,198000000,'Majuro','.mh','//upload.wikimedia.org/wikipedia/commons/2/2e/Flag_of_the_Marshall_Islands.svg');
INSERT INTO "world" VALUES ('Mauritania','Africa',1030700,3461041,3866000000,'Nouakchott','.mr','//upload.wikimedia.org/wikipedia/commons/4/43/Flag_of_Mauritania.svg');
INSERT INTO "world" VALUES ('Mauritius','Africa',2040,1257900,11452000000,'Port Louis','.mu','//upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Mauritius.svg');
INSERT INTO "world" VALUES ('Mexico','North America',1964375,119713203,1183655000000,'Mexico City','.mx','//upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg');
INSERT INTO "world" VALUES ('Micronesia, Federated States of','Oceania',702,101351,327000000,'Palikir','.fm','//upload.wikimedia.org/wikipedia/commons/e/e4/Flag_of_the_Federated_States_of_Micronesia.svg');
INSERT INTO "world" VALUES ('Moldova','Europe',33846,3557600,7253000000,'Chișinău','.md','//upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Moldova.svg');
INSERT INTO "world" VALUES ('Monaco','Europe',2,36950,5707000000,'Monaco-Ville','.mc','//upload.wikimedia.org/wikipedia/commons/e/ea/Flag_of_Monaco.svg');
INSERT INTO "world" VALUES ('Mongolia','Asia',1564110,2931300,10271000000,'Ulaanbaatar','.mn','//upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Mongolia.svg');
INSERT INTO "world" VALUES ('Montenegro','Europe',13812,620029,4046000000,'Podgorica','.me','//upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Montenegro.svg');
INSERT INTO "world" VALUES ('Morocco','Africa',446550,33307500,95992000000,'Rabat','.ma','//upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg');
INSERT INTO "world" VALUES ('Mozambique','Africa',801590,23700715,14605000000,'Maputo','.mz','//upload.wikimedia.org/wikipedia/commons/d/d0/Flag_of_Mozambique.svg');
INSERT INTO "world" VALUES ('Myanmar','Asia',676578,61120000,59444000000,'Naypyidaw','.mm','//upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg');
INSERT INTO "world" VALUES ('Namibia','Africa',825615,2113077,12807000000,'Windhoek','.na','//upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Namibia.svg');
INSERT INTO "world" VALUES ('Nauru','Oceania',21,9945,121000000,'Yaren District','.nr','//upload.wikimedia.org/wikipedia/commons/3/30/Flag_of_Nauru.svg');
INSERT INTO "world" VALUES ('Nepal','Asia',147181,26494504,18029000000,'Kathmandu','.np','//upload.wikimedia.org/wikipedia/commons/9/9b/Flag_of_Nepal.svg');
INSERT INTO "world" VALUES ('Netherlands','Europe',41543,16857500,800535000000,'Amsterdam','.nl','//upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg');
INSERT INTO "world" VALUES ('New Zealand','Oceania',270467,4538520,171256000000,'Wellington','.nz','//upload.wikimedia.org/wikipedia/commons/3/3e/Flag_of_New_Zealand.svg');
INSERT INTO "world" VALUES ('Nicaragua','North America',130373,6071045,10508000000,'Managua','.ni','//upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Nicaragua.svg');
INSERT INTO "world" VALUES ('Niger','Africa',1267000,17138707,6773000000,'Niamey','.ne','//upload.wikimedia.org/wikipedia/commons/f/f4/Flag_of_Niger.svg');
INSERT INTO "world" VALUES ('Nigeria','Africa',923768,178517000,286470000000,'Abuja','.ng','//upload.wikimedia.org/wikipedia/commons/7/79/Flag_of_Nigeria.svg');
INSERT INTO "world" VALUES ('North Korea','Asia',120538,25027000,14411000000,'Pyongyang','.kp','//upload.wikimedia.org/wikipedia/commons/5/51/Flag_of_North_Korea.svg');
INSERT INTO "world" VALUES ('Norway','Europe',323802,5124383,499667000000,'Oslo','.no','//upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Norway.svg');
INSERT INTO "world" VALUES ('Oman','Asia',309500,4020000,78111000000,'Muscat','.om','//upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Oman.svg');
INSERT INTO "world" VALUES ('Pakistan','Asia',881912,188020000,215117000000,'Islamabad','.pk','//upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg');
INSERT INTO "world" VALUES ('Palau','Oceania',459,20901,213000000,'Ngerulmud','.pw','//upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Palau.svg');
INSERT INTO "world" VALUES ('Panama','North America',75417,3405813,36253000000,'Panama City','.pa','//upload.wikimedia.org/wikipedia/commons/a/ab/Flag_of_Panama.svg');
INSERT INTO "world" VALUES ('Papua New Guinea','Oceania',462840,7398500,15677000000,'Port Moresby','.pg','//upload.wikimedia.org/wikipedia/commons/e/e3/Flag_of_Papua_New_Guinea.svg');
INSERT INTO "world" VALUES ('Paraguay','South America',406752,6783374,25935000000,'Asunción','.py','//upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Paraguay.svg');
INSERT INTO "world" VALUES ('Peru','South America',1285216,30475144,204681000000,'Lima','.pe','//upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Peru.svg');
INSERT INTO "world" VALUES ('Philippines','Asia',342353,99804200,250182000000,'Manila','.ph','//upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg');
INSERT INTO "world" VALUES ('Poland','Europe',312679,38496000,489852000000,'Warsaw','.pl','//upload.wikimedia.org/wikipedia/commons/1/12/Flag_of_Poland.svg');
INSERT INTO "world" VALUES ('Portugal','Europe',92090,10477800,212139000000,'Lisbon','.pt','//upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg');
INSERT INTO "world" VALUES ('Qatar','Asia',11586,2174035,192402000000,'Doha','.qa','//upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Qatar.svg');
INSERT INTO "world" VALUES ('Romania','Europe',238391,19942642,169396000000,'Bucharest','.ro','//upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Romania.svg');
INSERT INTO "world" VALUES ('Russia','Eurasia',17125242,146000000,2029812000000,'Moscow','.ru','//upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg');
INSERT INTO "world" VALUES ('Rwanda','Africa',26338,10537222,7103000000,'Kigali','.rw','//upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Rwanda.svg');
INSERT INTO "world" VALUES ('Saint Kitts and Nevis','North America',261,55000,765000000,'Basseterre','.kn','//upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Saint_Kitts_and_Nevis.svg');
INSERT INTO "world" VALUES ('Saint Lucia','Caribbean',616,180000,1318000000,'Castries','.lc','//upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Saint_Lucia.svg');
INSERT INTO "world" VALUES ('Saint Vincent and the Grenadines','South America',389,109000,694000000,'Kingstown','.vc','//upload.wikimedia.org/wikipedia/commons/6/6d/Flag_of_Saint_Vincent_and_the_Grenadines.svg');
INSERT INTO "world" VALUES ('Samoa','Oceania',2842,187820,681000000,'Apia','.ws','//upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Samoa.svg');
INSERT INTO "world" VALUES ('San Marino','Europe',61,32637,1853000000,'San Marino','.sm','//upload.wikimedia.org/wikipedia/commons/b/b1/Flag_of_San_Marino.svg');
INSERT INTO "world" VALUES ('Sao Tomé and Príncipe','Africa',964,190428,707000000,'São Tomé','.st','//upload.wikimedia.org/wikipedia/commons/4/4f/Flag_of_Sao_Tome_and_Principe.svg');
INSERT INTO "world" VALUES ('Saudi Arabia','Asia',2149690,29994272,711050000000,'Riyadh','.sa','//upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_Saudi_Arabia.svg');
INSERT INTO "world" VALUES ('Senegal','Africa',196722,12873601,13962000000,'Dakar','.sn','//upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Senegal.svg');
INSERT INTO "world" VALUES ('Serbia','Europe',88361,7181505,38491000000,'Belgrade','.rs','//upload.wikimedia.org/wikipedia/commons/6/6d/Flag_of_Serbia_%282004-2010%29.svg');
INSERT INTO "world" VALUES ('Seychelles','Africa',452,90945,1031000000,'Victoria','.sc','//upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Seychelles.svg');
INSERT INTO "world" VALUES ('Sierra Leone','Africa',71740,6190280,43366000000,'Freetown','.sl','//upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Sierra_Leone.svg');
INSERT INTO "world" VALUES ('Singapore','Asia',710,5399200,276520000000,'Singapore','.sg','//upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg');
INSERT INTO "world" VALUES ('Slovakia','Europe',49037,5415949,91349000000,'Bratislava','.sk','//upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Slovakia.svg');
INSERT INTO "world" VALUES ('Slovenia','Europe',20273,2063151,45380000000,'Ljubljana','.si','//upload.wikimedia.org/wikipedia/commons/f/f0/Flag_of_Slovenia.svg');
INSERT INTO "world" VALUES ('Solomon Islands','Oceania',28896,581344,1010000000,'Honiara','.sb','//upload.wikimedia.org/wikipedia/commons/7/74/Flag_of_the_Solomon_Islands.svg');
INSERT INTO "world" VALUES ('Somalia','Africa',637657,10806000,1306000000,'Mogadishu','.so','//upload.wikimedia.org/wikipedia/commons/a/a0/Flag_of_Somalia.svg');
INSERT INTO "world" VALUES ('South Africa','Africa',1221037,52981991,384313000000,'Pretoria','.za','//upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg');
INSERT INTO "world" VALUES ('South Korea','Asia',100210,50423955,1129598000000,'Seoul','.kr','//upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_South_Korea.svg');
INSERT INTO "world" VALUES ('South Sudan','Africa',619745,11739000,10060000000,'Juba','.ss','//upload.wikimedia.org/wikipedia/commons/7/7a/Flag_of_South_Sudan.svg');
INSERT INTO "world" VALUES ('Spain','Europe',505992,46609700,1322126000000,'Madrid','.es','//upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg');
INSERT INTO "world" VALUES ('Sri Lanka','Asia',65610,20277597,59421000000,'Sri Jayawardenepura Kotte','.lk','//upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Sri_Lanka.svg');
INSERT INTO "world" VALUES ('Sudan','Africa',1886068,37289406,51453000000,'Khartoum','.sd','//upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Sudan.svg');
INSERT INTO "world" VALUES ('Suriname','South America',163820,534189,5012000000,'Paramaribo','.sr','//upload.wikimedia.org/wikipedia/commons/6/60/Flag_of_Suriname.svg');
INSERT INTO "world" VALUES ('Swaziland','Africa',17364,1268000,3861000000,'Lobamba','.sz','//upload.wikimedia.org/wikipedia/commons/1/1e/Flag_of_Swaziland.svg');
INSERT INTO "world" VALUES ('Sweden','Europe',450295,9675885,523804000000,'Stockholm','.se','//upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg');
INSERT INTO "world" VALUES ('Switzerland','Europe',41284,8160900,631183000000,'Bern','.ch','//upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Switzerland.svg');
INSERT INTO "world" VALUES ('Syria','Asia',185180,21987000,46540000000,'Damascus','.sy','//upload.wikimedia.org/wikipedia/commons/5/53/Flag_of_Syria.svg');
INSERT INTO "world" VALUES ('Taiwan','Asia',36193,23386883,NULL,'Taipei','.tw','//upload.wikimedia.org/wikipedia/commons/7/72/Flag_of_the_Republic_of_China.svg');
INSERT INTO "world" VALUES ('Tajikistan','Asia',143100,8160000,7633000000,'Dushanbe','.tj','//upload.wikimedia.org/wikipedia/commons/d/d0/Flag_of_Tajikistan.svg');
INSERT INTO "world" VALUES ('Tanzania','Africa',945087,44928923,28249000000,'Dodoma','.tz','//upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Tanzania.svg');
INSERT INTO "world" VALUES ('Thailand','Asia',513120,64456700,385694000000,'Bangkok','.th','//upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg');
INSERT INTO "world" VALUES ('Timor-Leste','Asia',14874,1212107,5387000000,'Dili','.tl','//upload.wikimedia.org/wikipedia/commons/2/26/Flag_of_East_Timor.svg');
INSERT INTO "world" VALUES ('Togo','Africa',56785,6993000,3917000000,'Lomé','.tg','//upload.wikimedia.org/wikipedia/commons/9/91/Flag_of_Togo_%281958-1960%29.svg');
INSERT INTO "world" VALUES ('Tonga','Oceania',747,103036,465000000,'Nuku\'alofa','.to','//upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Tonga.svg');
INSERT INTO "world" VALUES ('Trinidad and Tobago','Caribbean',5130,1328019,23225000000,'Port of Spain','.tt','//upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Trinidad_and_Tobago.svg');
INSERT INTO "world" VALUES ('Tunisia','Africa',163610,10886500,45132000000,'Tunis','.tn','//upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg');
INSERT INTO "world" VALUES ('Turkey','Asia',783562,76667864,788299000000,'Ankara','.tr','//upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg');
INSERT INTO "world" VALUES ('Turkmenistan','Asia',488100,5307000,33466000000,'Aşgabat','.tm','//upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Turkmenistan.svg');
INSERT INTO "world" VALUES ('Tuvalu','Oceania',26,11323,40000000,'Funafuti','.tv','//upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Tuvalu.svg');
INSERT INTO "world" VALUES ('Uganda','Africa',241550,35357000,21736000000,'Kampala','.ug','//upload.wikimedia.org/wikipedia/commons/4/4e/Flag_of_Uganda.svg');
INSERT INTO "world" VALUES ('Ukraine','Europe',603500,43009258,176309000000,'Kiev','.ua','//upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg');
INSERT INTO "world" VALUES ('United Arab Emirates','Asia',83600,9446000,383799000000,'Abu Dhabi','.ae','//upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_United_Arab_Emirates.svg');
INSERT INTO "world" VALUES ('United Kingdom','Europe',242900,64105700,2471600000000,'London','.uk','//upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg');
INSERT INTO "world" VALUES ('United States','North America',9826675,318320000,16244600000000,'Washington, D.C.','.us','//upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg');
INSERT INTO "world" VALUES ('Uruguay','South America',181034,3286314,49919000000,'Montevideo','.uy','//upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Uruguay.svg');
INSERT INTO "world" VALUES ('Uzbekistan','Asia',447400,30492800,51414000000,'Tashkent','.uz','//upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg');
INSERT INTO "world" VALUES ('Vanuatu','Oceania',12189,264652,752000000,'Port Vila','.vu','//upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Vanuatu.svg');
INSERT INTO "world" VALUES ('Vatican City','Europe',0,839,NULL,NULL,'.va','//upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_the_Vatican_City.svg');
INSERT INTO "world" VALUES ('Venezuela','South America',916445,28946101,382424000000,'Caracas','.ve','//upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Venezuela.svg');
INSERT INTO "world" VALUES ('Vietnam','Asia',331212,89708900,155820000000,'Hanoi','.vn','//upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg');
INSERT INTO "world" VALUES ('Yemen','Asia',527968,25235000,32831000000,'Sana‘a','.ye','//upload.wikimedia.org/wikipedia/commons/8/89/Flag_of_Yemen.svg');
INSERT INTO "world" VALUES ('Zambia','Africa',752612,15023315,21490000000,'Lusaka','.zm','//upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Zambia.svg');
INSERT INTO "world" VALUES ('Zimbabwe','Africa',390757,13061239,9802000000,'Harare','.zw','//upload.wikimedia.org/wikipedia/commons/6/6a/Flag_of_Zimbabwe.svg');
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-12 14:29:23
