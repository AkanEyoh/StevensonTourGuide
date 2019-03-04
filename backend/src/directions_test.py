import functools
import unittest

import shortest_path
import locations

# get the directions between the rooms and convert into a string
def directions(start, end):
    direction_arr = shortest_path.get_directions(start, end)[0]
    return functools.reduce(lambda x, y: x + ' ' + y, direction_arr)


# more complicated expansion that cannot be accomplished solely with dictionary
def turnExpansion(expr):
    short = {'r': 'right.', 'l': 'left.', 'str': 'straight ahead.', 'e': 'elevator', 's': 'staircase'}
    pieces = expr.split(',')
    return 'Enter {}{} which will be on your {}'.format(short[pieces[0]], pieces[1], short[pieces[2]])


# expand directions relating to stairs
def stairExpansion(expr):
    shorthand = {'u': 'up', 'l': 'down'}
    firstChar = expr[0]
    multipleFlights = len(expr[1:]) > 1
    if multipleFlights:
        return 'Go {} {} floors.'.format(shorthand[firstChar], expr[1:])
    else:
        return 'Go {} 1 floor.'.format(shorthand[firstChar])
    

# expand shorthand for directions to actual directions
def exp(directions):
    shorthand = {'wstr': 'Walk straight ahead.', 'tkl': 'Take a left.', 'tkr': 'Take a right.', 'destl': 'Your destination is on the left.',
             'destr': 'Your destination is on the right.', 'deststr': 'Your destination is straight ahead.', 'tnl': 'Turn left.', 'tnr': 'Turn right.',
             }
    final = ''
    directions = directions.split(' ')
    for i in range(len(directions)):
        direction = directions[i]
        firstChar = direction[0]
        # turning-related direction
        if firstChar == 'T':
            final += turnExpansion(direction[1:])
        # stair-related direction
        elif firstChar in ['u', 'l']:
            final += stairExpansion(direction)
        # elevator-related direction
        elif firstChar == 'e':
            final += 'Head to floor {}.'.format(direction[1:])
        # enter/exit direction
        else:
            final += shorthand[directions[i]]
        if i != len(directions) - 1:
            final += ' '
    return final

# to use when toggling between whether stair-based or elevator-based directions are given
HIGH_STAIR_LENGTH = 10
LOW_STAIR_LENGTH = 1
ELEVATOR_LENGTH = 5

def switchToElevator():
    shortest_path.createPaths(HIGH_STAIR_LENGTH, ELEVATOR_LENGTH)

def switchToStairs():
    shortest_path.createPaths(LOW_STAIR_LENGTH, ELEVATOR_LENGTH)

