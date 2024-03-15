import json

from domain.core.models import UserModel
from domain.core.ports import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def find(self, filter_query: dict) -> list[UserModel]:
        with open("domain/infra/usuarios.json", "r") as file:
            users = json.load(file)

        users_filtrados = []
        for user in users:
            # Verifica se todos os critérios de filtro são atendidos
            if all(user[key] == value for key, value in filter_query.items()):
                users_filtrados.append(user)

        return users_filtrados

    def insert_one(self, user: UserModel) -> UserModel | dict:
        try:
            with open("domain/infra/usuarios.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            # Se o arquivo não existir, criar uma lista vazia
            users = []

        # Adicionar o novo usuário à lista de usuários
        users.append(user)

        try:
            with open("domain/infra/usuarios.json", "w") as arquivo:
                json.dump(users, arquivo, indent=4)
            return user
        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")
            return {}
