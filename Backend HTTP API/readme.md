# Delivery Fee Calculator HTTP API

This is a backend HTTP API that calculates the delivery fee for a given order. The delivery fee is calculated based on several factors, including the cart value, delivery distance, number of items, and time of order.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- Flask

### Installing

1. Download the files directly or clone the repository to your local machine.
2. Install the required dependencies:

```bash
pip install flask

```

## Running the Application

You can run the application either from the terminal or from any IDE, e.g., PyCharm or Visual Studio.

### Terminal

Navigate to the directory containing the `server.py` file and run the following command:

```bash
python server.py

```

The application will start and listen for requests at `http://localhost:5000`.

### PyCharm/VSCode or other IDE

1.  Open the project folder in your preferred IDE.
2.  Right-click the `server.py` file in the Project tool window and select ‘Run server’.
3.  The application will start and listen for requests at `http://localhost:5000`.
4.  Select the `test.py` file where you can run the default tests and you can also customize the tests as per your needs.


## API Endpoints

### POST /calculate_fee

Calculates the delivery fee for a given order.

#### Parameters

-   `cart_value`: The total value of the cart in cents (integer).
-   `delivery_distance`: The delivery distance in meters (integer).
-   `number_of_items`: The number of items in the cart (integer).
-   `time`: The time of the order in UTC (string, format: ‘YYYY-MM-DDTHH:MM:SSZ’).

#### Response

Returns a JSON object with the calculated delivery fee:

```json
{
    "delivery_fee": Integer
}

```

Here is an example of a request payload and a corresponding response for the `/calculate_fee` endpoint. Here’s an example:

Here's an example of how to use the `/calculate_fee` endpoint:

#### Request

```json

{
    "cart_value": 10000,
    "delivery_distance": 3000,
    "number_of_items": 13,
    "time": "2024-01-19T18:00:00Z"
}

```

#### Response

```json
{
    "delivery_fee": 1404
}

```

In this example, the request payload includes a `cart_value` of 10000 cents (or 100 euros), a `delivery_distance` of 3000 meters, `number_of_items` as 13, and the `time` of the order. The response includes the calculated `delivery_fee` of 1404 cents or 14.04 euros. Please refer to the Testing Scenario 5 in the `test.py` file for the detailed breakdown of calculation of delivery_fee.

## Running the Tests

## Running the Tests

The tests for this project are written using Python's built-in `unittest` module. They are located in the `test.py` file.

To run the tests, navigate to the directory containing the `test.py` file and run the following command:

```bash
python test.py

```
The tests cover several scenarios to ensure the `calculate_fee` function works as expected. Here are the scenarios tested:

1.  **Scenario 1**: Tests the calculation of the delivery fee when the cart value is less than 10€, the delivery distance is 2235 meters, the number of items is 4, and the time is not during the Friday rush. The expected delivery fee is 710 cents = 7.10 euros.
    
2.  **Scenario 2**: Tests the calculation of the delivery fee when the cart value is greater than or equal to 200€. The expected delivery fee is 0 cents = 0 €, regardless of the other parameters.
    
3.  **Scenario 3**: Tests the calculation of the delivery fee when the delivery distance is 5000 meters and the number of items is 14. The expected delivery fee is 1500 cents = 15€, which is the maximum delivery fee that can be charged. 
    
4.  **Scenario 4**: Tests the calculation of the delivery fee during the Friday rush. The expected delivery fee is 720 cents = 7.2€.
    
5.  **Scenario 5**: Tests the calculation of the delivery fee with a large number of items during the Friday rush. The expected delivery fee is 1404 cents = 14.04€.
    

Each test sends a POST request to the `/calculate_fee` endpoint with a sample request payload, checks that the response status code is 200 (OK), checks that the response data includes the `delivery_fee` key, and checks that the calculated delivery fee matches the manually calculated or actual delivery fee.

## Built With

-   Flask - The web framework used

## Authors

-   Muhammad Ajlal

## License

This project is licensed under the XYZ License - see the LICENSE.md file for details

```

I have tried to create a readme.md in a professional style to showcase that I use best software engineering paractices. This `README.md` provides a brief overview of our project, instructions on how to install and run this backend application, details about the API endpoint, and information on how to run the tests.
```
