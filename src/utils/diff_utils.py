import difflib


def get_text_changes(original_text: str, refined_text: str):
    original_words = original_text.split()
    refined_words = refined_text.split()

    matcher = difflib.SequenceMatcher(
        None,
        original_words,
        refined_words
    )

    changes = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue

        before = " ".join(original_words[i1:i2])
        after = " ".join(refined_words[j1:j2])

        changes.append({
            "type": tag,
            "before": before,
            "after": after
        })

    return changes