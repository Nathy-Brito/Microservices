import json
from pathlib import Path

class DatabaseService:
    def __init__(self, db_file="users.json"): # _init_ é o construtor. db_file recebe o nome do arquivo JSON onde os dados estão armazenados
        self.db_file = Path(db_file) #converte o nome do arquivo em um objeto Path p
        if not self.db_file.exists(): #aqui verifica se o arquivo json existe no disco
            self._initialize_db() #se o arquivo não existir chama o metodo que cria e inicializa ele
            
    def _initialize_db(self): #método inicializador do banco de dados
        with open(self.db_file, "w") as file: #abre o arquivo no modo escrita
            json.dump([], file) # inicia com uma lista vazia
            
    def read_users(self): #lê os usuarios
        with open(self.db_file, "r") as file: #abre o arquivo no mode de leitura
            return json.load(file) #lê o conteudo json e converte em estrutura de dadis Python (lista oou dicionario) e retorna essa lista
        
    def write_users(self, users): #escreve os usuarios
        with open(self.db_file, "w") as file: # abre o arquivo no mode de escrita
            json.dump(users, file, indent = 4) #grava a lista fornecida no json e organiza o json com identação (organização)