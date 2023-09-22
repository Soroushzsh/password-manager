import os

import pytest

from database import Database

# Define a fixture to create a temporary SQLite database for testing
@pytest.fixture
def test_db():
    test_db_name = 'test_database.db'
    db = Database(test_db_name)
    yield db
    db.__del__()  # Close the database connection
    os.remove(test_db_name)  # Remove the temporary database file


# Test the insert method
def test_insert(test_db):
    test_db.insert("Service 1", "User 1", "Password 1")
    result = test_db.retrieve_all_services()
    assert len(result) == 1
    assert result[0][1] == "Service 1"
    assert result[0][2] == "User 1"


# Test the update method
def test_update(test_db):
    test_db.insert("Service 1", "User 1", "Password 1")
    service_id = test_db.retrieve_all_services()[0][0]
    test_db.update(service_id, "Service 2", "User 2", "Password 2")
    updated_service = test_db.retrieve_service_by_id(service_id)
    assert updated_service[0] == "Service 2"
    assert updated_service[1] == "User 2"
    assert updated_service[2] == "Password 2"


# Test the delete method
def test_delete(test_db):
    test_db.insert("Service 1", "User 1", "Password 1")
    service_id = test_db.retrieve_all_services()[0][0]
    test_db.delete(service_id)
    result = test_db.retrieve_all_services()
    assert len(result) == 0


# Test the retrieve_by_service_name method
def test_retrieve_by_service_name(test_db):
    test_db.insert("Service 1", "User 1", "Password 1")
    result = test_db.retrieve_by_service_name("Service 1")
    assert len(result) == 1
    assert result[0][1] == "Service 1"
    assert result[0][2] == "User 1"


# Test the retrieve_by_id method
def test_retrieve_by_id(test_db):
    test_db.insert("Email", "user@example.com", "mypassword")
    service = test_db.retrieve_service_by_id(1)
    assert service[0] == "Email"


# Test the count method
def test_count(test_db):
    test_db.insert("Service 1", "User 1", "Password 1")
    test_db.insert("Service 2", "User 2", "Password 2")
    count = test_db.count(service_name="Service 1")
    assert count == 1
