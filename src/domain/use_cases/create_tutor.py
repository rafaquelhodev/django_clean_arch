from domain.entities.pet import Pet
from domain.repository.TutorRepository import TutorRepository


class CreateTutor:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo: TutorRepository = tutor_repo

    def execute(self, name: str, email: str) -> None:
        self.__tutor_repo.create_tutor(name, email)
