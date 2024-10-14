CREATE DATABASE IF NOT EXISTS `euro2012`;
USE `euro2012`;
-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: gisq
-- ------------------------------------------------------
-- Server version	10.0.21-MariaDB
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */
;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */
;
/*!40101 SET NAMES utf8 */
;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */
;
/*!40103 SET TIME_ZONE='+00:00' */
;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
;
--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8 */
;
CREATE TABLE `game` (
  `id` int(11) DEFAULT NULL,
  `mdate` varchar(12) DEFAULT NULL,
  `stadium` varchar(100) DEFAULT NULL,
  `team1` varchar(100) DEFAULT NULL,
  `team2` varchar(100) DEFAULT NULL
) ENGINE = MyISAM DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */
;
INSERT INTO `game`
VALUES (
    1001,
    '8 June 2012',
    'National Stadium, Warsaw',
    'POL',
    'GRE'
  ),
(
    1002,
    '8 June 2012',
    'Stadion Miejski (Wroclaw)',
    'RUS',
    'CZE'
  ),
(
    1003,
    '12 June 2012',
    'Stadion Miejski (Wroclaw)',
    'GRE',
    'CZE'
  ),
(
    1004,
    '12 June 2012',
    'National Stadium, Warsaw',
    'POL',
    'RUS'
  ),
(
    1005,
    '16 June 2012',
    'Stadion Miejski (Wroclaw)',
    'CZE',
    'POL'
  ),
(
    1006,
    '16 June 2012',
    'National Stadium, Warsaw',
    'GRE',
    'RUS'
  ),
(
    1007,
    '9 June 2012',
    'Metalist Stadium',
    'NED',
    'DEN'
  ),
(1008, '9 June 2012', 'Arena Lviv', 'GER', 'POR'),
(1009, '13 June 2012', 'Arena Lviv', 'DEN', 'POR'),
(
    1010,
    '13 June 2012',
    'Metalist Stadium',
    'NED',
    'GER'
  ),
(
    1011,
    '17 June 2012',
    'Metalist Stadium',
    'POR',
    'NED'
  ),
(1012, '17 June 2012', 'Arena Lviv', 'DEN', 'GER'),
(
    1013,
    '10 June 2012',
    'PGE Arena Gdansk',
    'ESP',
    'ITA'
  ),
(
    1014,
    '10 June 2012',
    'Stadion Miejski (Poznan)',
    'IRL',
    'CRO'
  ),
(
    1015,
    '14 June 2012',
    'Stadion Miejski (Poznan)',
    'ITA',
    'CRO'
  ),
(
    1016,
    '14 June 2012',
    'PGE Arena Gdansk',
    'ESP',
    'IRL'
  ),
(
    1017,
    '18 June 2012',
    'PGE Arena Gdansk',
    'CRO',
    'ESP'
  ),
(
    1018,
    '18 June 2012',
    'Stadion Miejski (Poznan)',
    'ITA',
    'IRL'
  ),
(1019, '11 June 2012', 'Donbass Arena', 'FRA', 'ENG'),
(
    1020,
    '11 June 2012',
    'Olimpiyskiy National Sports Complex',
    'UKR',
    'SWE'
  ),
(1021, '15 June 2012', 'Donbass Arena', 'UKR', 'FRA'),
(
    1022,
    '15 June 2012',
    'Olimpiyskiy National Sports Complex',
    'SWE',
    'ENG'
  ),
(1023, '19 June 2012', 'Donbass Arena', 'ENG', 'UKR'),
(
    1024,
    '19 June 2012',
    'Olimpiyskiy National Sports Complex',
    'SWE',
    'FRA'
  ),
(
    1025,
    '21 June 2012',
    'National Stadium, Warsaw',
    'CZE',
    'POR'
  ),
(
    1026,
    '22 June 2012',
    'PGE Arena Gdansk',
    'GER',
    'GRE'
  ),
