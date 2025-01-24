from main import Solution


def test_isPalindrome():
    a = Solution()
    assert a.isPalindrome(131) == True, "Should be True"
    assert a.isPalindrome(-7654) == False, "Should be False"
