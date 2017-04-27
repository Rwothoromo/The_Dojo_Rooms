import unittest
from dojo.the_dojo_rooms import *

class TestDojo(unittest.TestCase):
    def test_create_room_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)

        blue_room = ["Blue"]
        blue_room_type = "office"

        blue_office = dojo.create_room(blue_room_type, blue_room)
        self.assertTrue(blue_office)

        new_room_count = len(dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_multiple_rooms_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        multiple_rooms = ["Red", "Green", "Orange"]
        multiple_rooms_type = "office"

        multiple_offices = dojo.create_room(multiple_rooms_type, multiple_rooms)
        self.assertTrue(multiple_offices)

        new_room_count = len(dojo.all_rooms)
        room_increment = len(multiple_rooms)
        self.assertEqual(new_room_count - initial_room_count, room_increment)

    def test_add_person_successfully(self):
        dojo = Dojo()

        person_name1 = "Eli1 Rwt1"
        person_type1 = "STAFF"

        person_name2 = "Eli2 Rwt2"
        person_type2 = "FELLOW"

        person_name3 = "Eli3 Rwt3"
        person_type3 = "Other"

        add_person1 = dojo.add_person(person_name1, person_type1)
        add_person2 = dojo.add_person(person_name2, person_type2, 'Y')
        add_person3 = dojo.add_person(person_name3, person_type3, 'N')

        self.assertTrue(add_person1)
        self.assertTrue(add_person2)
        self.assertFalse(add_person3)

    def test_print_room_successfully(self):
        dojo = Dojo()

        multiple_rooms = ["Blue", "Green", "Orange"]
        multiple_rooms_type = "office"
        multiple_offices = dojo.create_room(multiple_rooms_type, multiple_rooms)

        multiple_livingspaces = dojo.create_room("livingspace", ["Python", "Django"])

        person_name1 = "Eli1 Rwt1"
        person_type1 = "STAFF"
        add_person1 = dojo.add_person(person_name1, person_type1)

        person_name2 = "Eli2 Rwt2"
        person_type2 = "FELLOW"
        add_person2 = dojo.add_person(person_name2, person_type2, 'Y')

        person_name3 = "Eli3 Rwt3"
        person_type3 = "FELLOW"
        add_person3 = dojo.add_person(person_name3, person_type3, 'N')

        person_name4 = "Eli4 Rwt4"
        person_type4 = "FELLOW"
        add_person4 = dojo.add_person(person_name4, person_type4, 'Y')

        person_name5 = "Eli5 Rwt5"
        person_type5 = "STAFF"
        add_person5 = dojo.add_person(person_name5, person_type5)

        room_name1 = "Blue"
        rooms_print1 = dojo.print_room(room_name1)
        self.assertTrue(rooms_print1)

        room_name2 = "Green"
        rooms_print2 = dojo.print_room(room_name2)
        self.assertTrue(rooms_print2)

        room_name3 = "A12" #inexistent room
        rooms_print3 = dojo.print_room(room_name3)
        self.assertFalse(rooms_print3)

        room_name4 = 4 #wrong value
        self.assertRaises(TypeError, dojo.print_room, room_name4)

        room_name5 = "Orange"
        rooms_print5 = dojo.print_room(room_name5)
        self.assertTrue(rooms_print5)

if __name__ == '__main__':
    unittest.main()
