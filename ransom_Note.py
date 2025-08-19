def canConstruct_debug(ransomNote: str, magazine: str) -> bool:
    print(f"\n--- Run: ransomNote='{ransomNote}', magazine='{magazine}' ---")

    # 1) Count characters in magazine
    letter_count = {}
    print("[1] Counting characters in magazine:")
    for i, char in enumerate(magazine):
        prev = letter_count.get(char, 0)
        letter_count[char] = prev + 1
        print(
            f"  i={i} | char='{char}' | previous_count={prev} -> new_count={letter_count[char]} | letter_count={letter_count}")

    # 2) Consume characters for ransomNote
    print("[2] Consuming characters for ransomNote:")
    for i, char in enumerate(ransomNote):
        available = letter_count.get(char, 0)
        print(f"  i={i} | need char='{char}' | available_before={available}")
        if available == 0:
            print(f"    -> Not enough '{char}'. Return False.")
            return False
        letter_count[char] -= 1
        print(
            f"    -> Used one '{char}'. remaining={letter_count[char]} | letter_count={letter_count}")

    print("All characters satisfied. Return True.")
    return True


# ✅ Example runs
print(canConstruct_debug("a", "b"))
print(canConstruct_debug("aa", "ab"))
print(canConstruct_debug("aa", "aab"))
