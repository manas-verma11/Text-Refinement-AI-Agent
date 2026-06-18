from src.utils.diff_utils import get_text_changes

def test_get_text_changes_detects_replacement():
    original_text = "heloo i am good"
    refined_text = "hello I am doing well"

    changes = get_text_changes(original_text, refined_text)

    assert len(changes) > 0
    assert any(change["type"] in ["replace", "insert", "delete"] for change in changes)