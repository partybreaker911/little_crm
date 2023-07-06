import pytest

from apps.accounts.models import CustomUser

# from mono_integration.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


# @pytest.fixture
# def user(db) -> User:
#     return UserFactory()
