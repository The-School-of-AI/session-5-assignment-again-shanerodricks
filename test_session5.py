import unittest
from time import time
from your_module import time_it, squared_power_list, polygon_area, temp_converter, speed_converter

class TestFunctions(unittest.TestCase):
    
    def test_squared_power_list(self):
        test_cases = [
            (2, 0, 5, [1, 2, 4, 8, 16, 32]),
            (3, 0, 3, [1, 3, 9, 27]),
            (5, 1, 4, [5, 25, 125, 625]),
            (10, 2, 4, [100, 1000, 10000]),
            (7, 0, 0, [1]),
        ]
        for number, start, end, expected in test_cases:
            with self.subTest(number=number, start=start, end=end):
                self.assertEqual(squared_power_list(number, start, end), expected)
                
    def test_polygon_area(self):
        test_cases = [
            (15, 3, 97.42785792574934),
            (10, 4, 100.0),
            (7, 5, 84.30339262885938),
            (6, 6, 93.53074360871938),
            (8, 8, 308.16992531295375),
        ]
        for side_length, sides, expected in test_cases:
            with self.subTest(side_length=side_length, sides=sides):
                self.assertAlmostEqual(polygon_area(side_length, sides), expected, places=5)
                
    def test_temp_converter(self):
        test_cases = [
            (100, 'c', 212.0),
            (32, 'f', 0.0),
            (0, 'c', 32.0),
            (100, 'f', 37.77777777777778),
            (-40, 'c', -40.0),
        ]
        for temp, temp_given_in, expected in test_cases:
            with self.subTest(temp=temp, temp_given_in=temp_given_in):
                self.assertAlmostEqual(temp_converter(temp, temp_given_in), expected, places=5)
                
    def test_speed_converter(self):
        test_cases = [
            (100, 'km', 'hr', 100.0),
            (60, 'm', 's', 216.0),
            (30, 'ft', 'min', 0.54864),
            (5, 'yrd', 'day', 0.019049795),
            (100, 'km', 'min', 6000.0),
        ]
        for speed, dist, time, expected in test_cases:
            with self.subTest(speed=speed, dist=dist, time=time):
                self.assertAlmostEqual(speed_converter(speed, dist, time), expected, places=5)
                
    def test_time_it(self):
        test_cases = [
            (squared_power_list, [2], {'start': 0, 'end': 5}, 5),
            (polygon_area, [15], {'sides': 3}, 10),
            (temp_converter, [100], {'temp_given_in': 'f'}, 100),
            (speed_converter, [100], {'dist': 'km', 'time': 'min'}, 200),
        ]
        for fn, args, kwargs, repetitions in test_cases:
            with self.subTest(fn=fn, args=args, kwargs=kwargs, repetitions=repetitions):
                avg_time = time_it(fn, *args, repetitions=repetitions, **kwargs)
                self.assertIsInstance(avg_time, float)
    def test_readme_exists():
        '''
        Test 1
        '''
        assert os.path.isfile("README.md"), "README.md file missing!"

    def test_readme_contents():
        '''
        Test 2
        '''
        readme = open("README.md", "r")
        readme_words = readme.read().split()
        readme.close()
        assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

    def test_readme_proper_description():
        '''
        Test 3
        '''
        READMELOOKSGOOD = True
        f = open("README.md", "r")
        content = f.read()
        f.close()
        for c in README_CONTENT_CHECK_FOR:
            if c not in content:
                READMELOOKSGOOD = False
                pass
        assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

    def test_readme_file_for_formatting():
        '''
        Test 4
        '''
        f = open("README.md", "r")
        content = f.read()
        f.close()
        assert content.count("#") >= 10
                
if __name__ == '__main__':
    unittest.main()


