import pytest
from service.library import Library
from service.runner import Runner


@pytest.fixture
def library():
    return Library(storage_file="data/test_library.json")


@pytest.fixture
def runner():
    """Создает экземпляр Runner для тестов."""
    return Runner()
