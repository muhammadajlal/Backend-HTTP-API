# Importing necessary libraries
from datetime import datetime


def calculate_delivery_fee(data):
    # Extracting the data from payload
    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance']
    number_of_items = data['number_of_items']
    time = datetime.strptime(data['time'], '%Y-%m-%dT%H:%M:%SZ')

    # Implementing the delivery fee calculation logic here
    delivery_fee = 0  # Initialize the delivery fee to 0

    # cart_value
    cart_value_euros = cart_value / 100  # As we know that price is stored in cents so converting from cents to euros
    # If the cart value is less than 10 euros, add a surcharge
    # The surcharge is the difference between 10 euros and the cart value
    if cart_value_euros < 10:
        surcharge = (10 - cart_value_euros) * 100  # Adding surcharge to delivery_fee in cents
        delivery_fee += surcharge

    # delivery_distance
    # Calculate the delivery fee based on the delivery distance
    # The first 1000 meters cost 2 euros or 200 cents
    # Every additional 500 meters cost 1 euro or (100 cents)
    if delivery_distance <= 1000:
        delivery_fee += 2 * 100

    else:
        delivery_fee += 2 * 100  # Base fee for the first 1000 meters
        remaining_distance = delivery_distance - 1000
        delivery_fee += (remaining_distance // 500) * 100  # Additional fee for each 500 meters

        if remaining_distance % 500 > 0:
            delivery_fee += 1 * 100  # Additional fee for the remaining distance less than 500 meters

    # number_of_items
    # Add surcharge for number of items
    # If the number of items is 5 or more, add a 50 cent surcharge for each item above and including the fifth item
    # If the number of items is more than 12, add a bulk fee of 1.20 euros or (1200 cents)
    item_surcharge = 0  # initializing item_surcharge variable to 0

    if number_of_items >= 5:
        item_surcharge += (number_of_items - 4) * 50
    if number_of_items > 12:
        item_surcharge += 1.20 * 100

    delivery_fee += item_surcharge

    # Friday rush
    # During the Friday rush, the delivery fee will be multiplied by 1.2x
    # Check if it's Friday and between 3-7 PM UTC
    if time.weekday() == 4 and 15 <= time.hour < 19:  # Check if it's Friday and between 3-7 PM UTC
        delivery_fee *= 1.2
        # When I was testing the code, especially while multiplying the delivery_fee with 1.2 during
        # Friday Rush, I found that floating-point numbers can sometimes have small precision errors
        # causing the test to fail so that's why rounding the result to two decimal places.
        delivery_fee = round(delivery_fee)

    # The delivery is free when the cart value is equal or more than 200 euros or (20000 cents)
    if cart_value >= 200 * 100:
        return 0

    # The delivery fee can never be more than 15 euros or (1500 cents)
    delivery_fee = min(delivery_fee, 15 * 100)

    # Return the delivery fee
    return delivery_fee
