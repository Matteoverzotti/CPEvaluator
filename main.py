import time
import sys
import random
import os
import subprocess
import constants  # constants.py
from solver import Solver

def main():
    try:
        os.chdir(
            constants.PATH
        )  # Go to the directory of the program (specified in the JSON file)
    except FileNotFoundError:
        print("Directory not found!\n")
        exit(0)

    if solver.Compile() == constants.COMPILE_ERROR:  # Compilation Error
        sys.stdout.write(constants.RED + "Compilation error!\n" + constants.WHITE)

        print("Compilation message: ")
        with open("compile_message.txt", "r") as f:
            print(f.read())

        exit(0)

    sys.stdout.write(constants.GREEN + "Compilation Successful!\n" + constants.WHITE)
    sys.stdout.write(
        constants.MAGENTA
        + "Execution time limit: "
        + constants.WHITE
        + str(constants.TIME_LIMIT)
        + " seconds\n"
    )

    sys.stdout.write(
        constants.MAGENTA
        + "Execution memory limit: "
        + constants.WHITE
        + str(constants.MEMORY_LIMIT)
        + " kbytes\n"
    )

    try:
        test_cases = int(input("Input the number of test cases: "))
    except ValueError:
        print("Invalid number of test cases!")
        exit(0)

    for test in range(1, test_cases + 1):
        sys.stdout.write("Verdict to test {} ... Waiting".format(test))
        sys.stdout.flush()

        solver.Copy_Input(test)
        verdict = solver.Solve_Case(test)

        if verdict == constants.WRONG_ANSWER:  # Wrong answer
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test)
                + constants.RED
                + "Wrong Answer "
                + constants.WHITE
            )

        elif verdict == constants.ACCEPTED:  # OK
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test)
                + constants.GREEN
                + "Accepted "
                + constants.WHITE
            )

        elif verdict == constants.TIME_LIMIT_EXCEEDED:  # Time Limit Exceeded
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test)
                + constants.YELLOW
                + "Time Limit Exceeded "
                + constants.WHITE
            )

        elif verdict == 3:  # Memory Limit Exceeded
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test)
                + constants.YELLOW
                + "Memory Limit Exceeded "
                + constants.WHITE
            )

        else:  # Runtime Error
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test)
                + constants.YELLOW
                + "Runtime Error "
                + constants.WHITE
            )

        sys.stdout.write("| " + str(constants.EXEC_TIME) + " s | "
                    + str(constants.MEMORY_USED) + " kb\n")

if __name__ == "__main__":
    solver = Solver(constants.TIME_LIMIT, constants.MEMORY_LIMIT)
    main()
