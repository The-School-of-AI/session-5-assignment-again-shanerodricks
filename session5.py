import time

def time_it(fn, *args, repetitions=1, **kwargs):
    total_time = 0.0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        fn(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    avg_time = total_time / repetitions
    return avg_time

def squared_power_list(number, start=0, end=5):
    return [number ** i for i in range(start, end+1)]

def polygon_area(side_length, sides=3):
    from math import tan, pi
    return (sides * side_length ** 2) / (4 * tan(pi / sides))

def temp_converter(temp, temp_given_in='c'):
    if temp_given_in == 'c':
        # Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif temp_given_in == 'f':
        # Fahrenheit to Celsius
        return (temp - 32) * 5/9

def speed_converter(speed, dist='km', time='hr'):
    # Convert speed to km/h
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
