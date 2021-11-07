from django.shortcuts import render
from rest_framework.serializers import Serializer
from adapter.django_adapter import DjangoAdapter
from controller.tutor_controller import TutorController
from infra.repository.TutorRepositoryDjangoORM import TutorRepositoryDjangoORM
from infra.repository.TutorRepositoryMemory import TutorRepositoryMemory

# from django_project.app.api.serializer import TutorSerializer
from django_project.app.api.models import Tutor as TutorORM

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializer.tutor_serializer import TutorSerializer, MultipleTutorsSerializer


class TutorView(APIView):
    """
    List all tutor, or create a new tutor.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        tutor_repo = TutorRepositoryDjangoORM()
        self.__controller = TutorController(tutor_repo)

    def get(self, request, **kwargs):
        res = DjangoAdapter.create(
            self.__controller.get, request, MultipleTutorsSerializer, **kwargs
        )
        return res

    def post(self, request, **kwargs):
        res = DjangoAdapter.create(
            self.__controller.create_tutor, request, TutorSerializer, **kwargs
        )
        return res


class TutorDetailView(APIView):
    """
    Get information of a specific tutor
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        tutor_repo = TutorRepositoryDjangoORM()
        self.__controller = TutorController(tutor_repo)

    def get(self, request, **kwargs):
        res = DjangoAdapter.create(
            self.__controller.get_tutor_by_id, request, TutorSerializer, **kwargs
        )
        return res
