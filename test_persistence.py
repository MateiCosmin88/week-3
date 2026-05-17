from persistence import SaveManager
from unittest.mock import Mock

def test_save_user():
    fake_database = Mock()

    manager = SaveManager()
    result = manager.save_user("Amina")
    fake_database.save.assert_called_with("Amina")
    assert result == "User Saved"

test_save_user()

print ("Mock test passed")