class TestBuilding1(unittest.TestCase):
    
    def test_sameFloor(self):
        # floor 1
        self.assertEqual(directions('1122', '1120'), exp('wstr destl'))
        self.assertEqual(directions('1122', '1117'), exp('wstr destr'))
        self.assertEqual(directions('1120', '1117'), exp('tkl destr'))
        self.assertEqual(directions('1120', '1122'), exp('tkr deststr'))
        self.assertEqual(directions('1117', '1113'), exp('tkr destr'))
        self.assertEqual(directions('1117', '1110'), exp('tkr destl'))
       
        # floor 2
        self.assertEqual(directions('1224', '1210'), exp('tkl destl'))
        self.assertEqual(directions('1224', '1219'), exp('tkl destr'))
        self.assertEqual(directions('1206', '1219'), exp('tkr destl'))
        self.assertEqual(directions('1225', '1214'), exp('tkr destl'))
        self.assertEqual(directions('1232', '1220'), exp('tkl destl'))
        self.assertEqual(directions('1224', '1222'), exp('tkl destl'))

        # floor 3
        self.assertEqual(directions('1326', '1312'), exp('tkr destl'))
        self.assertEqual(directions('1326', '1308'), exp('tkr desl'))
        self.assertEqual(directions('1323', '1317'), exp('tkr destr'))
        self.assertEqual(directions('1326', '1324'), exp('wstr tnr deststr'))
        self.assertEqual(directions('1317', '1313'), exp('tkr destr'))
        self.assertEqual(directions('1307', '1321'), exp('tkl destl'))

        # floor 4
        self.assertEqual(directions('1428', '1413'), exp('tkl destr'))
        self.assertEqual(directions('1426', '1415'), exp('tkl destr'))
        self.assertEqual(directions('1424', '1417'), exp('tkl destr'))
        self.assertEqual(directions('1422', '1421'), exp('tkl destr'))
        self.assertEqual(directions('1420', '1401'), exp('tkl deststr'))
        self.assertEqual(directions('1412', '1410'), exp('tkl destl'))

        # floor 5
        self.assertEqual(directions('1532', '1505'), exp('tkl destr'))
        self.assertEqual(directions('1528', '1507'), exp('tkl destr'))
        self.assertEqual(directions('1526', '1511'), exp('tkl destr'))
        self.assertEqual(directions('1524', '1513'), exp('tkl destr'))
        self.assertEqual(directions('1533', '1502'), exp('tkr destl'))
        self.assertEqual(directions('1529', '1518'), exp('tkr destl'))

    def test_betweenFloorStairs(self):
        switchToStairs()
        self.assertEqual(directions('1103', '1219'), exp('tkl Ts,1-1-2,r u1 tkr destl'))
        self.assertEqual(directions('1120', '1224'), exp('tkl Ts,1-1-1,l u1 tkl destl'))
        self.assertEqual(directions('1206', '1110'), exp('tkl Ts,1-2-2,l l1 tkr destr'))
        self.assertEqual(directions('1232', '1122'), exp('tkl Ts,1-2-1,l l1 tkr deststr'))
        self.assertEqual(directions('1522', '1320'), exp('tkr Ts,1-5-1,r l2 wstr destl'))
        self.assertEqual(directions('1403', '1118'), exp('tkl Ts,1-4-1,l l3 tkr destr'))

    def test_betweenFloorElevator(self):
        switchToElevator()
        self.assertEqual(directions('1103', '1219'), exp('tkl Te,1-1,l e2 tkr destr'))
        self.assertEqual(directions('1120', '1224'), exp('tkl Te,1-1,r e2 tkl destr'))
        self.assertEqual(directions('1206', '1110'), exp('tkr Te,1-2,l e1 tkr destl'))
        self.assertEqual(directions('1232', '1122'), exp('tkl Te,1-2,r e1 tkl deststr'))
        self.assertEqual(directions('1522', '1320'), exp('tkr Te,1-5,l e3 tkr destl'))
        self.assertEqual(directions('1403', '1118'), exp('tkl Te,1-4,r e4 tkl destr'))


