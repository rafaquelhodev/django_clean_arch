import uuid
from typing import List, Type
from domain.entities.tutor import Tutor
from domain.entities.pet import Pet
from domain.repository.TutorRepository import TutorRepository


class TutorRepositoryMemory(TutorRepository):
    def __init__(self) -> None:
        self.__tutors: List[Tutor] = [
            Tutor("1234", "Joao", "joao@tutor"),
            Tutor("5678", "Maria", "maria@tutor"),
        ]

    def create_tutor(self, name: str, email: str) -> None:
        new_tutor = Tutor(uuid.uuid4(), name, email)
        self.__tutors.append(new_tutor)

    def get_tutor_by_id(self, tutor_id: str) -> Tutor:
        tutor = [tutor for tutor in self.__tutors if tutor.id == tutor_id]

        if not tutor:
            raise Exception("Tutor not found")

        return tutor[0]

    def get_tutor_by_email(self, tutor_email: str) -> Tutor:
        tutor = [tutor for tutor in self.__tutors if tutor.get_email() == tutor_email]

        if not tutor:
            raise Exception("Tutor not found")

        return tutor[0]