(1027, '23 June 2012', 'Donbass Arena', 'ESP', 'FRA'),
(
    1028,
    '24 June 2012',
    'Olimpiyskiy National Sports Complex',
    'ENG',
    'ITA'
  ),
(1029, '27 June 2012', 'Donbass Arena', 'POR', 'ESP'),
(
    1030,
    '28 June 2012',
    'National Stadium, Warsaw',
    'GER',
    'ITA'
  ),
(
    1031,
    '1 July 2012',
    'Olimpiyskiy National Sports Complex',
    'ESP',
    'ITA '
  );
/*!40000 ALTER TABLE `game` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `eteam`
--

DROP TABLE IF EXISTS `eteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8 */
;
CREATE TABLE `eteam` (
  `id` varchar(3) DEFAULT NULL,
  `teamname` varchar(50) DEFAULT NULL,
  `coach` varchar(50) DEFAULT NULL
) ENGINE = MyISAM DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `eteam`
--

LOCK TABLES `eteam` WRITE;
/*!40000 ALTER TABLE `eteam` DISABLE KEYS */
;
INSERT INTO `eteam`
VALUES ('POL', 'Poland', 'Franciszek Smuda'),
('RUS', 'Russia', 'Dick Advocaat'),
('CZE', 'Czech Republic', 'Michal Bílek'),
('GRE', 'Greece', 'Fernando Santos'),
('NED', 'Netherlands', 'Bert van Marwijk'),
('DEN', 'Denmark', 'Morten Olsen'),
('GER', 'Germany', 'Joachim Löw'),
('POR', 'Portugal', 'Paulo Bento'),
('ESP', 'Spain', 'Vicente del Bosque'),
('ITA', 'Italy', 'Cesare Prandelli'),
(
    'IRL',
    'Republic of Ireland',
    'Giovanni Trapattoni'
  ),
('CRO', 'Croatia', 'Slaven Bilic'),
('UKR', 'Ukraine', 'Oleh Blokhin'),
('SWE', 'Sweden', 'Erik Hamrén'),
('ENG', 'England', 'Roy Hodgson'),
('FRA', 'France', 'Laurent Blanc');
/*!40000 ALTER TABLE `eteam` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `goal`
--

DROP TABLE IF EXISTS `goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8 */
;
CREATE TABLE `goal` (
  `matchid` int(11) NOT NULL DEFAULT '0',
  `teamid` varchar(3) DEFAULT NULL,
  `player` varchar(100) DEFAULT NULL,
  `gtime` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`matchid`, `gtime`)
) ENGINE = MyISAM DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `goal`
--