class TestBuilding2(unittest.TestCase):

    def test_sameFloor(self):
        # floor 1
        self.assertEqual(directions('2128', '2129'), exp('tkl destl'))
        self.assertEqual(directions('2129', '2128'), exp('tkr destr'))
        self.assertEqual(directions('2121', '2105'), exp('tkr destr'))
        self.assertEqual(directions('2104', '2105'), exp('tkl destr'))
        self.assertEqual(directions('2123', '2127'), exp('wstr deststr'))
        self.assertEqual(directions('2126', '2125'), exp('wstr destr'))

        # floor 2
        self.assertEqual(directions('2220', '2200A'), exp('tkr tkl deststr'))
        self.assertEqual(directions('2212', '2220'), exp('tkr tkr tkl destl'))

        # floor 3
        self.assertEqual(directions('2314', '2316'), exp('tkr destr'))
        self.assertEqual(directions('2318', '2320'), exp('tkr destr'))
        self.assertEqual(directions('2326', '2328'), exp('tkr destr'))
        self.assertEqual(directions('2332', '2336'), exp('tkr destr'))
        self.assertEqual(directions('2325', '2327'), exp('tkl destl'))
        self.assertEqual(directions('2337', '2332'), exp('tkl destr'))

        # floor 4
        self.assertEqual(directions('2414', '2416'), exp('tkr destr'))
        self.assertEqual(directions('2418', '2422'), exp('tkr destr'))
        self.assertEqual(directions('2442', '2426'), exp('tkr destr'))
        self.assertEqual(directions('2430', '2434'), exp('tkr destr'))
        self.assertEqual(directions('2438', '2442'), exp('tkr deststr'))
        self.assertEqual(directions('2401', '2425'), exp('tkl destl'))

        # floor 5
        self.assertEqual(directions('2501', '2514'), exp('tkl destr'))
        self.assertEqual(directions('2516', '2518'), exp('tkr destr'))
        self.assertEqual(directions('2520', '2522'), exp('tkr destr'))
        self.assertEqual(directions('2524', '2528'), exp('tkr destr'))
        self.assertEqual(directions('2530', '2534A'), exp('tkr destr'))
        self.assertEqual(directions('2523', '2522'), exp('tkr destl'))

        # floor 6
        self.assertEqual(directions('2603', '2605A'), exp('tkl deststr'))
        self.assertEqual(directions('2612', '2605'), exp('tkr destr'))

    def test_betweenFloorStairs(self):
        switchToStairs()
        self.assertEqual(directions('2129', '2220'), exp('tkl tkl Ts,2-1-1,r u1 tkl destr'))
        self.assertEqual(directions('2129', '2314'), exp('tkl tkl Ts,2-1-1,r u2 wstr destr'))
        self.assertEqual(directions('2105', '2426'), exp('wstr Ts,2-1-1,r u3 tkr destr'))
        self.assertEqual(directions('2430', '2129'), exp('tkl Ts,2-4-1,l l3 tkl tkr destr'))
        self.assertEqual(directions('2524', '2442'), exp('tkr Ts,2-5-2,r l1 tkr deststr'))
        self.assertEqual(directions('2336', '2121'), exp('tkl Ts,2-3-1,str l2 tkl tkr destl'))

    def test_betweenFloorElevator(self):
        switchToElevator()
        self.assertEqual(directions('2129', '2220'), exp('tkl Te,2-1,l e2 wstr destr'))
        self.assertEqual(directions('2129', '2314'), exp('tkl Te,2-1,l e3 wstr tkr destr'))
        self.assertEqual(directions('2105', '2426'), exp('wstr Te,2-1,str e4 wstr tkr destr'))
        self.assertEqual(directions('2430', '2129'), exp('tkl Te,2-4,l e1 wstr tkr destr'))
        self.assertEqual(directions('2524', '2442'), exp('tkl Te,2-5,l e4 wstr tkr deststr'))
        self.assertEqual(directions('2336', '2121'), exp('tkl Te,2-3,l e1 wstr tkr destl'))


# Building three is the floor with the Engineering Library and only has 1 floor
class TestBuilding3(unittest.TestCase):

    def test_sameFloor(self):
        self.assertEqual(directions('3218', '3210'), exp('tkl destl'))
        self.assertEqual(directions('3216', '3205'), exp('tkl destr'))
        self.assertEqual(directions('3212', '3222'), exp('tkr deststr'))
        self.assertEqual(directions('3210', '3212'), exp('tkr destr'))


# this building contains the two large lecture halls and has only two floors
class TestBuilding4(unittest.TestCase):

    def test_sameFloor(self):
        # floor 1
        self.assertEqual(directions('4219', '4221'), exp('tkl destl'))
        self.assertEqual(directions('4221', '4219'), exp('tkr destr'))

    def test_betweenFloorStairs(self):
        switchToStairs()
        self.assertEqual(directions('4221', '4327'), exp('tkr Ts,4-2-1,l u1 wstr deststr'))
        self.assertEqual(directions('4219', '4327'), exp('wstr Ts,4-2-1,l u1 wstr deststr'))
        

if __name__ == '__main__':
    unittest.main()
