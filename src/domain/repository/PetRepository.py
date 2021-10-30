from abc import ABC, abstractmethod
from datetime import date
from typing import List

from domain.entities.pet import Pet
from domain.entities.tutor import Tutor


class PetRepository(ABC):
    @abstractmethod
    def create_pet(self, name: str, tutor: Tutor, birth_date: date, breed: str) -> None:
        """Create new pet"""

    @abstractmethod
    def get_pet_by_id(self, pet_id: str) -> Pet:
        """Get pet by id"""

    @abstractmethod
    def get_pets_by_tutor_email(self, tutor_email: str) -> List[Pet]:
        """Get pets by tutor email"""