LOCK TABLES `goal` WRITE;
/*!40000 ALTER TABLE `goal` DISABLE KEYS */
;
INSERT INTO `goal`
VALUES (1001, 'POL', 'Robert Lewandowski', 17),
(1001, 'GRE', 'Dimitris Salpingidis', 51),
(1002, 'RUS', 'Alan Dzagoev', 15),
(1002, 'RUS', 'Alan Dzagoev', 79),
(1002, 'RUS', 'Roman Shirokov', 24),
(1002, 'RUS', 'Roman Pavlyuchenko', 82),
(1002, 'CZE', 'Václav Pilar', 52),
(1003, 'GRE', 'Theofanis Gekas', 53),
(1003, 'CZE', 'Petr Jirácek', 3),
(1003, 'CZE', 'Václav Pilar', 6),
(1004, 'POL', 'Jakub Blaszczykowski', 57),
(1004, 'RUS', 'Alan Dzagoev', 37),
(1005, 'CZE', 'Petr Jirácek', 72),
(1006, 'GRE', 'Giorgos Karagounis', 45),
(1007, 'DEN', 'Michael Krohn-Dehli', 24),
(1008, 'GER', 'Mario Gómez', 72),
(1009, 'DEN', 'Nicklas Bendtner', 41),
(1009, 'DEN', 'Nicklas Bendtner', 80),
(1009, 'POR', 'Pepe (footballer born 1983)', 24),
(1009, 'POR', 'Hélder Postiga', 36),
(1009, 'POR', 'Silvestre Varela', 87),
(1010, 'NED', 'Robin van Persie', 73),
(1010, 'GER', 'Mario Gómez', 24),
(1010, 'GER', 'Mario Gómez', 38),
(1011, 'POR', 'Cristiano Ronaldo', 28),
(1011, 'POR', 'Cristiano Ronaldo', 74),
(1011, 'NED', 'Rafael van der Vaart', 11),
(1012, 'DEN', 'Michael Krohn-Dehli', 24),
(1012, 'GER', 'Lukas Podolski', 19),
(1012, 'GER', 'Lars Bender', 80),
(1013, 'ESP', 'Cesc Fàbregas', 64),
(1013, 'ITA', 'Antonio Di Natale', 61),
(1014, 'IRL', 'Sean St Ledger', 19),
(1014, 'CRO', 'Mario Mandžukic', 3),
(1014, 'CRO', 'Mario Mandžukic', 49),
(1014, 'CRO', 'Nikica Jelavic', 43),
(1015, 'ITA', 'Andrea Pirlo', 39),
(1015, 'CRO', 'Mario Mandžukic', 72),
(1016, 'ESP', 'Fernando Torres', 4),
(1016, 'ESP', 'Fernando Torres', 70),
(1016, 'ESP', 'David Silva', 49),
(1016, 'ESP', 'Cesc Fàbregas', 83),
(1017, 'ESP', 'Jesús Navas', 88),
(1018, 'ITA', 'Antonio Cassano', 35),
(1018, 'ITA', 'Mario Balotelli', 90),
(1019, 'FRA', 'Samir Nasri', 39),
(1019, 'ENG', 'Joleon Lescott', 30),
(1020, 'UKR', 'Andriy Shevchenko', 55),
(1020, 'UKR', 'Andriy Shevchenko', 62),
(1020, 'SWE', 'Zlatan Ibrahimovic', 52),
(1021, 'FRA', 'Jérémy Ménez', 53),
(1021, 'FRA', 'Yohan Cabaye', 56),
(
    1022,
    'SWE',
    'Glen Johnson (English footballer)',
    49
  ),
(1022, 'SWE', 'Olof Mellberg', 59),
(1022, 'ENG', 'Andy Carroll', 23),
(1022, 'ENG', 'Theo Walcott', 64),
(1022, 'ENG', 'Danny Welbeck', 78),
(1023, 'ENG', 'Wayne Rooney', 48),
(1024, 'SWE', 'Zlatan Ibrahimovic', 54),
(1024, 'SWE', 'Sebastian Larsson', 90),
(1025, 'POR', 'Cristiano Ronaldo', 79),
(1026, 'GER', 'Philipp Lahm', 39),
(1026, 'GER', 'Sami Khedira', 61),
(1026, 'GER', 'Miroslav Klose', 68),
(1026, 'GER', 'Marco Reus', 74),
(1026, 'GRE', 'Georgios Samaras', 55),
(1026, 'GRE', 'Dimitris Salpingidis', 89),
(1027, 'ESP', 'Xabi Alonso', 19),
(1027, 'ESP', 'Xabi Alonso', 90),
(1030, 'GER', 'Mesut Özil', 90),
(1030, 'ITA', 'Mario Balotelli', 20),
(1030, 'ITA', 'Mario Balotelli', 36),
(1031, 'ESP', 'David Silva', 14),
(1031, 'ESP', 'Jordi Alba', 41),
(1031, 'ESP', 'Fernando Torres', 84),
(1031, 'ESP', 'Juan Mata', 88);
/*!40000 ALTER TABLE `goal` ENABLE KEYS */
;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */
;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */
;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */
;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
;
-- Dump completed on 2018-03-07 15:10:16