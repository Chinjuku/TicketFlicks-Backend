from django.test import TestCase
from django_seed import Seed
from .models import Theatre, Place

# class SeedTestCase(TestCase):
#     def setUp(self):
#         seeder = Seed.seeder()

#         seeder.add_entity(Theatre, 5)
#         seeder.add_entity(Place, 12, {
#             'seat_num': lambda x: f"A{x}",  # Generating seat numbers like "A1", "A2", ...
#             'theatre': "3ac4dbe5-a168-4035-a8b7-7a88b3c95b94",
#             'type': 'normal'
#         })

#         inserted_pks = seeder.execute()

#     def test_theatre_count(self):
#         # Verify that the correct number of theatres are seeded
#         theatre_count = Theatre.objects.count()
#         self.assertEqual(theatre_count, 5)

#     def test_place_count(self):
#         # Verify that the correct number of places are seeded
#         place_count = Place.objects.count()
#         self.assertEqual(place_count, 12)

#     def test_place_seat_numbers(self):
#         # Verify that the seat numbers are generated correctly
#         places = Place.objects.all()
#         for place in places:
#             self.assertTrue(place.seat_num.startswith("A"))  # Verify seat numbers start with "A"

    # Add more test cases as needed

