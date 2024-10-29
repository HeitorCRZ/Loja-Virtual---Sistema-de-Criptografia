create database Biblioteca;
use Biblioteca;
CREATE TABLE Autores (
	Autor_ID int primary key,
	Nome varchar(50),
	Nacionalidade varchar(50)
);
INSERT INTO Autores (Autor_ID, Nome, Nacionalidade) VALUES
(1, 'Gabriel Garcia Marquez', 'Colombiana'),
(2, 'J.K. Rowling', 'Britânica'),
(3, 'Haruki Murakami', 'Japonesa');

CREATE TABLE Livros (
	Livro_ID int primary key,
	Titulo varchar(50),
	Ano_Publicação varchar(50),
    Autor_id int,
    foreign key(Autor_id) REFERENCES Autores(Autor_ID)
);
INSERT INTO Livros (Livro_ID, Titulo, Ano_Publicação, Autor_id) VALUES
(1, 'Cem Anos de Solidão', 1967, 1),
(2, 'Harry Potter e a Pedra Filosofal', 1997, 2),
(3, 'Kafka à Beira-Mar', 2002, 3);

CREATE TABLE Categorias (
	Categoria_ID int primary key,
	Nome_Categoria varchar(50)
);
INSERT INTO Categorias (Categoria_ID, Nome_Categoria) VALUES
(1, 'Ficção'),
(2, 'Fantasia'),
(3, 'Literatura Latino-Americana');

CREATE TABLE Usuarios (
	Usuario_ID int primary key,
	Nome_Usuario varchar(50),
	Email varchar(50)
);
INSERT INTO Usuarios (Usuario_ID, Nome_Usuario, Email) VALUES
(1, 'Ana Silva', 'ana.silva@example.com'),
(2, 'Bruno Dias', 'bruno.dias@example.com'),
(3, 'Carlos Souza', 'carlos.souza@example.com');

CREATE TABLE Livros_Categoria (
	ID_Categoria int ,
	ID_Livro int,
	foreign key(ID_Categoria) references Categorias(Categoria_ID),
    foreign key(ID_Livro) references Livros(Livro_ID)
);
INSERT INTO Livros_Categoria (ID_Livro, ID_Categoria) VALUES
(1, 3),
(2, 2),
(3, 1);

CREATE TABLE Emprestimos (
	Emprestimo_ID int primary key,
	ID_livro int,
    ID_usuario int,
	Data_Emprestimo varchar(50),
    Data_Devolução varchar(50),
    foreign key(ID_livro) references Livros(Livro_ID),
    foreign key(ID_usuario) references Usuarios(Usuario_ID)
);
INSERT INTO Emprestimos (Emprestimo_ID, ID_livro, ID_usuario,
Data_Emprestimo, Data_Devolução) VALUES
(1, 1, 1, '2023-01-10', '2023-01-24'),
(2, 2, 2, '2023-02-15', NULL),
(3, 3, 1, '2023-03-12', '2023-03-26');

SELECT Nome AS Autor, Titulo AS Livro FROM Autores, Livros WHERE Autores.Autor_ID = Livros.Autor_id;
SELECT Titulo AS Livro,'Não devolveu' AS Devolução FROM Emprestimos, Livros WHERE Data_Devolução IS NULL AND ID_livro = Livro_ID;
SELECT Titulo AS Livro,Nome_Categoria as Categoria FROM Categorias, Livros, Livros_Categoria WHERE Categoria_ID = 3  AND ID_Categoria = 3 AND Livro_ID = ID_Livro;
SELECT Nome AS Autor, count(Livros.Livro_ID) AS livros FROM Autores, Livros WHERE Autores.Autor_ID = Livros.Autor_id GROUP BY Nome;
SELECT DISTINCT Nome_Usuario AS Usuário FROM Emprestimos, Usuarios WHERE Usuario_ID = ID_usuario;
SELECT Titulo AS Livro, Ano_Publicação AS Publicação FROM Livros ORDER BY Ano_Publicação LIMIT 1;
SELECT Titulo AS Livro, Nome_Categoria AS Categoria FROM Livros, Categorias, Livros_Categoria WHERE ID_Categoria = Categoria_ID AND ID_Livro = Livro_ID;
SELECT Nome_Usuario AS Usuario, Nome_Categoria AS Categoria FROM Usuarios,Emprestimos,Categorias,Livros_Categoria WHERE Usuario_ID = ID_usuario AND Categoria_ID = ID_Categoria AND Livros_Categoria.ID_Livro = Emprestimos.ID_livro AND ID_Categoria = 3
SELECT Titulo AS Livro, Data_Emprestimo AS Emprestimo FROM Livros, Emprestimos WHERE Data_Emprestimo LIKE'2023%' AND ID_Livro = Livro_ID;
SELECT Nome AS Autor, Count(ID_livro) AS LivrosEmprestados FROM Livros, Emprestimos, Autores WHERE Livro_ID = ID_livro AND Autores.Autor_ID = Livros.autor_ID GROUP BY Nome;
SELECT Titulo AS Livros_Não_Emprestados FROM Livros, Emprestimos WHERE count(Livro_ID);




