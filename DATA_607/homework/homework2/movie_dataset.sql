CREATE SCHEMA `movies` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE `movies`.`ratings` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`movie` VARCHAR(255) NOT NULL,
    `reviewer` VARCHAR(255) NOT NULL,
    `ratings` INT UNSIGNED NOT NULL,    
    PRIMARY KEY (`id`)
);

INSERT INTO `movies`.`ratings` 
	(`movie`, `reviewer`, `ratings`)
VALUES
 ('The Social Delimma', 'Kenan', 4),
 ('The Social Delimma', 'Barbie', 4),
 ('The Social Delimma', 'Prince', 4),
 ('The Social Delimma', 'Fay', 4),
 ('The Social Delimma', 'Kelly', 4),
 ('Death To 2020', 'Kenan', 4),
 ('Death To 2020', 'Barbie', 4),
 ('Death To 2020', 'Prince', 4),
 ('Death To 2020', 'Fay', 3),
 ('Death To 2020', 'Kelly', 3),
 ('The Queens Gambit', 'Kenan', 5),
 ('The Queens Gambit', 'Barbie', 4),
 ('The Queens Gambit', 'Prince', 4),
 ('The Queens Gambit', 'Fay', 4),
 ('The Queens Gambit', 'Kelly', 4),
 ('The Dictator', 'Kenan', 3),
 ('The Dictator', 'Barbie', 4),
 ('The Dictator', 'Prince', 5),
 ('The Dictator', 'Fay', 3),
 ('The Dictator', 'Kelly', 4);
