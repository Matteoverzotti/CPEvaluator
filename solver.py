import subprocess
import os
import sys
import threading
import time
from datetime import datetime

import constants  # constants.py

class Solver:
    def __init__(self, time_limit, memory_limit):
        self.time_limit = time_limit
        self.memory_limit = memory_limit

    def Copy_Input(self, test_case):
        in_file = "in/test" + str(test_case) + ".in"
        p = subprocess.run(
            ["cp", "-v", in_file, constants.INPUT],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )  # Copies the contents of "testx.in" into "input.in"

        if p.returncode != 0:  # Throws Error
            sys.stdout.write(
                "\rVerdict to test {} ... ".format(test_case)
                + constants.RED
                + "Test case {} doesn't exist\n".format(test_case)
                + constants.WHITE
            )
            sys.stdout.write("Exiting...\n")
            exit(0)

    def Check_Ok(self, test_case):  # Compares the output file with the ok file
        out_file = constants.OUTPUT
        ok_file = "ok/test" + str(test_case) + ".ok"

        diff_output = subprocess.run(
            ["diff", "-qBbEa", out_file, ok_file], capture_output=True, text=True
        )
        # returns if {out_file} and {ok_file} are identical or not
        # -q reports only when files differ

        if diff_output.stdout == "":
            return constants.ACCEPTED
        return constants.WRONG_ANSWER

    def Solve_Case(self, test_case):
        def RunProgram():
            global process
            global finished

            finished = False
            process = subprocess.run(
                    ["./{}".format(constants.EXECUTABLE)], capture_output = True, text = True
            )  # Execute the program
            finished = True
            
            if process.stderr.find('runtime error') != -1:
                process.returncode = 1

        def Memory_Check():
            process = subprocess.run(["valgrind", "--tool=memcheck", "./a.out"], 
                                     capture_output = True, 
                                     text = True
            )
            idx = process.stderr.find("bytes allocated")
            idx = idx - 2
            
            while process.stderr[idx] != ' ':
                idx = idx - 1
            
            idx = idx + 1
            consumed_memory = ""
            while process.stderr[idx].isdigit() or process.stderr[idx] == ',':
                if process.stderr[idx].isdigit():
                    consumed_memory += process.stderr[idx]

                idx = idx + 1
            
            # consumed_memory is in bytes, we have to convert to kbytes
            consumed_memory = int(consumed_memory)
            consumed_memory /= 1000
            return int(consumed_memory)

        program = threading.Thread(target=RunProgram, daemon=True)
        startTime = datetime.now()
        program.start()

        while (
            finished == False
            and (datetime.now() - startTime).seconds
            + (datetime.now() - startTime).microseconds / 1000000
            < self.time_limit
        ):  # Try to let the time pass while executing the program on a separate thread
            time.sleep(0.01)
            pass
        
        constants.EXEC_TIME = min((datetime.now() - startTime).seconds 
                + (datetime.now() - startTime).microseconds / 1000000, constants.TIME_LIMIT)
        if finished == False:  # TLE
            constants.EXEC_TIME = constants.TIME_LIMIT
            constants.MEMORY_USED = "NaN" # Not measured
            return constants.TIME_LIMIT_EXCEEDED

        if process.returncode != 0:  # RE
            constants.EXEC_TIME = "NaN" # Not measured
            constants.MEMORY_USED = "NaN"
            return constants.RUNTIME_ERROR

        constants.MEMORY_USED = Memory_Check()

        if constants.MEMORY_USED > self.memory_limit:  # MLE
            return constants.MEMORY_LIMIT_EXCEEDED

        return self.Check_Ok(test_case)  # Check the files

    def Compile(self):  # This compiles the program
        sys.stdout.write("Compiling ... ")
        sys.stdout.flush()

        with open("compile_message.txt", "w") as f:
            run_program = subprocess.run(
                constants.FLAGS, stderr=f
            )  # Redirects the compiler messages to "compile_message.txt"

        # Returns the error code, 0 = successful, 1 = compilation error
        if run_program.returncode == 0:
            return constants.ACCEPTED
        return constants.COMPILE_ERROR
