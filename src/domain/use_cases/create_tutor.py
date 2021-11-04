from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository


class CreateTutor:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo: TutorRepository = tutor_repo

    def execute(self, name: str, email: str) -> Tutor:
        return self.__tutor_repo.create_tutor(name, email)
