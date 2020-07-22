#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, str: str) -> bool:
        res = True
        stack = []
        for s in str:
            if s == '(' or s == '{' or s == '[':
                stack.append(s)
            elif len(stack) > 0:
                stackTop = stack[len(stack)-1]
                if False == ((s == ')' and '(' == stackTop) or (s == '}' and '{' == stackTop) or (s == ']' and '[' == stackTop)):
                    res = False
                    break
                stack.pop()
            else:
                res = False
        
        if res == True and len(stack) == 0:
            res = True
        else:
            res = False
        return res
    
    testCase = []
    testCaseStr = "()"
    testCase.append(testCaseStr)
    testCaseStr = "()[]{}"
    testCase.append(testCaseStr)
    testCaseStr = "(]"
    testCase.append(testCaseStr)
    testCaseStr = "([)]"
    testCase.append(testCaseStr)
    testCaseStr = "{[]}"
    testCase.append(testCaseStr)
    testCaseStr = "]"
    testCase.append(testCaseStr)
    testCaseStr = "["
    testCase.append(testCaseStr)
    
    for val in testCase:
        print(isValid('', val))