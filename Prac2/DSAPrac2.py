

# Activity 2 - Implement Stacks and Queues

# DSA Stack
# arrays as data structure

class DSAStack:
    def __init__(self, stack, count, def_cap = 100):
        self.stack = stack
        self.count = count
        self.def_cap = def_cap

    def is_full(self):
        """Checks if stack is full"""
        pass

    def push(self, value):
        """add new item to top of stack"""
        if self.is_full():
            print("Stack full")     # FIXME: handle this correctly
            pass
        else:
            self[count] = value
            self.count += 1
        pass

    def pop(self):
        """take top-most item from stack"""
        pass

    def top(self):
        """look at top-most item, leave it on stack"""
        pass

    def is_empty(self):
        """check if stack is empty"""
        pass


# DSAQueue



# Activity 3 - Equation Solver


"""
Simple class that takes string of infix equation

converts to postfix
evaluates postfix
"""

infix = "4 + 3 * 12"


class EqSolver:
    def __init__(self):


    def precedence_of(the_operator):
        """Helper function for parse_infix_2_postfix()

        Returns precedence (as int) of the_operator

        examples:
            + or - return 1
            * or / return 2"""
        pass

    def parse_next_term(equation):
        pass

    def parse_infix_2_postfix(equation):
        """Convert infix form equation to postfix

        Stores postfix terms in queue of objects"""
        postfix = []

        while infix:
            term = parse_next_term()  # TODO: implement method

            if term == "(":
                op_stack.push("(")  # TODO: implement
            elif term == ")":
                while op_stack.top() not "(":
                    postfix = postfix + op_stack.pop()
                op_stack.pop()
            elif (term == "+") or (term == "-") or (term == "*") or (
                    term == "/"):
                while (not op_stack.is_empty()) and (op_stack.top()
                not "(") and (
                precendence_of(op_stack.top() >= precendence_of(term))):
                    postfix = postfix + op_stack.pop()
                op_stack.push(term)
            else:
                postfix = postfix + term

        while not op_stack.is_empty():
            postfix = postfix + op_stack.pop()






    def execute_operation(op1, op2, op3):
        """Helper function for eval_postfix()

        Executes binary operation implied by op and returns result"""
        pass


    def eval_postfix(postfix_queue):
        """Takes postfix queue and evaluates it"""
        pass


    def solve(equation):
        """Should call parse_infix_2_postfix() and then eval_postfix()"""
        pass



