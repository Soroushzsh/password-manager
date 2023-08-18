import pytest
from database import Database

# Fixture to create a temporary database for testing
@pytest.fixture
def temp_db():
    db = Database(":memory:")  # Use in-memory database for testing
    yield db
    db.__del__()  # Clean up the database connection

def test_insert_and_retrieve(temp_db):
    temp_db.insert_service("Email", "user@example.com", "mypassword")
    services = temp_db.retrieve_all_services()
    assert len(services) == 1
    assert services[0][1] == "Email"

def test_update_and_retrieve(temp_db):
    temp_db.insert_service("Email", "user@example.com", "mypassword")
    temp_db.update_service(1, "New Email", "newuser@example.com", "newpassword")
    service = temp_db.retrieve_by_id(1)
    assert service[1] == "New Email"
    assert service[2] == "newuser@example.com"
    assert service[3] == "newpassword"

def test_delete(temp_db):
    temp_db.insert_service("Email", "user@example.com", "mypassword")
    temp_db.delete_service(1)
    services = temp_db.retrieve_all_services()
    assert len(services) == 0

def test_retrieve_by_service_name(temp_db):
    temp_db.insert_service("Email", "user@example.com", "mypassword")
    temp_db.insert_service("Social Media", "myusername", "mysecretpassword")
    services = temp_db.retrieve_by_service_name("Email")
    assert len(services) == 1
    assert services[0][1] == "Email"

def test_retrieve_by_id(temp_db):
    temp_db.insert_service("Email", "user@example.com", "mypassword")
    service = temp_db.retrieve_by_id(1)
    assert service[1] == "Email"

if __name__ == "__main__":
    pytest.main()
