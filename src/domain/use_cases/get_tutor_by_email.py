from typing import Type
from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository


class GetTutorByEmail:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo = tutor_repo

    def execute(self, tutor_email: str) -> Tutor:
        tutor = self.__tutor_repo.get_tutor_by_email(tutor_email)
        return tutor
