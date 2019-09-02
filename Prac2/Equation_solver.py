"""
Activity 3 - Equation Solver

Simple class that takes string of infix equation

converts to postfix
evaluates postfix
"""
import myQueue
import myStack

infix = "((4 + 3) / 20) * 12"


class EqSolver:
    def __init__(self):
        pass

    def _precedence_of(the_operator):
        """Helper function for parse_infix_2_postfix()

        Returns precedence (as int) of the_operator

        examples:
            + or - return 1
            * or / return 2"""
        pass

    def parse_next_term(equation):
        pass

    def _parse_infix_2_postfix(equation):
        """Convert infix form equation to postfix

        Stores postfix terms in stack of objects"""

        postfix_s = myStack.DSAStack()
        op_stack = myStack.DSAStack()

        while infix:
            term = parse_next_term(equation)  # TODO: implement method

            if term == "(":
                op_stack.push("(")  # TODO: implement
            elif term == ")":
                while op_stack.top() not "(":
                    popped = op_stack.pop()
                    postfix_s.push(popped)
                op_stack.pop()
            elif (term == "+") or (term == "-") or (term == "*") or (
                    term == "/"):
                while (not op_stack.is_empty()) and (op_stack.top()
                not "(") and (
                precendence_of(op_stack.top() >= precendence_of(term))):
                    postfix_s.push(op_stack.pop())
                op_stack.push(term)
            else:
                postfix_s.push(term)

        while not op_stack.is_empty():
            postfix_s.push(op_stack.pop())






    def _execute_operation(op1, op2, op3):
        """Helper function for eval_postfix()

        Executes binary operation implied by op and returns result"""
        pass


    def _eval_postfix(postfix_queue):
        """Takes postfix queue and evaluates it"""
        pass


    def solve(equation):
        """Should call parse_infix_2_postfix() and then eval_postfix()"""
        pass



