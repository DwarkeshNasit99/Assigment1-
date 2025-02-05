import unittest
from unittest.mock import MagicMock
from user import Database, UserService

class TestUserService(unittest.TestCase):
    
    def setUp(self):
        self.mock_db = MagicMock()
        self.user_service = UserService(self.mock_db)

    def test_create_user(self):
        self.mock_db.insert_user.return_value = 1
        response, status_code = self.user_service.create_user("Alice", 25)
        self.assertEqual(response, {"user_id": 1, "name": "Alice", "age": 25})
        self.assertEqual(status_code, 201)

    def test_get_user_found(self):
        self.mock_db.get_user.return_value = (1, "Alice", 25)
        response, status_code = self.user_service.get_user(1)
        self.assertEqual(response, {"user_id": 1, "name": "Alice", "age": 25})
        self.assertEqual(status_code, 200)

    def test_get_user_not_found(self):
        self.mock_db.get_user.return_value = None
        response, status_code = self.user_service.get_user(2)
        self.assertEqual(response, {"error": "User not found"})
        self.assertEqual(status_code, 404)

    def test_update_user_success(self):
        self.mock_db.update_user.return_value = 1
        response, status_code = self.user_service.update_user(1, "Bob", 30)
        self.assertEqual(response, {"message": "User updated successfully"})
        self.assertEqual(status_code, 200)

    def test_update_user_not_found(self):
        self.mock_db.update_user.return_value = 0
        response, status_code = self.user_service.update_user(2, "Charlie", 40)
        self.assertEqual(response, {"error": "User not found"})
        self.assertEqual(status_code, 404)

    def test_delete_user_success(self):
        self.mock_db.delete_user.return_value = 1
        response, status_code = self.user_service.delete_user(1)
        self.assertEqual(response, {"message": "User deleted successfully"})
        self.assertEqual(status_code, 200)

    def test_delete_user_not_found(self):
        self.mock_db.delete_user.return_value = 0
        response, status_code = self.user_service.delete_user(2)
        self.assertEqual(response, {"error": "User not found"})
        self.assertEqual(status_code, 404)

if __name__ == '__main__':
    unittest.main()
