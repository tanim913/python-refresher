class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        result = []

        def recursive(n_open, n_close):
            if n_open == n_close == n:
                comb = "".join(stack)
                result.append(comb)

            if n_open > n_close:
                stack.append(")")
                recursive(n_open, n_close + 1)
                stack.pop() # we are using same stack variable, so stack need to be popped after appending the closing bracket

            if n_open < n:
                stack.append("(")
                recursive(n_open + 1, n_close)
                stack.pop() # we are using same stack variable, so stack need to be popped after appending the opening bracket


        recursive(0,0)
        return result