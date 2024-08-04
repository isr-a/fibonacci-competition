from tabulate import tabulate
from functools import cmp_to_key
from fibonacci import *
from tester import Tester


def get_participants(max_seconds):
    recursive_fibonacci = SimpleRecursiveFibonacci(max_seconds)
    iterative_fibonacci = IterativeFibonacci(max_seconds)
    recursive_fibonacci_with_catch = RecursiveFibonacciWithCatch(max_seconds)
    recursive_fibonacci_with_restart = RecursiveFibonacciWithRestart(max_seconds)
    iterative_fibonacci_with_2s = IterativeFibonacciWith2S(max_seconds)
    iterative_fibonacci_with_2lu = IterativeFibonacciWith2LU(max_seconds)
    iterative_fibonacci_with_4lu = IterativeFibonacciWith4LU(max_seconds)
    iterative_fibonacci_with_5s = IterativeFibonacciWith5S(max_seconds)
    return [
        recursive_fibonacci,
        iterative_fibonacci,
        recursive_fibonacci_with_catch,
        recursive_fibonacci_with_restart,
        iterative_fibonacci_with_2s,
        iterative_fibonacci_with_2lu,
        iterative_fibonacci_with_4lu,
        iterative_fibonacci_with_5s,
    ]


def sort_results(a, b):
    (part_a, result_a, time_a) = a
    (part_b, result_b, time_b) = b
    if result_a == "FAILED":
        return 1
    if result_b == "FAILED":
        return -1
    cmp_a = int(result_a.split("E+")[1])
    cmp_b = int(result_b.split("E+")[1])
    if cmp_a > cmp_b:
        return -1
    if cmp_a < cmp_b:
        return 1
    return 0


def format_results(results):
    return tabulate(sorted([(k,) + v for k, v in results.items()], key=cmp_to_key(sort_results)),
                    headers=['Participant', 'Result', 'Total Time'], tablefmt='pipe')


def save_to_readme(pretty_results):
    with open('README.md', 'w') as file:
        file.write("# Fibonacci method tier list! \n")
        file.write("\n")
        file.write("Ever wondered what the quickest way to calculate a fibonacci number was? \n")
        file.write("No? Well whether you are or not I'm here to figure out what is the ideal! \n")
        file.write("\n")
        file.write("Below is a table containing the results of the most recent run (before committing) with the competitors: \n")
        file.write("\n")
        file.write("\n")
        file.write(pretty_results)
        file.write("\n")
        file.write("\n")
        file.write("Interested in taking a swing with your own function? \n")
        file.write("Make a Pull Request and submit your attempt! Alongside running the code to see how you stack up :)\n")


def main():
    max_seconds = 1

    participants = get_participants(max_seconds)
    tester = Tester(participants)
    results = tester.test_implementations()
    pretty_results = format_results(results)
    save_to_readme(pretty_results)
    print(pretty_results)


if __name__ == '__main__':
    main()
