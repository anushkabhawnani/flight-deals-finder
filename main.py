from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch(data_manager)
notification_manager = NotificationManager(flight_search)