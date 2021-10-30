from typing import Type
from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository


class GetTutorById:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo = tutor_repo

    def execute(self, tutor_id: str) -> Tutor:
        tutor = self.__tutor_repo.get_tutor_by_id(tutor_id=tutor_id)
        return tutor
