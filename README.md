# Informed Search Assignment

Note: The user must have Python already installed on their local machine in order for this program script to run.

This assignment is a program that creates two heuristic search algorithms that find solutions to the 24-puzzle problem. I first started with solving the 8-puzzle problem, then adjusted the program to solve the 24-puzzle problem.

WARNING: There is a possibility that this program might crash due to my machine not having enough RAM to solve the 24-puzzle problem (I progammed this assignment locally). During test runs, I had an average of about 5.6 GB of RAM left on my machine. I hard-coded RAM guardrails into this program so that it maxes out how much it is allowed to use (3000000 states is the maximum amount that are allowed to be searched through). I was aware that this guardrail would not allow me to solve the given 24-puzzle problem in the assignment.

-----------------------------
## How to execute:
* Clone this repo from GitHub using `git clone https://github.com/emirick72/CS-580_Informed_Search_Assignment.git`
* cd into the program's repo on your machine (`cd CS-580_Informed_Search_Assignment`)
* To run the program (not the generate results command), type this command into the terminal: `python main.py`
* Alternatively, to generate the benchmark results into a text file (which must be named `results.txt` and be completely empty before running the command), type this command into the terminal: `python generate_results.py`
* NOTE: The results from the final run I did are located in `results.txt`