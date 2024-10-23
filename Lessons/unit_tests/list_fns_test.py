from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


# desired return value
def test_remove_first_return_value() -> None:
    """remove_first shoud return None."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove_first should remove the first element from the input"""
    dog_breeds: list[str] = ["husky", "golden", "poodle"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    """get_list called on an empty list shoudl return ""."""
    assert get_first([]) == ""
