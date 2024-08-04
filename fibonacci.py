from abc import ABC, abstractmethod
from time import time
from decimal import Decimal
from numpy import array, matmul
from karatsuba import multiply


class Fibonacci(ABC):
    final_value: int = 0
    start_time: time

    def __init__(self, max_seconds: int):
        self.max_seconds = max_seconds

    @abstractmethod
    def start(self) -> (int, time):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class SimpleRecursiveFibonacci(Fibonacci):

    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        if time() - self.start_time >= self.max_seconds:
            return n1
        return self.fib(n1, n0 + n1)

    def get_name(self) -> str:
        return "Simple Recursive Fibonacci"


class RecursiveFibonacciWithCatch(Fibonacci):

    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        if time() - self.start_time >= self.max_seconds:
            return n1
        try:
            return self.fib(n1, n0 + n1)
        except RecursionError as e:
            return n1

    def get_name(self) -> str:
        return "Recursive Fibonacci with Catch"


class RecursiveFibonacciWithRestart(Fibonacci):

    def start(self) -> (int, time):
        self.start_time = time()
        n0 = 0
        n1 = 1
        while time() - self.start_time <= self.max_seconds:
            n0, n1 = self.fib(n0, n1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(n1)), finish_time

    def fib(self, n0, n1):
        try:
            return self.fib(n1, n0 + n1)
        except RecursionError as e:
            return n0, n1

    def get_name(self) -> str:
        return "Recursive Fibonacci with Restart"


class IterativeFibonacci(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (n0, n1) = n1, n0 + n1
        return n1

    def get_name(self) -> str:
        return "Iterative Fibonacci"


class IterativeFibonacciWith2S(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (n0, n1) = n0 + n1, n0 + 2 * n1
        return n1

    def get_name(self) -> str:
        return "Iterative Fibonacci with 2-step"


class IterativeFibonacciWith2LU(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (tmp0, tmp1) = n1, n0 + n1
            (n0, n1) = tmp1, tmp0 + tmp1
        return n1

    def get_name(self) -> str:
        return "Iterative Fibonacci with 2-Loop Unroll"


class IterativeFibonacciWith4LU(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (tmp0, tmp1) = n1, n0 + n1
            (tmp2, tmp3) = tmp1, tmp0 + tmp1
            (n0, n1) = tmp3, tmp2 + tmp3
        return n1

    def get_name(self) -> str:
        return "Iterative Fibonacci with 4-Loop Unroll"


class IterativeFibonacciWith5S(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(0, 1)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (n0, n1) = 2 * n0 + 5 * n1, 4 * n0 + 8 * n1
        return n1

    def get_name(self) -> str:
        return "Iterative Fibonacci with 5-step"


class MatrixFibonacci(Fibonacci):

    def start(self) -> (int, time):
        self.start_time = time()
        result = array([[1, 1], [1, 0]])
        while time() - self.start_time < self.max_seconds:
            result = matmul(result, result)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result[0, 0].item())), finish_time

    def get_name(self) -> str:
        return "Matrix Fibonacci"


#  from: https://www.nayuki.io/page/fast-fibonacci-algorithms
class FastDoublingFibonacci(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(1, 2)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (n0, n1) = n0 * (2 * n1 - n0), n1 ** 2 + n0 ** 2
        return n1

    def get_name(self) -> str:
        return "Fast Doubling Fibonacci"


class FastDoublingKaratsubaFibonacci(Fibonacci):
    def start(self) -> (int, time):
        self.start_time = time()
        result = self.fib(1, 2)
        finish_time = time() - self.start_time
        return "{:.2E}".format(Decimal(result)), finish_time

    def fib(self, n0, n1):
        while time() - self.start_time < self.max_seconds:
            (n0, n1) = multiply(n0, (2 * n1 - n0)), multiply(n1, n1) + multiply(n0, n0)
        return n1

    def get_name(self) -> str:
        return "Fast Doubling Fibonacci w/ Karatsuba"
