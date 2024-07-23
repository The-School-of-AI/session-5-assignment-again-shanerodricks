import pytest
import os
import re
import inspect
import session5
from session5 import time_it, squared_power_list, polygon_area, temp_converter, speed_converter

# Constants for README content checks
README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

# Test 1: README file existence
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# Test 2: README content length
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"

# Test 3: README proper description
def test_readme_proper_description():
    READMELOOKSGOOD = True
    with open("README.md", "r") as f:
        content = f.read()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

# Test 4: README file formatting
def test_readme_file_for_formatting():
    with open("README.md", "r") as f:
        content = f.read()
    assert content.count("#") >= 10

# Test 5: Code indentation and PEP8 guidelines
def test_fourspace():
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code indentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

# Test 6: time_it function with print
def test_time_it_print():
    assert isinstance(time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5), float)

# Test 7: time_it function with squared_power_list
def test_time_it_squared_power_list():
    assert isinstance(time_it(squared_power_list, 2, start=0, end=5, repetitions=5), float)

# Test 8: time_it function with polygon_area
def test_time_it_polygon_area():
    assert isinstance(time_it(polygon_area, 15, sides=3, repetitions=10), float)

# Test 9: time_it function with temp_converter
def test_time_it_temp_converter():
    assert isinstance(time_it(temp_converter, 100, temp_given_in='f', repetitions=100), float)

# Test 10: time_it function with speed_converter
def test_time_it_speed_converter():
    assert isinstance(time_it(speed_converter, 100, dist='km', time='min', repetitions=200), float)

# Test 11: Functionality of squared_power_list
def test_squared_power_list():
    assert squared_power_list(2, start=0, end=5) == [1, 2, 4, 8, 16, 32]

# Test 12: Functionality of polygon_area
def test_polygon_area():
    assert pytest.approx(polygon_area(15, sides=3), 0.01) == 97.43

# Test 13: Functionality of temp_converter (Celsius to Fahrenheit)
def test_temp_converter_c_to_f():
    assert temp_converter(0, temp_given_in='c') == 32
    assert temp_converter(100, temp_given_in='c') == 212

# Test 14: Functionality of temp_converter (Fahrenheit to Celsius)
def test_temp_converter_f_to_c():
    assert pytest.approx(temp_converter(32, temp_given_in='f'), 0.01) == 0
    assert pytest.approx(temp_converter(212, temp_given_in='f'), 0.01) == 100

# Test 15: Functionality of speed_converter
def test_speed_converter():
    assert pytest.approx(speed_converter(1, dist='km', time='hr'), 0.01) == 1
    assert pytest.approx(speed_converter(1, dist='m', time='s'), 0.01) == 3.6
    assert pytest.approx(speed_converter(1, dist='ft', time='s'), 0.01) == 1.09728
    assert pytest.approx(speed_converter(1, dist='yrd', time='min'), 0.01) == 0.05486

if __name__ == '__main__':
    pytest.main()
