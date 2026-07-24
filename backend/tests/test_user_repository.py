from backend.app.repositories.user_repository import UserRepository

def test_user_repository_exists():
    assert UserRepository is not None
