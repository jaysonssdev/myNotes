import pytest
from src.user_manager.main import UserManager


# define a pytest fixture to create a fresh instance of UserManager before each test
@pytest.fixture
def user_manager():
    return UserManager()


# test the 'add_user' function
def test_add_user(user_manager):
    # add a user
    user_manager.add_user("user1", "user1@example.com")
    # check that the user was added successfully
    assert user_manager.get_user("user1") == "user1@example.com"


# test the 'get_user' function
def test_get_user(user_manager):
    # add a user
    user_manager.add_user("user2", "user2@example.com")
    # check that we can retrieve the user correctly
    assert user_manager.get_user("user2") == "user2@example.com"
    # check that None is returned when a user does not exist
    assert user_manager.get_user("user3") is None
