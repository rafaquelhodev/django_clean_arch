from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository
from domain.use_cases.get_all_tutors import GetAllTutors
from domain.use_cases.get_tutor_by_id import GetTutorById
from domain.use_cases.create_tutor import CreateTutor


class TutorController:
    def __init__(self, tutor_repo: TutorRepository) -> None:
        self.__tutor_repo = tutor_repo

    def create_tutor(self, request, serializer, **kwargs) -> Tutor:
        create_tutor = CreateTutor(self.__tutor_repo)
        new_tutor = create_tutor.execute(request["name"], request["email"])
        res_new_tutor = serializer.serialize(new_tutor)
        return res_new_tutor, 200

    def get(self, request, serializer, **kwargs):
        try:
            get_tutors = GetAllTutors(self.__tutor_repo)
            tutors = get_tutors.execute()
            res_tutors = serializer.serialize(tutors)
            return res_tutors, 200
        except:
            # TODO create error class
            return {"Error": "Error getting tutor"}

    def get_tutor_by_id(self, request, serializer, **kwargs):
        try:
            get_tutor = GetTutorById(self.__tutor_repo)
            tutor = get_tutor.execute(kwargs["pk"])
            res_tutor = serializer.serialize(tutor)
            return res_tutor, 200
        except:
            # TODO create error class
            return {"Error": "Error getting tutor"}
