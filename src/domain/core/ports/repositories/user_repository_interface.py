from abc import ABC, abstractmethod

from domain.core.models import UserModel


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find(self, filter_query: dict) -> list[UserModel]:
        pass

    @abstractmethod
    def insert_one(self, user: UserModel) -> UserModel | dict:
        pass
