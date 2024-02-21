# Importing necessary libraries
import unittest
import server
import json


class TestServer(unittest.TestCase):
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_calculate_fee(self):
        # Defining sample request payloads below and testing them

        # Testing Scenario 1 (it should calculate the delivery fee = 210 + 500 = 710 cents)
        data = {
            'cart_value': 790,  # surcharge = 10-7.9 = 2.1 * 100 = 210
            'delivery_distance': 2235,  # delivery_fee += 2+2+1 = 5 * 100 = 500
            'number_of_items': 4,  # item_surcharge = 0
            'time': '2024-01-15T13:00:00Z'  # Not Friday Rush so no multiplication by 1.2x
        }

        # Testing Scenario 2 (it should calculate the delivery fee = 0 because cart_value >= 200 euros or (20000 cents))
        """data = {
            'cart_value': 20000,  # cart_value >= 200 euros or (20000 cents)
            'delivery_distance': 2235,
            'number_of_items': 4,
            'time': '2024-01-15T13:00:00Z'
        }"""

        # Testing Scenario 3 (it should calculate the delivery fee = 1500 because its maximum delivery fee we can
        # charge If we did not have a cap for maximum deliver_fee = 1500 then the actual fee would be 1000 + 620 = 1620
        """data = {
            'cart_value': 10000,  # cart_value_euros = 100, so no surcharge
            'delivery_distance': 5000,  # delivery_fee += 2+(8*1) = 10 * 100 = 1000
            'number_of_items': 14,  # item_surcharge = (10*0.50) + 1.20 = 6.20 * 100 = 620
            'time': '2024-01-15T13:00:00Z'  # Not Friday Rush so no multiplication by 1.2x
        }"""

        # Testing Scenario 4 (it should calculate the delivery fee = (600)*1.2 = 720
        """data = {
            'cart_value': 10000,  # cart_value_euros = 100, so no surcharge
            'delivery_distance': 3000,  # delivery_fee += 2+(4*1) = 6 * 100 = 600
            'number_of_items': 4,  # item_surcharge = 0
            'time': '2024-01-19T18:00:00Z'  # Its Friday Rush, so delivery_fee = (600)*1.2 = 720
        }"""

        # Testing Scenario 5 (it should calculate the delivery fee = (600 + 570) * 1.2 = 1404
        """data = {
            'cart_value': 10000,  # cart_value_euros = 100, so no surcharge
            'delivery_distance': 3000,  # delivery_fee += 2+(4*1) = 6 * 100 = 600
            'number_of_items': 13,  # item_surcharge = ((9 * 50 cents) + 1,20€) = 5.70 * 100 = 570
            'time': '2024-01-19T18:00:00Z'  # Its Friday Rush, so delivery_fee = (600 + 570)*1.2 = 1404
        }"""

        # Sending a POST request to the calculate_fee endpoint
        response = self.app.post('/calculate_fee', data=json.dumps(data), content_type='application/json')

        # Checking that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Checking that the response data returned by our API is correct
        response_data = json.loads(response.data)
        self.assertIn('delivery_fee', response_data)

        # Checking that the delivery_fee calculation is correct
        expected_delivery_fee = 710
        self.assertEqual(response_data['delivery_fee'], expected_delivery_fee)


if __name__ == '__main__':
    unittest.main()
