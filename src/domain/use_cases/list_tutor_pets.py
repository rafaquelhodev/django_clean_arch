from typing import List
from domain.entities.pet import Pet
from domain.repository.PetRepository import PetRepository
from domain.repository.TutorRepository import TutorRepository


class ListTutorPets:
    def __init__(self, pet_repo: PetRepository) -> None:
        self.__pet_repo = pet_repo

    def execute(self, tutor_email: str) -> List[Pet]:
        return self.__pet_repo.get_pets_by_tutor_email(tutor_email)
