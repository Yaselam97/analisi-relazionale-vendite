-- Tabella clienti
CREATE TABLE clienti (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
);

INSERT INTO clienti (nome, email) VALUES
('Mario Rossi', 'mario.rossi@gmail.com'),
('Giulia Bianchi', 'giulia.bianchi@gmail.com'),
('Luca Verdi', 'luca.verdi@gmail.com'),
('Anna Neri', 'anna.neri@gmail.com'),
('Marco Gialli', 'marco.gialli@gmail.com');

-- Tabella vendite (con cliente_id)
CREATE TABLE vendite (
    id INTEGER PRIMARY KEY,
    data DATE,
    prodotto TEXT,
    quantità INTEGER,
    prezzo_unitario REAL,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clienti(id)
);

INSERT INTO vendite (data, prodotto, quantità, prezzo_unitario, cliente_id) VALUES
('2025-05-01', 'Latte', 2, 1.20, 1),
('2025-05-02', 'Uova', 4, 2.50, 2),
('2025-05-03', 'Pane', 1, 0.80, 3),
('2025-05-04', 'Latte', 3, 1.20, 4),
('2025-05-05', 'Yogurt', 5, 2.00, 5),
('2025-05-06', 'Formaggio', 2, 3.50, 1),
('2025-05-07', 'Burro', 1, 4.00, 2),
('2025-05-08', 'Pasta', 6, 1.50, 3),
('2025-05-09', 'Riso', 2, 2.00, 4),
('2025-05-10', 'Olio', 1, 5.00, 5);

