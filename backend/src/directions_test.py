import functools
import unittest
from shortest_path import get_directions

shorthand = {'wstr': 'Walk straight ahead.', 'tkl': 'Take a left.', 'tkr': 'Take a right.', 'destl': 'Your destination is on the left.',
             'destr': 'Your destination is on the right.', 'deststr': 'Your destination is straight ahead.', 'tnl': 'Turn left.', 'tnr': 'Turn right.'}

# get the directions between the rooms and convert into a string
def directions(start, end):
    direction_arr = get_directions(start, end)
    return functools.reduce(lambda x, y: x + ' ' + y, direction_arr)

# expand shorthand for directions to actual directions
def exp(directions):
    final = ''
    directions = directions.split(' ')
    for i in range(len(directions)):
        final += shorthand[directions[i]]
        if i != len(directions) - 1:
            final += ' '
    return final


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

if __name__ == '__main__':
    unittest.main()
