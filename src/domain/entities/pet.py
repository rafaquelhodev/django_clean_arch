from datetime import datetime

from domain.entities.tutor import Tutor


class Pet:
    def __init__(
        self, id: str, name: str, birth_date: datetime, breed: str, tutor: Tutor
    ) -> None:
        self.id = id
        self.__name = name
        self.__birth_date = birth_date
        self.__tutor = tutor
        self.__breed = breed

        self.__validate_pet()

    def get_tutor_email(self):
        return self.__tutor.get_email()

    def __validate_pet(self):
        if self.__name == "":
            raise Exception("A pet must have a name")

        if not self.__tutor:
            raise Exception("A pet must have a tutor")

        return
