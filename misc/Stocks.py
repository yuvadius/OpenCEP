from datetime import datetime

from base.DataFormatter import DataFormatter
from misc.Utils import str_to_number

METASTOCK_7_COLUMN_KEYS = [
    "Stock Ticker",
    "Date",
    "Opening Price",
    "Peak Price",
    "Lowest Price",
    "Close Price",
    "Volume"]

METASTOCK_EVENT_TYPE_KEY = "Stock Ticker"
METASTOCK_EVENT_TIMESTAMP_KEY = "Date"


class MetastockDataFormatter(DataFormatter):
    """
    A data formatter implementation for a stock event stream, where each event is given as a string in metastock 7
    format.
    """
    def parse_event(self, raw_data: str):
        """
        Parses a metastock 7 formatted string into an event.
        """
        event_attributes = raw_data.replace("\n", "").split(",")
        for j in range(len(event_attributes)):
            event_attributes[j] = str_to_number(event_attributes[j])
        return dict(zip(METASTOCK_7_COLUMN_KEYS, event_attributes))

    def get_event_type(self, event_payload: dict):
        """
        The type of a stock event is equal to the stock ticker (company name).
        """
        return event_payload[METASTOCK_EVENT_TYPE_KEY]

    def get_event_timestamp(self, event_payload: dict):
        """
        The event timestamp is represented in metastock 7 using a YYYYMMDDhhmm format.
        """
        timestamp_str = str(event_payload[METASTOCK_EVENT_TIMESTAMP_KEY])
        return datetime(year=int(timestamp_str[0:4]), month=int(timestamp_str[4:6]), day=int(timestamp_str[6:8]),
                        hour=int(timestamp_str[8:10]), minute=int(timestamp_str[10:12]))
