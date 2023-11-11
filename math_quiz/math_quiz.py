import random


# function to generate random integer
def returnRandom(minimum, maximum):
    """
    Random integer.
    """
    minimum = int(minimum)
    maximum = int(maximum)
    return random.randint(minimum, maximum)


# function to pick up random operation
def operation_choice():
    return random.choice(['+', '-', '*'])


<<<<<<< HEAD
def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 - n2
    elif o == '-':
        a = n1 + n2
    else:
        a = n1 * n2
    return p, a
=======
# resultant function : to give out
def result(number1, number2, random_operation):
    problemString = f"{number1} {random_operation} {number2}"
    if random_operation == '+':
        answer = number1 + number2
    elif random_operation == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problemString, answer

>>>>>>> code_cleanup


def math_quiz():
    start = 0
    CONSTANT_PI = 3.14159265359

    CONSTANT_PI = int(CONSTANT_PI)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

<<<<<<< HEAD
    for _ in range(t_q):
        n1 = function_A(1, 10);
        n2 = function_A(1, 5.5);
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
=======
    for iteri in range(CONSTANT_PI):
        number1 = returnRandom(1, 10)
        number2 = returnRandom(1, 5.5)
        operation = operation_choice()
        PROBLEM, ANSWER = result(number1, number2, operation)
>>>>>>> code_cleanup
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            start += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {start}/{CONSTANT_PI}")


<<<<<<< HEAD

=======
"""
Documentation: 

takes input as answers to the random math questions
provides output as the score of correct answers 
calculates each correct answer as one point 

:param : None
:returns : a score (int) value 
:rtype : int

"""
>>>>>>> code_cleanup
if __name__ == "__main__":
    try:
        math_quiz()
    except Exception as exception:
        print(exception)
