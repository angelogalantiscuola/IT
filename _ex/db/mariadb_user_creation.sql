CREATE USER 'amati'@'localhost' IDENTIFIED BY 'amati';
GRANT ALL PRIVILEGES ON `amati\_%`.* TO 'amati'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'amati'@'localhost';

CREATE USER 'baffert'@'localhost' IDENTIFIED BY 'baffert';
GRANT ALL PRIVILEGES ON `baffert\_%`.* TO 'baffert'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'baffert'@'localhost';

CREATE USER 'chiarabini'@'localhost' IDENTIFIED BY 'chiarabini';
GRANT ALL PRIVILEGES ON `chiarabini\_%`.* TO 'chiarabini'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'chiarabini'@'localhost';

CREATE USER 'ciaramidaro'@'localhost' IDENTIFIED BY 'ciaramidaro';
GRANT ALL PRIVILEGES ON `ciaramidaro\_%`.* TO 'ciaramidaro'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'ciaramidaro'@'localhost';

CREATE USER 'cornacchia'@'localhost' IDENTIFIED BY 'cornacchia';
GRANT ALL PRIVILEGES ON `cornacchia\_%`.* TO 'cornacchia'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'cornacchia'@'localhost';

CREATE USER 'delia'@'localhost' IDENTIFIED BY 'delia';
GRANT ALL PRIVILEGES ON `delia\_%`.* TO 'delia'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'delia'@'localhost';

CREATE USER 'franci'@'localhost' IDENTIFIED BY 'franci';
GRANT ALL PRIVILEGES ON `franci\_%`.* TO 'franci'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'lupafranciscu'@'localhost';

CREATE USER 'lupascu'@'localhost' IDENTIFIED BY 'lupascu';
GRANT ALL PRIVILEGES ON `lupascu\_%`.* TO 'lupascu'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'lupascu'@'localhost';

CREATE USER 'maccione'@'localhost' IDENTIFIED BY 'maccione';
GRANT ALL PRIVILEGES ON `maccione\_%`.* TO 'maccione'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'maccione'@'localhost';

CREATE USER 'pelusi'@'localhost' IDENTIFIED BY 'pelusi';
GRANT ALL PRIVILEGES ON `pelusi\_%`.* TO 'pelusi'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'pelusi'@'localhost';

CREATE USER 'savioli'@'localhost' IDENTIFIED BY 'savioli';
GRANT ALL PRIVILEGES ON `savioli\_%`.* TO 'savioli'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'savioli'@'localhost';

CREATE USER 'sejdi'@'localhost' IDENTIFIED BY 'sejdi';
GRANT ALL PRIVILEGES ON `sejdi\_%`.* TO 'sejdi'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'sejdi'@'localhost';

CREATE USER 'serra'@'localhost' IDENTIFIED BY 'serra';
GRANT ALL PRIVILEGES ON `serra\_%`.* TO 'serra'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'serra'@'localhost';

CREATE USER 'tamburini'@'localhost' IDENTIFIED BY 'tamburini';
GRANT ALL PRIVILEGES ON `tamburini\_%`.* TO 'tamburini'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'tamburini'@'localhost';

CREATE USER 'tonelli'@'localhost' IDENTIFIED BY 'tonelli';
GRANT ALL PRIVILEGES ON `tonelli\_%`.* TO 'tonelli'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'tonelli'@'localhost';

CREATE USER 'uva'@'localhost' IDENTIFIED BY 'uva';
GRANT ALL PRIVILEGES ON `uva\_%`.* TO 'uva'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *.* TO 'uva'@'localhost';

FLUSH PRIVILEGES;