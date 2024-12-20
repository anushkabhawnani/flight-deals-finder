
# Flight Deals Finder

A python code written so as to find the cheapest flights for a given destination with a budget for the tickets and destination IATA codes that were input in a Google Sheets document. Additionally, it collects the lists of users who wish to subscribe to this service and send them a mail as such! This is a capstone project assigned by Angela Yu as part of her course, 100 Days of Code, and this is my method of solving it!


## How it works

This file access the Google Sheet document in data_manager.py and finds the IATA codes and the budget limits for each ticket. 

It uses that information to find flights that have the same IATA codes as mentioned in the Google Sheet using the Amadeus API, this all is done in flight_search.py. It additionally gets the flight with ticket fares less than the budget provided and returns them as a list.

In notification_manager.py, the files are then brought together to send a Whatsapp alert using Twilio API and an e-mail using the smtplib, whenever it finds a flight that fits our given condition.

Finally, all of these modules were brought together in main.py for a smooth functioning.


## Links to APIs used

 - [Sheety API](https://sheety.co/)
 - [Amadeus API](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference)
 - [Twilio API](https://www.twilio.com/docs/whatsapp/quickstart/python)


## Google Sheet

![Flight Deals](https://github.com/user-attachments/assets/2a83c7af-a440-44ad-9ac3-2b9239a4a823)

## Demo

![Twilio Whatsapp](https://github.com/user-attachments/assets/f8f1ebc9-fae4-4578-9051-1dda5e051112)


![e-mail Demo](https://github.com/user-attachments/assets/9bec7427-7203-499e-b4a7-d8ec57055276)


