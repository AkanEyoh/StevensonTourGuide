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

class TestBuilding5(unittest.TestCase):

    def test_sameFloor(self):
        # floor 1
        self.assertEqual(directions('5116', '5119'), exp('tkr destr'))
        self.assertEqual(directions('5115', '5114'), exp('tkr destl'))
        self.assertEqual(directions('5117', '5134'), exp('tkl destr'))

        # floor 2
        self.assertEqual(directions('5234', '5216'), exp('wstr destl'))
        self.assertEqual(directions('5233B', '5215'), exp('tkl destr'))
        self.assertEqual(directions('5212', '5211'), exp('tkr destr'))
        self.assertEqual(directions('5200B', '5215'), exp('wstr destl'))

        # floor 3
        self.assertEqual(directions('5322', '5321'), exp('wstr destr'))
        self.assertEqual(directions('5317', '5326'), exp('tkr tkl destl'))
        self.assertEqual(directions('5308', '5307'), exp('tkr destr'))
        self.assertEqual(directions('5320', '5319'), exp('tkr destr'))

        # floor 4
        self.assertEqual(directions('5433', '5423'), exp('wstr destr'))
        self.assertEqual(directions('5421', '5419'), exp('tkr destr'))
        self.assertEqual(directions('5401', '5435'), exp('wstr deststr'))

        # floor 5
        self.assertEqual(directions('5523', '5521'), exp('tkr destr'))
        self.assertEqual(directions('5519', '5517'), exp('tkr destr'))
        self.assertEqual(directions('5522', '5502'), exp('tkl destl'))
        self.assertEqual(directions('5503', '5501'), exp('tkr destr'))

        # floor 6
        self.assertEqual(directions('5624', '5622'), exp('tkl destl'))
        self.assertEqual(directions('5623', '5621'), exp('tkr destr'))
        self.assertEqual(directions('5619', '5617'), exp('tkr destr'))
        self.assertEqual(directions('5607', '5605'), exp('tkr destr'))

        # floor 7
        self.assertEqual(directions('5724', '5721'), exp('tkl destr'))
        self.assertEqual(directions('5722', '5719'), exp('tkl destr'))
        self.assertEqual(directions('5707', '5705'), exp('tkr destr'))
        self.assertEqual(directions('5703', '5712'), exp('wstr destr'))

        # floor 8
        self.assertEqual(directions('5822', '5821'), exp('tkl destr'))
        self.assertEqual(directions('5819', '5817'), exp('tkr destr'))
        self.assertEqual(directions('5814', '5812'), exp('tkl destl'))
        self.assertEqual(directions('5805', '5803'), exp('tkr destr'))

        # floor 9
        self.assertEqual(directions('5924', '5922'), exp('tkl destl'))
        self.assertEqual(directions('5923', '5921'), exp('tkr destr'))
        self.assertEqual(directions('5919', '5917'), exp('tkr destr'))
        self.assertEqual(directions('5901', '5902'), exp('tkl destr'))

        # floor 10 is the roof, so no directions needed

        def test_betweenFloorStairs(self):
            switchToStairs()
            self.assertEqual(directions('5115', '5215'), exp('tkr Ts,5-1-2,r u1 tkl destl'))
            self.assertEqual(directions('5215', '5317'), exp('tkr Ts,5-2-2,r u1 tkl destl'))
            self.assertEqual(directions('5421', '5320'), exp('tkl Ts,5-4-1,str l1 tkl tkr destr'))
            self.assertEqual(directions('5605', '5320'), exp('tkl Ts,5-6-2,l l3 tkl destl'))
            self.assertEqual(directions('5707', '5321'), exp('tkl Ts,5-7-2,l l4 tkl destl'))
            self.assertEqual(directions('5822', '5121'), exp('tkr Ts,5-8-1,str l7 wstr destl'))

        def test_betweenFloorElevator(self):
            switchToElevator()
            self.assertEqual(directions('5207', '5317'), exp('tkl Te,5-2,l e3 tkl destl'))
            self.assertEqual(directions('5423', '5622'), exp('tkl tkl Te,5-2,l e6 tkr tkr destl'))
            self.assertEqual(directions('5601', '5307'), exp('tkl Te,5-6,l e3 tkr destr'))
            self.assertEqual(directions('5705', '5307'), exp('tkl Te,5-7,l e3 tkr destr'))
            self.assertEqual(directions('5823', '5423'), exp('tkl tkl Te,5-8,l e4 tkr tkr destr'))
            self.assertEqual(directions('5906', '5823'), exp('tkr Te,5-9,l e8 tkl destl'))


class TestBuilding6(unittest.TestCase):

    def test_sameFloor(self):
        # floor 1
        self.assertEqual(directions('6109', '6119'), exp('tkr destr'))
        self.assertEqual(directions('6105', '6109'), exp('tkr destr'))
        self.assertEqual(directions('6109', '6114'), exp('tkr destl'))

        # floor 2
        self.assertEqual(directions('6206', '6209'), exp('tkl destr'))
        self.assertEqual(directions('6210', '6209'), exp('tkr destl'))

        # floor 3
        self.assertEqual(directions('6325', '6321'), exp('tkl destl'))
        self.assertEqual(directions('6317', '6313'), exp('tkl destl'))
        self.assertEqual(directions('6328', '6322'), exp('wstr destr'))
        self.assertEqual(directions('6308', '6313'), exp('tkl destr'))

        # floor 4
        self.assertEqual(directions('6414', '6412'), exp('tkr destr'))
        self.assertEqual(directions('6416', '6410'), exp('tkr destr'))
        self.assertEqual(directions('6422', '6408'), exp('tkr destr'))

        # floor 5
        self.assertEqual(directions('6516', '6514'), exp('tkr destr'))
        self.assertEqual(directions('6512', '6510'), exp('tkr destr'))
        self.assertEqual(directions('6525', '6508'), exp('wstr destr'))
        self.assertEqual(directions('6502', '6506'), exp('tkl destl'))

        # floor 6
        self.assertEqual(directions('6638', '6640'), exp('tkr destr'))
        self.assertEqual(directions('6613', '6609'), exp('tkl destl'))
        self.assertEqual(directions('6605', '6601'), exp('tkl destl'))
        self.assertEqual(directions('6620', '6614'), exp('tkr destr'))

        # floor 7
        self.assertEqual(directions('6719', '6717'), exp('tkl destl'))
        self.assertEqual(directions('6715', '6713'), exp('tkl destl'))
        self.assertEqual(directions('6711', '6709'), exp('tkl destl'))
        self.assertEqual(directions('6703', '6701'), exp('tkl destl'))

        # floor 8
        self.assertEqual(directions('6839', '6841'), exp('tkr destr'))
        self.assertEqual(directions('6829', '6831'), exp('tkr destr'))
        self.assertEqual(directions('6825', '6827'), exp('tkr destr'))
        self.assertEqual(directions('6821', '6819'), exp('tkl destl'))

        # floor 9
        self.assertEqual(directions('6908', '6906'), exp('tkr destr'))
        self.assertEqual(directions('6914', '6912'), exp('tkr destr'))
        self.assertEqual(directions('6907G', '6907H'), exp('tkr destr'))
        self.assertEqual(directions('6901', '6930'), exp('wstr tkr deststr'))

        # floor 10
        self.assertEqual(directions('61024', '61014'), exp('tkr destr'))
        self.assertEqual(directions('61008', '61006'), exp('tkr tkr destr'))


        def test_betweenFloorStairs(self):
            switchToStairs()


        def test_betweenFloorElevator(self):
            switchToElevator()


if __name__ == '__main__':
    unittest.main()
