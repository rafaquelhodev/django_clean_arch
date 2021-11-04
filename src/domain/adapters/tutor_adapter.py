from domain.entities.tutor import Tutor


class TutorAdapter:
    @staticmethod
    def create(id: str, name: str, email: str) -> Tutor:
        return Tutor(id, name, email)
