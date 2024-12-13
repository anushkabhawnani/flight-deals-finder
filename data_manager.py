import os
from dotenv import find_dotenv, load_dotenv
import requests

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SHEETY_USERNAME = os.getenv('SHEETY_USERNAME_LONG')
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices'
sheety_username = os.getenv('sheety_username')
sheety_password = os.getenv('sheety_password')

class DataManager:

    def __init__(self):
        self.response = requests.get(url=SHEETY_ENDPOINT, auth=(sheety_username, sheety_password))
        self.result = self.response.json()
        self.get_iata_code()
        self.get_lowest_price()
        self.get_emails()

    def get_iata_code(self):
        iataCode = []

        # RETRIEVING IATA CODE FOR THE LIST OF PLACES WE WANT TO VISIT

        for item in self.result['prices']:
            iataCode.append(item['iataCode'])
        return iataCode

    def get_lowest_price(self):
        lowestPrice = []

        # RETRIEVING THE LOWEST PRICE VALUES WE NEED TO FIND OUR TICKETS UNDER

        for item in self.result['prices']:
            lowestPrice.append({
                'IATA': item['iataCode'],
                'PRICE': item['lowestPrice'],
            })
        return lowestPrice

    def get_emails(self):
        emails = []
    
        # GET EMAIL AND NAMES OF EACH USER THAT REGISTERS FOR THE SUBSCRIPTION PLAN
    
        response = requests.get(url=SHEETY_ENDPOINT_USERS, auth=(sheety_username, sheety_password))
        result = response.json()
    
        for user in result['users']:
            emails.append({
                'firstName': user['whatIsYourFirstName?'],
                'lastName': user['whatIsYourLastName?'],
                'emailAddress': user['whatIsYourEMailAddress?']
            })
        return emails
