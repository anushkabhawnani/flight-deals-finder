
# Flight Deals Finder

A python code written so as to find the cheapest flights for a given destination with a budget for the tickets and destination IATA codes that were input in a Google Sheets document. This is a capstone project assigned by Angela Yu as part of her course, 100 Days of Code, and this is my method of solving it!




## How it works

This file access the Google Sheet document in data_manager.py and finds the IATA codes and the budget limits for each ticket. 

It uses that information to find flights that have the same IATA codes as mentioned in the Google Sheet using the Amadeus API, this all is done in flight_search.py. It additionally gets the flight with ticket fares less than the budget provided and returns them as a list.

In notification_manager.py, the files are then brought together to send a Whatsapp alert using Twilio API, whenever it finds a flight that fits our given condition.

Finally, all of these modules were brought together in main.py for a smooth functioning.


## Links to APIs used

 - [Sheety API](https://sheety.co/)
 - [Amadeus API](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference)
 - [Twilio API](https://www.twilio.com/docs/whatsapp/quickstart/python)

