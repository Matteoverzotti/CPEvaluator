CPEvaluator
===========

CPEvaluator is a program built to run trusted executables on your
local machine, in order to test your program for a problem which is not
currently on a competitive programming judge. It is not perfectly
accurate, and can lead to higher execution times than normal. This is just
a side project for myself.


Prerequisites
=============

* [Valgrind](https://valgrind.org/)


Setup
=====

Just clone the github repository to any folder.

Edit the `config.json` file to specify the path of the program,
the time/memory limits, the name of the program, and the compilation flags

After that, create 2 folders in the folder you have specified previously, called
/in and /ok. In them, Put the files you have to test your program to. Their format should
be `testx.in` and `testx.ok` (where `x` is the number of the test, starting with 1, no leading zeroes)


Now, just run the `main.py` program.
