from domain.entities.tutor import Tutor


class MultipleTutorsSerializer:
    @staticmethod
    def serialize(tutors):
        return [TutorSerializer.serialize(tutor) for tutor in tutors]


class TutorSerializer:
    @staticmethod
    def serialize(tutor: Tutor):
        return {
            "id": str(tutor.id),
            "name": tutor.get_name(),
            "email": tutor.get_email(),
        }
