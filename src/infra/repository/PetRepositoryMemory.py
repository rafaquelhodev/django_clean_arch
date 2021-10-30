import uuid
from datetime import date
from typing import List, Type
from domain.entities.tutor import Tutor
from domain.entities.pet import Pet
from domain.repository.PetRepository import PetRepository


class PetRepositoryMemory(PetRepository):
    def __init__(self) -> None:
        self.__pets: List[Pet] = [
            Pet(
                "123456",
                "bob",
                date(2021, 10, 1),
                "York",
                Tutor("123-456-789", "Maria", "maria@tutor.com"),
            ),
            Pet(
                "223456",
                "trix",
                date(2019, 10, 1),
                "Poodle",
                Tutor("123-456-789", "Maria", "maria@tutor.com"),
            ),
        ]

    def create_pet(self, name: str, tutor: Tutor, birth_date: date, breed: str) -> None:
        new_pet = Pet(uuid.uuid4(), name, birth_date, breed, tutor)
        self.__pets.append(new_pet)

    def get_pet_by_id(self, pet_id: str) -> Pet:
        pet = [pet for pet in self.__pets if pet.id == pet_id]

        if not pet:
            raise Exception("Pet not found")

        return pet[0]

    def get_pets_by_tutor_email(self, tutor_email: str) -> List[Pet]:
        pets = [pet for pet in self.__pets if pet.get_tutor_email() == tutor_email]
        return pets
