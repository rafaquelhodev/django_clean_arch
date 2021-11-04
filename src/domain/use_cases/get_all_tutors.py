from typing import List
from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository


class GetAllTutors:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo = tutor_repo

    def execute(self) -> List[Tutor]:
        tutors = self.__tutor_repo.get_all_tutors()
        return tutors
