import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch
from twilio.rest import Client

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')

class NotificationManager:

    def __init__(self, flight_search: FlightSearch):
        self.cheapest_tickets = flight_search
        self.send_whatsapp()
        self.send_email()

    def send_whatsapp(self):

        # SEND A WHATSAPP MESSAGE FOR EVERY FLIGHT THAT HAS CHEAPER TICKETS THAN THE ONES MENTIONED SO THAT YOU CAN BE ALERTED WHENEVER THERE IS A CHEAPEST FLIGHT AVAILABLE

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        for ticket in self.cheapest_tickets.find_cheapest_tickets():
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=f'Low Price Alert! Only ₹{ticket['ticket_price']} to fly from BOM to {ticket['IATA']}, on {ticket['fromDate']} until {ticket['toDate']}',
                to=WHATSAPP_NUMBER
            )

    def send_email(self):

        # SEND AN EMAIL TO EACH USER IN THE SUBSCRIPTION PLAN FOR EACH TICKET THAT IS CHEAP

        for user in self.sheety.get_emails():

            for ticket in self.cheapest_tickets.find_cheapest_tickets():
                
                with smtplib.SMTP('smtp.gmail.com') as connection:
                    connection.starttls()

                    connection.login(user=my_email, password=email_password)

                    message = f'Subject: Low Price Alert!\n\nDear {user['firstName']} {user['lastName']},\n\nOnly ₹{ticket['ticket_price']} to fly from BOM to {ticket['IATA']}, on {ticket['fromDate']} until {ticket['toDate']}'

                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=user['emailAddress'],
                        msg=message.encode('utf-8').strip())

