from domain.core.models.user import UserModel
from domain.core.ports import UserRepositoryInterface
from domain.core.use_cases import UserHandlerInterface


class UserHandler(UserHandlerInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def find(self, filter_query: dict) -> list[UserModel]:
        return self.user_repository.find(filter_query=filter_query)

    def insert_one(self, user: UserModel) -> UserModel | dict:
        return self.user_repository.insert_one(user)
