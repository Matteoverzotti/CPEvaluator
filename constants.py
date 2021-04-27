# Color unicodes
WHITE = "\033[0m"
GREEN = "\033[92m"
RED = "\u001b[31m"
BLACK = "\u001b[30m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"

# Verdicts
COMPILE_ERROR = -1
WRONG_ANSWER = 0
ACCEPTED = 1
TIME_LIMIT_EXCEEDED = 2
MEMORY_LIMIT_EXCEEDED = 3
RUNTIME_ERROR = 4


import json

with open("config.json", "r") as config_file:
    parameters = json.load(config_file)

PATH = parameters['path']
TIME_LIMIT = parameters['time_limit']
MEMORY_LIMIT = parameters['memory_limit']
FLAGS = parameters['flags']

FILE = parameters['filename']
INPUT = parameters['input_file']
OUTPUT = parameters['output_file']

for EXECUTABLE in parameters['flags']:
    pass

# These are actually variables
EXEC_TIME = 0
MEMORY_USED = 0
