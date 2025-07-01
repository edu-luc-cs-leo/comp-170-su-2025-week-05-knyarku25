#This function finds the common characters betweeen two strings
#It avoids duplicate characters in the result
from bleach import clean


# Returns characters from foo that are in bar, respecting how many times they appear in bar
def intersection(foo: str, bar: str) -> str:
    if foo is None or bar is None:
        return ""

    result = ""

    # Build a frequency list of characters in bar
    bar_freq = []
    for i in range(len(bar)):
        bar_freq.append(bar[i])

    # Loop through each character in foo
    for i in range(len(foo)):
        for j in range(len(bar_freq)):
            if foo[i] == bar_freq[j]:
                result += foo[i]
                bar_freq[j] = "*"  # Mark as used
                break  # Only use each bar character once
    return result





# This  function checks if the string has only letters
def is_alphabetical(string: str) -> bool:
    if string is None or string == "":
        return False
    for char in string:
        # Get ASCII value for each character
        ascii_val = ord(char)
        # Check if  it is not a letter (A-Z or a-z)
        if not ((65 <= ascii_val <= 90)or (97 <= ascii_val <= 122)):
            return False # found something that's not a letter
    return True # all characters were letters    

# This function removes any character that is not a letter
def letters_only(string: str) -> str | None:
    if string is None or string == "":
        return None  # Return None for None or empty input

    result = ""
    for i in range(len(string)):
        if string[i].isalpha():
            result += string[i]

    return result  # If no letters found, still return "" as per test


# This function creates a weird-looking palindrome by appending the reverse of the string
def generate_palindrome(string: str) -> str | None:
    if string is None or string == "":
        return None
    reverse = ""
    # Build the reverse of the string manually
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    # Just stick the original and reversed string together
    return string + reverse

# This function checks if a string is a palindrome ( ignores punctuation and case)
def is_palindrome(string: str) -> bool:
    if string is None or string == "":
        return False
    cleaned = ""
    # Clean the string. Keep only letters and numbers, and make them lowercase
    for char in string:
        if char.isalnum():
            cleaned += char.lower()
# Check of ot reads the same forward and backward
    reversed_str = ""
    for i in range(len(cleaned) - 1, -1, -1 ):
        reversed_str += cleaned[i]
    return cleaned == reversed_str    
                
import unittest


class TestStringMethods(unittest.TestCase):


    def test_intersection(self):

        self.assertEqual(intersection("airplanes", "repairman"), "airpne")

        self.assertEqual(intersection("abc", "def"), "")

        self.assertEqual(intersection("hello", "hello"), "hello")

        self.assertEqual(intersection("aaaa", "aaa"), "a")

        self.assertEqual(intersection("", "abc"), None)

        self.assertEqual(intersection("abc", ""), None)

        self.assertEqual(intersection("", ""), None)

        self.assertEqual(intersection("abc", "cab"), "abc") # preserves order of `foo`


    def test_is_alphabetical(self):

        self.assertTrue(is_alphabetical("abcXYZ"))

        self.assertFalse(is_alphabetical("abc1"))

        self.assertFalse(is_alphabetical("hello!"))

        self.assertFalse(is_alphabetical(" "))

        self.assertFalse(is_alphabetical(""))

        self.assertFalse(is_alphabetical(None))

        self.assertTrue(is_alphabetical("ZzAaBb"))


def test_letters_only(self):

    self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")

    self.assertEqual(letters_only("!@#$%^&*()"), "")

    self.assertEqual(letters_only(""), None)

    self.assertEqual(letters_only(None), None)

    self.assertEqual(letters_only("LettersONLY"), "LettersONLY")


def test_generate_palindrome(self):

    self.assertEqual(generate_palindrome("mice"), "miceecim")

    self.assertEqual(generate_palindrome("mad"), "madam")

    self.assertEqual(generate_palindrome("a"), "a")

    self.assertEqual(generate_palindrome(""), None)

    self.assertEqual(generate_palindrome(None), None)


def test_is_palindrome(self):

    self.assertTrue(is_palindrome("Racecar"))

    self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    self.assertTrue(is_palindrome("No 'x' in Nixon"))

    self.assertFalse(is_palindrome("Hello"))

    self.assertFalse(is_palindrome("Palindrome"))

    self.assertFalse(is_palindrome(""))

    self.assertFalse(is_palindrome(None))




# This allows the test to be run from the command line using `python -m unittest filename.py`

if __name__ == '__main__':

    unittest.main()


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))

