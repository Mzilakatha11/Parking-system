import unittest
from new_parking import Parking_Hours  

class TestParkingHours(unittest.TestCase):
    
    def setUp(self):
        self.park = Parking_Hours(name="John Doe", car_registration_number="ABC123")

    
    def test_is_parking1(self):
        self.assertTrue(self.park.hours_parking(0)== None)

    def test_is_parking2(self):
        self.assertTrue(self.park.yearly_parking(-100)== None)

    def test_hours_parking_one_hour(self):
        self.assertEqual(self.park.hours_parking(1), 14)
        self.assertEqual(self.park.hours_parking(2), 24)
        self.assertEqual(self.park.hours_parking(5), 64) 
        self.assertEqual(self.park.hours_parking(8), 101)

    def test_daily_parking(self):
        self.assertEqual(self.park.daily_parking(1), 156)
        self.assertEqual(self.park.daily_parking(2), 312)
        self.assertEqual(self.park.daily_parking(5), 780) 

    def test_monthly_parking(self):
        self.assertEqual(self.park.monthly_parking(1), 3336)  
        self.assertEqual(self.park.monthly_parking(4), 13344) 
        self.assertEqual(self.park.monthly_parking(5), 11680) 

    def test_yearly_parking(self):
        self.assertEqual(self.park.yearly_parking(1), 35032) 
        self.assertEqual(self.park.yearly_parking(3), 115096)  
        self.assertEqual(self.park.yearly_parking(6), 160192) 
    
if __name__ == "__main__":
    unittest.main()