-- Criação da tabela "Clientes"
CREATE TABLE Clientes (
  ID INT PRIMARY KEY,
  Nome VARCHAR(100),
  Email VARCHAR(100),
  Telefone VARCHAR(20),
  Endereco VARCHAR(200)
);

-- Criação da tabela "Seguros"
CREATE TABLE Seguros (
  ID INT PRIMARY KEY,
  ID_cliente INT,
  Modelo_celular VARCHAR(100),
  Tipo_seguro VARCHAR(20),
  Preco DECIMAL(10, 2),
  Data_contrato DATE,
  FOREIGN KEY (ID_cliente) REFERENCES Clientes(ID)
);
