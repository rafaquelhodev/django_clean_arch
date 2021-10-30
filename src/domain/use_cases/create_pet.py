from datetime import datetime
from domain.entities.tutor import Tutor

from domain.repository.PetRepository import PetRepository


class CreatePet:
    def __init__(self, pet_repo: PetRepository) -> None:
        self.__pet_repo: PetRepository = pet_repo

    def execute(
        self, name: str, tutor: Tutor, birth_date: datetime = None, breed: str = ""
    ) -> None:
        self.__pet_repo.create_pet(name, tutor, birth_date, breed)
