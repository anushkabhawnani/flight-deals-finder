import datetime
import os
from dotenv import find_dotenv, load_dotenv
import requests
from datetime import *
from data_manager import DataManager

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')

class FlightSearch:

    def __init__(self, data_manager: DataManager):
        self.sheety = data_manager
        self.token = self.get_token()
        self.get_flight_info()
        self.find_cheapest_tickets()

    def get_token(self):

        # GET ACCESS TOKEN TO ACCESS THE AMADEUS API LATER

        body = {
            "grant_type": "client_credentials"
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(TOKEN_ENDPOINT, data=body, headers=header, auth=(AMADEUS_API_KEY, AMADEUS_API_SECRET))
        if response.status_code == 200:
            access_token = response.json().get("access_token")
        else:
            raise Exception(response.json().get("error_description"))
        return access_token

    def get_flight_info(self):

        # GET THE DATE OF DEPARTURE AND RETURN DATE

        tommorrow = datetime.now() + timedelta(days=1)
        six_months_from_today = datetime.now() + timedelta(days=180)

        # SET THE FLIGHT PARAMETERS

        self.result = {}
        self.price_list = []
        flight_params = {
            'originLocationCode': 'BOM',
            'departureDate': tommorrow.strftime('%Y-%m-%d'),
            'returnDate': six_months_from_today.strftime('%Y-%m-%d'),
            'adults': 1,
            'currencyCode': 'INR',
            'max': 1,
            'nonStop': 'true'
        }

        # ACCESS THE API TO GET A FLIGHT FOR EVERY DESTINATION CODE PRESENT IN THE GOOGLE SHEET

        for destination in self.sheety.get_iata_code():

            flight_params['destinationLocationCode'] = destination

            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(url=FLIGHT_ENDPOINT, params=flight_params, headers=headers)
            # response.raise_for_status()
            self.result[destination] = response.json()

            # APPEND ONLY THE DATA THAT WE REQUIRE IN A SEPARATE LIST TO MAKE IT EASY TO UNDERSTAND LATER ON

            for item in self.result[destination]['data']:

                self.price_list.append({
                    'IATA': destination,
                    'PRICE': item['price']['total'],
                    'fromDate': item['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0],
                    'toDate': item['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]
                })

    def find_cheapest_tickets(self):
        cheapest_tickets = []

        # MAKE SURE THAT THERE IS A FLIGHT FOR ANY OF THE GIVEN DESTINATION CODES PRESENT IN THE GOOGLE SHEET AND MATCH TO SEE IF THE TICKET PRICE FOUND IF LESS THAN THE TICKET PRICE DESIRED THEN ADD THEM TO A SEPARATE LIST WITH ALL THE NECESSARY KEYS AND VALUES SO IT IS EASIER TO UNDERSTAND LATER ON

        for destination in self.sheety.get_lowest_price():

            for item in self.price_list:
                if destination['IATA'] in item['IATA'] and float(destination['PRICE']) > float(item['PRICE']):
                    cheapest_tickets.append({
                        'IATA': destination['IATA'],
                        'ticket_price': item['PRICE'],
                        'cheapest_ticket': destination['PRICE'],
                        'fromDate': item['fromDate'],
                        'toDate': item['toDate']
                    })

        # RETURN THE VALUE FOR USAGE IN A DIFFERENT MODULE

        return cheapest_tickets

