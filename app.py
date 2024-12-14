from flask import Flask, jsonify, request #Flask é o frmaework usado para construir a API; jsonify converte objetos python (listas e dicionarios) em resposta JSON; request permite acessar dados enviados na requisição HTTP
from DatabaseService import DatabaseService #DatabaseService é a classe criada para gerenciar o banco de dados JSON

app = Flask(__name__) # cria uma instancia do flask
db_service = DatabaseService() #inicializa o serviço de banco de dados, e se não existir, cria

@app.route('/users', methods=['GET']) #essa é a rota HTTP
def get_users():
    users = db_service.read_users() #lê a lista de usuários do banco de dados JSON
    return jsonify(users), 200 #retorna a lista de usuários em formato JSON. o 200 é um status que define sucesso

@app.route('/users', methods=['POST']) #rota HTTP
def add_user():
    new_user = request.json #aqui obtém o corpo da requisição como por exemplo um dicionario JSON
    if not new_user.get('name') or not new_user.get('email'): #verifica se os campos (name e email) estão preenchidos 
        return jsonify({"error": "Nome e email são requisitados"}), 400 #retorna um erro caso os campos não estejam preenchidos
    
    users = db_service.read_users() # lê a lista de usuários
    new_user['id'] = len(users) + 1 # incrementa o id com base no numero de usuários existentes
    users.append(new_user) #adiciona um novo usuário na lista
    db_service.write_users(users) #atualiza o arquivo JSON com a lista de usuários
    return jsonify(new_user), 201 # retorna o usuario que foi criado em formato JSON com o código de status 201 que indica criação (created) 

#iniciação do servidor:
if __name__ == '__main__':
    app.run(debug=True)