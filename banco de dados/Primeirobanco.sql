USE primeirobanco
UPDATE Cadastro SET Telefone = "123-456-7890" WHERE ID_Cadastro = 3;
SELECT Telefone FROM Cadastro WHERE ID_Cadastro = 3;
INSERT INTO Cadastro VALUES (71,'Heitor','Cruz','heitorrcruz0608@gmail.com','12 99204-3112','2007-6-06');
DELETE FROM Cadastro WHERE ID_Cadastro =71;
SELECT * FROM Cadastro;
SELECT * FROM Cadastro WHERE Nome LIKE 'A%';
SELECT Data_Nascimento FROM Cadastro WHERE Data_Nascimento > '1990-01-10';
UPDATE Cadastro SET Sobrenome = 'Pereira' WHERE Nome = 'Ana';