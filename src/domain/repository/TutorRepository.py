from abc import ABC, abstractmethod
from typing import Type, List

from domain.entities.tutor import Tutor
from domain.entities.pet import Pet


class TutorRepository(ABC):
    @abstractmethod
    def create_tutor(self, name: str, email: str) -> None:
        """Create new tutor"""

    @abstractmethod
    def get_tutor_by_id(self, tutor_id: str) -> Tutor:
        """Get tutor by id"""

    @abstractmethod
    def get_tutor_by_email(self, tutor_email: str) -> Tutor:
        """Get tutor by email"""
