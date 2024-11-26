
def test_validate_input(monkeypatch):
    from utils.validators import validate_input

    monkeypatch.setattr("builtins.input", lambda _: "Test Title")
    result = validate_input("Enter title: ", validation_func=lambda x: x)
    assert result == "Test Title"
