from pytest import fixture

from domain.use_cases.create_tutor import CreateTutor
from domain.use_cases.get_tutor_by_id import GetTutorById
from infra.repository.TutorRepositoryMemory import TutorRepositoryMemory


class TestCreateTutor:
    @fixture
    def mock_uuid(self, mocker):
        mock_func = mocker.patch("uuid.uuid4")
        mock_func.return_value = "123-456"
        return mock_func

    def test_should_create_owner(self, mock_uuid):
        tutor_repo_memory = TutorRepositoryMemory()
        create_tutor = CreateTutor(tutor_repo_memory)

        create_tutor.execute("tutor name", "new_tutor@tutor.com")

        get_tutor = GetTutorById(tutor_repo_memory)
        tutor = get_tutor.execute("123-456")

        assert tutor.id == "123-456"
