CREATE SCHEMA IF NOT EXISTS eventos_mma;
USE eventos_mma;
SET SQL_SAFE_UPDATES = 0;



CREATE TABLE IF NOT EXISTS Academia(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Categoria(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
limite_peso DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Lutador(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
id_academia INTEGER NOT NULL,
id_categoria INTEGER NOT NULL,
nome VARCHAR(100) NOT NULL,
altura FLOAT NOT NULL,
envergaura FLOAT NOT NULL,
tem_luta_marcada BOOL NOT NULL,
posicao_ranking INTEGER,
FOREIGN KEY (id_academia) REFERENCES Academia(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE,
FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS Card(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
data_evento DATE
);


CREATE TABLE IF NOT EXISTS Arbitro(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
altura FLOAT NOT NULL,
limite_peso DECIMAL(5, 2) NOT NULL,
numero_doc VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Luta(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
numero_rounds INTEGER NOT NULL,
id_arbitro INTEGER NOT NULL,
id_card INTEGER NOT NULL,
FOREIGN KEY (id_arbitro) REFERENCES Arbitro(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE,
FOREIGN KEY (id_card) REFERENCES Card(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Participa(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
id_lutador INTEGER NOT NULL,
id_luta INTEGER NOT NULL,
FOREIGN KEY (id_lutador) REFERENCES Lutador(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE,
FOREIGN KEY (id_luta) REFERENCES Luta(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Juiz(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
numero_doc VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS julga(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
id_juiz INTEGER NOT NULL,
id_luta INTEGER NOT NULL,
pontuacao VARCHAR(10),
FOREIGN KEY (id_juiz) REFERENCES Juiz(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE,
FOREIGN KEY (id_luta) REFERENCES Luta(id)
 ON UPDATE CASCADE
 ON DELETE CASCADE
);

USE eventos_mma;

-- Populando Academia (15 registros)
INSERT INTO Academia (nome) VALUES 
('American Top Team'),
('Jackson Wink MMA Academy'),
('Tiger Muay Thai'),
('Chute Boxe'),
('Nova União'),
('Alliance MMA'),
('Tristar Gym'),
('AKA (American Kickboxing Academy'),
('Kings MMA'),
('City Kickboxing'),
('Evolve MMA'),
('Gracie Barra'),
('Team Alpha Male'),
('Xtreme Couture'),
('American Kickboxing');

-- Populando Categoria (10 registros)
INSERT INTO Categoria (nome, limite_peso) VALUES 
('Peso Palha', 52.16),
('Peso Mosca', 56.70),
('Peso Galo', 61.23),
('Peso Pena', 65.77),
('Peso Leve', 70.31),
('Peso Meio-Médio', 77.11),
('Peso Médio', 83.91),
('Peso Meio-Pesado', 93.00),
('Peso Pesado', 120.20),
('Super Pesado', 265.00);

-- Populando Lutador (15 registros)
INSERT INTO Lutador (id_academia, id_categoria, nome, altura, envergaura, tem_luta_marcada, posicao_ranking) VALUES 
(1, 5, 'Anderson Silva Jr', 1.83, 1.88, TRUE, 3),
(2, 6, 'Carlos Mendes', 1.78, 1.85, TRUE, 5),
(3, 4, 'Thiago Santos', 1.75, 1.80, FALSE, 8),
(4, 7, 'Rafael Costa', 1.85, 1.90, TRUE, 2),
(5, 5, 'José Aldo Filho', 1.70, 1.75, TRUE, 1),
(6, 8, 'Marcus Vieira', 1.88, 1.95, FALSE, 10),
(7, 6, 'Jean Pierre', 1.80, 1.83, TRUE, 4),
(8, 9, 'Fabricio Lima', 1.93, 2.00, FALSE, 7),
(9, 3, 'Pedro Souza', 1.68, 1.73, TRUE, 6),
(10, 4, 'Daniel Kim', 1.73, 1.78, FALSE, 12),
(11, 5, 'Roberto Oliveira', 1.77, 1.82, TRUE, 9),
(12, 7, 'Gabriel Ferreira', 1.83, 1.87, FALSE, 15),
(13, 2, 'Felipe Moraes', 1.65, 1.70, TRUE, 11),
(14, 6, 'Lucas Barbosa', 1.79, 1.84, TRUE, 14),
(15, 8, 'Bruno Almeida', 1.87, 1.93, FALSE, 13);

-- Populando Card (12 registros)
INSERT INTO Card (nome, data_evento) VALUES 
('UFC Fight Night: Brasil', '2025-01-15'),
('Bellator 320', '2025-02-20'),
('UFC 315: Championship Edition', '2025-03-10'),
('ONE Championship: Warriors', '2025-04-05'),
('PFL Finals 2025', '2025-05-18'),
('UFC Fight Night: Vegas 90', '2025-06-22'),
('Bellator: Europa', '2025-07-14'),
('UFC 320: Summer Showdown', '2025-08-12'),
('Cage Warriors 180', '2025-09-07'),
('UFC Fight Night: Asia', '2025-10-25'),
('Bellator 325: Grand Prix', '2025-11-16'),
('UFC 325: Year End Spectacular', '2025-12-30');

-- Populando Arbitro (12 registros)
INSERT INTO Arbitro (nome, altura, limite_peso, numero_doc) VALUES 
('Marc Goddard', 1.82, 95.00, 'ARB-2024-001'),
('Herb Dean', 1.85, 88.50, 'ARB-2024-002'),
('John McCarthy', 1.80, 92.00, 'ARB-2024-003'),
('Jason Herzog', 1.78, 85.00, 'ARB-2024-004'),
('Keith Peterson', 1.75, 87.50, 'ARB-2024-005'),
('Dan Miragliotta', 1.88, 98.00, 'ARB-2024-006'),
('Mike Beltran', 1.73, 90.00, 'ARB-2024-007'),
('Chris Tognoni', 1.80, 86.00, 'ARB-2024-008'),
('Mark Smith', 1.83, 91.00, 'ARB-2024-009'),
('Frank Trigg', 1.77, 84.50, 'ARB-2024-010'),
('Mario Yamasaki', 1.76, 83.00, 'ARB-2024-011'),
('Yves Lavigne', 1.79, 89.00, 'ARB-2024-012');

-- Populando Luta (15 registros)
INSERT INTO Luta (numero_rounds, id_arbitro, id_card) VALUES 
(3, 1, 1),
(5, 2, 1),
(3, 3, 2),
(3, 4, 3),
(5, 5, 3),
(3, 6, 4),
(3, 7, 5),
(5, 8, 6),
(3, 9, 7),
(3, 10, 8),
(5, 11, 9),
(3, 12, 10),
(3, 1, 11),
(5, 2, 12),
(3, 3, 12);

-- Populando Participa (30 registros - 2 lutadores por luta)
INSERT INTO Participa (id_lutador, id_luta) VALUES 
(1, 1), (2, 1),
(3, 2), (4, 2),
(5, 3), (6, 3),
(7, 4), (8, 4),
(9, 5), (10, 5),
(11, 6), (12, 6),
(13, 7), (14, 7),
(15, 8), (1, 8),
(2, 9), (3, 9),
(4, 10), (5, 10),
(6, 11), (7, 11),
(8, 12), (9, 12),
(10, 13), (11, 13),
(12, 14), (13, 14),
(14, 15), (15, 15);

-- Populando Juiz (12 registros)
INSERT INTO Juiz (nome, numero_doc) VALUES 
('Douglas Crosby', 'JUI-2024-001'),
('Sal D\'Amato', 'JUI-2024-002'),
('Derek Cleary', 'JUI-2024-003'),
('Chris Lee', 'JUI-2024-004'),
('Dave Tirelli', 'JUI-2024-005'),
('Ron McCarthy', 'JUI-2024-006'),
('Tony Weeks', 'JUI-2024-007'),
('Junichiro Kamijo', 'JUI-2024-008'),
('Eric Colon', 'JUI-2024-009'),
('Glenn Trowbridge', 'JUI-2024-010'),
('Jeff Mullen', 'JUI-2024-011'),
('Marcos Rosales', 'JUI-2024-012');

-- Populando julga (45 registros - 3 juízes por luta)
INSERT INTO julga (id_juiz, id_luta, pontuacao) VALUES 
(1, 1, '29-28'), (2, 1, '30-27'), (3, 1, '29-28'),
(4, 2, '48-47'), (5, 2, '49-46'), (6, 2, '48-47'),
(7, 3, '30-27'), (8, 3, '29-28'), (9, 3, '30-27'),
(10, 4, '28-29'), (11, 4, '28-29'), (12, 4, '27-30'),
(1, 5, '49-46'), (2, 5, '48-47'), (3, 5, '50-45'),
(4, 6, '30-26'), (5, 6, '30-27'), (6, 6, '29-28'),
(7, 7, '29-28'), (8, 7, '29-28'), (9, 7, '30-27'),
(10, 8, '47-48'), (11, 8, '48-47'), (12, 8, '49-46'),
(1, 9, '30-27'), (2, 9, '30-27'), (3, 9, '29-28'),
(4, 10, '28-29'), (5, 10, '29-28'), (6, 10, '29-28'),
(7, 11, '50-45'), (8, 11, '49-46'), (9, 11, '48-47'),
(10, 12, '30-27'), (11, 12, '30-27'), (12, 12, '29-28'),
(1, 13, '29-28'), (2, 13, '30-27'), (3, 13, '29-28'),
(4, 14, '48-47'), (5, 14, '49-46'), (6, 14, '48-47'),
(7, 15, '30-27'), (8, 15, '30-27'), (9, 15, '29-28');
