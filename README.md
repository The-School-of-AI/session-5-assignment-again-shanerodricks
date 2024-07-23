[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HfhAxLC5)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15447757&assignment_repo_type=AssignmentRepo)

# Time_it - Performance Timing Utility

# Problem Description
Write a time_it function that can measure the average runtime of any given function over a specified number of repetitions. The function should be flexible enough to accept any function with its arguments and keyword arguments. It should return the average time taken for the function to execute.

# Function Definition
def time_it(fn, *args, repetitions=1, **kwargs):
    total_time = 0.0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        fn(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    avg_time = total_time / repetitions
    return avg_time

# Example Usage

def squared_power_list(number, start=0, end=5):
    return [number ** i for i in range(start, end+1)]

def polygon_area(side_length, sides=3):
    from math import tan, pi
    return (sides * side_length ** 2) / (4 * tan(pi / sides))

def temp_converter(temp, temp_given_in='c'):
    if temp_given_in == 'c':
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif temp_given_in == 'f':
        return (temp - 32) * 5/9  # Fahrenheit to Celsius

def speed_converter(speed, dist='km', time='hr'):
    # Convert speed to km/h first
    if dist == 'm':
        speed *= 0.001
    elif dist == 'ft':
        speed *= 0.0003048
    elif dist == 'yrd':
        speed *= 0.0009144
    # Convert time to hours
    if time == 'ms':
        speed *= 3600000
    elif time == 's':
        speed *= 3600
    elif time == 'min':
        speed *= 60
    elif time == 'day':
        speed /= 24
    return speed

# Test calls
print(time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5))
print(time_it(squared_power_list, 2, start=0, end=5, repetitions=5))
print(time_it(polygon_area, 15, sides=3, repetitions=10))
print(time_it(temp_converter, 100, temp_given_in='f', repetitions=100))
print(time_it(speed_converter, 100, dist='km', time='min', repetitions=200))

# Solution
A total of 1 function time_it and various example functions are implemented to demonstrate its usage.

# Functionality
'time_it':
- Measures the average runtime of a function over a specified number of repetitions.
- Returns the average time taken for the function to execute.

# Example Functions
- squared_power_list: Returns a list of powers of a given number.
- polygon_area: Calculates the area of a polygon given its side length and number of sides.
- temp_converter: Converts temperature between Celsius and Fahrenheit.
- speed_converter: Converts speed given in km/h to other units.

# Tests
Unit test file test_time_it.py must contain at least 25 tests and they must not be repetitive. Some of the tests it must implement are:
- Measure the time for a simple print statement repeated multiple times.
- Measure the time for calculating a list of powers.
- Measure the time for calculating the area of a polygon.
- Measure the time for temperature conversion.
- Measure the time for speed conversion.

# Example Test Cases
import unittest
from time_it_script import time_it, squared_power_list, polygon_area, temp_converter, speed_converter

class TestTimeIt(unittest.TestCase):

    def test_print_function(self):
        self.assertIsInstance(time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5), float)

    def test_squared_power_list(self):
        self.assertIsInstance(time_it(squared_power_list, 2, start=0, end=5, repetitions=5), float)

    def test_polygon_area(self):
        self.assertIsInstance(time_it(polygon_area, 15, sides=3, repetitions=10), float)

    def test_temp_converter(self):
        self.assertIsInstance(time_it(temp_converter, 100, temp_given_in='f', repetitions=100), float)

    def test_speed_converter(self):
        self.assertIsInstance(time_it(speed_converter, 100, dist='km', time='min', repetitions=200), float)

    # Additional tests for edge cases and performance

if __name__ == '__main__':
    unittest.main()

# Reference
- time.perf_counter(): High-resolution timer used to measure time intervals.
- unittest: Python's standard library for writing and running tests.