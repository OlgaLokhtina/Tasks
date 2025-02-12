from main import Solution


def test_isValid():
    s = Solution()
    assert s.isValid("([]){()[]}") == True, "Should be True"
    assert s.isValid("([]){([)[]]}") == False, "Should be False"
