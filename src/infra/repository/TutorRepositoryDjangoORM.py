from typing import List

from domain.entities.tutor import Tutor
from domain.repository.TutorRepository import TutorRepository
from domain.adapters.tutor_adapter import TutorAdapter

from django_project.app.api.models import Tutor as TutorORM


class TutorRepositoryDjangoORM(TutorRepository):
    def create_tutor(self, name: str, email: str) -> Tutor:
        tutor = TutorORM.objects.create(name=name, email=email)
        return TutorAdapter.create(tutor.id, tutor.name, tutor.email)

    def get_all_tutors(self) -> List[Tutor]:
        tutorsORM = TutorORM.objects.all()

        tutors = [
            TutorAdapter.create(tutor.id, tutor.name, tutor.email)
            for tutor in tutorsORM
        ]
        return tutors

    def get_tutor_by_id(self, tutor_id: str) -> Tutor:
        tutor = TutorORM.objects.filter(id=tutor_id).first()
        return TutorAdapter.create(tutor.id, tutor.name, tutor.email)

    def get_tutor_by_email(self, tutor_email: str) -> Tutor:
        tutor = TutorORM.objects.filter(email=tutor_email).first()
        return TutorAdapter.create(tutor.id, tutor.name, tutor.email)
