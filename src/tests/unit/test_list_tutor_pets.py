from pytest import fixture
from datetime import date

from domain.entities.pet import Pet
from domain.use_cases.create_pet import CreatePet

from domain.use_cases.create_tutor import CreateTutor
from domain.use_cases.get_tutor_by_email import GetTutorByEmail
from domain.use_cases.list_tutor_pets import ListTutorPets
from infra.repository.PetRepositoryMemory import PetRepositoryMemory
from infra.repository.TutorRepositoryMemory import TutorRepositoryMemory


class TestCreatePet:
    # @fixture
    # def mock_uuid(self, mocker):
    #     mock_uuid = mocker.patch("uuid.uuid4")
    #     mock_uuid.side_effect = ["123-456", "789-101"]
    #     return mock_uuid

    def test_should_list_tutor_pets(self):
        tutor_repo_memory = TutorRepositoryMemory()
        create_tutor = CreateTutor(tutor_repo_memory)

        create_tutor.execute("Jack_tutor", "jack@tutor.com")
        create_tutor.execute("Maria_tutor", "maria@tutor.com")
        get_tutor = GetTutorByEmail(tutor_repo_memory)
        jack_tutor = get_tutor.execute("jack@tutor.com")

        pet_repo_memory = PetRepositoryMemory()
        create_pet = CreatePet(pet_repo_memory)
        create_pet.execute("Bob", jack_tutor, date(2021, 12, 31), "York")
        create_pet.execute("Alice", jack_tutor, date(2020, 12, 31), "Poodle")

        list_tutor_pets = ListTutorPets(pet_repo_memory)

        jack_pets = list_tutor_pets.execute("jack@tutor.com")

        assert len(jack_pets) == 2
