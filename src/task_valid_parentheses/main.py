class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_br = ("(", "[", "{")
        close_br = (")", "]", "}")
        for sym in s:
            if sym in open_br:
                stack.insert(0, sym)
            elif close_br.index(sym) == open_br.index(stack[0]):
                stack.pop(0)
            else:
                return False
        return True
