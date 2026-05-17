from persistence import SaveManager
def test_save_user():
    manager = SaveManager() 
    result = manager.save_user("Animal")
    assert result == "User Saved"