from pytest import fixture
from datetime import date

from domain.entities.pet import Pet
from domain.use_cases.create_pet import CreatePet

from domain.use_cases.create_tutor import CreateTutor
from domain.use_cases.get_tutor_by_id import GetTutorById
from infra.repository.PetRepositoryMemory import PetRepositoryMemory
from infra.repository.TutorRepositoryMemory import TutorRepositoryMemory


class TestCreatePet:
    @fixture
    def mock_uuid(self, mocker):
        mock_uuid = mocker.patch("uuid.uuid4")
        mock_uuid.side_effect = ["123-456", "789-101"]
        return mock_uuid

    def test_should_create_pet(self, mock_uuid):
        tutor_repo_memory = TutorRepositoryMemory()
        create_tutor = CreateTutor(tutor_repo_memory)

        create_tutor.execute("tutor name", "tutor@tutor.com")
        get_tutor = GetTutorById(tutor_repo_memory)
        tutor = get_tutor.execute("123-456")

        pet_repo_memory = PetRepositoryMemory()
        create_pet = CreatePet(pet_repo_memory)
        create_pet.execute("bob", tutor, date(2021, 12, 31), "York")

        new_pet = pet_repo_memory.get_pet_by_id("789-101")

        assert new_pet.id == "789-101"
