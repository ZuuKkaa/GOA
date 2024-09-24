def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(is_anagram("Listen", "Silent"))  # Output: True
print(is_anagram("Hello", "World"))    # Output: False