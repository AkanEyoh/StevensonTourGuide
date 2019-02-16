import shortest_path
import functools

def direction_string(direction_arr):
    """ Human readable string from array of directions """
    return functools.reduce(lambda x, y: x + ' ' + y, direction_arr) 

def compare_directions(actual, correct):
    print('Comparing {} to {}'.format(direction_string(actual), direction_string(correct)))
    identical = True

    for elem_actual, elem_correct in zip(actual, correct):
        if elem_actual != elem_correct:
            print('# Error! Expected {} but received {}'.format(elem_actual, elem_correct))
            identical = False

    return identical

class Test:
   def __init__(self, test_type, test_room_pairs, expected_output):
        self.test_type = test_type
        self.room_pairs = test_room_pairs
        self.expected_output = expected_output
        self.total_failed = 0

   def run_test(self):
       print('\n~~~~~~~~~~~~~~\n~~~ NOW TESTING: {}\n~~~~~~~~~~~~~~\n\n'.format(self.test_type))
       for room_pair, expected in zip(self.room_pairs, self.expected_output):
           try:
               actual = shortest_path.get_directions(room_pair[0], room_pair[1])
               if not compare_directions(actual, expected):
                   print('### SUBTEST FAILED')
                   self.total_failed += 1
               else:
                   print('$$$ SUBTEST PASSED\n')

           except:
               print('### SUBTEST FAILED - COULD NOT COMPUTE PATH')
               self.total_failed += 1

       if self.total_failed > 0:
           print('#####\n### TEST {} FAILED. {} OUT OF {} FAILING\n#####'.format(self.test_type, self.total_failed, len(self.room_pairs)))
       else:
           print('$$$$$\n$$$ TEST {} PASSED. ALL {} CASES PASSING\n$$$$$'.format(self.test_type, len(self.room_pairs)))

same_hallway = Test('Same Hallway', [['1120', '1122'], ['1120', '1117']], [['Take a right.', 'Your destination is straight ahead.'], ['Take a left.', 'Your destination is on the right.']])

same_hallway.run_test()
