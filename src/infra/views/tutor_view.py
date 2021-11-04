from controller.tutor_controller import TutorController
from domain.repository.TutorRepository import TutorRepository


class TutorView:
    def __init__(self, tutor_repo: TutorRepository, tutor_serializer) -> None:
        self.__controller = TutorController(tutor_repo)
        self.__tutor_serializer = tutor_serializer

    def get(self):
        tutors = self.__controller.get_all_tutors()

        tutors_parsed = [
            TutorORM(id=tutor.id, name=tutor.get_name(), email=tutor.get_email())
            for tutor in tutors
        ]
        serializer = TutorSerializer(tutors_parsed, many=True)
        return Response(serializer.data)
