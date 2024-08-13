"""
This script extracts the data from the EIA API.
"""

import os
import json
import logging
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # load variables from .env


class Extract:
    def __init__(self, api_key: str, date_start: datetime, date_end: datetime):
        self.api_key = api_key
        self.date_start = date_start
        self.date_end = date_end
        self.url = "https://api.eia.gov/v2/petroleum/pnp/crq/data/"

    def get_request(self, params: dict, headers: dict) -> dict:
        logging.info(f"Getting data from {self.url}")
        response = requests.get(self.url, params=params, headers=headers)
        logging.info(f"Response: {response.text}")
        return response.json()

    @staticmethod
    def date_to_month(date: datetime) -> str:
        logging.info(f"Converting date {date} to month")
        month = date.strftime("%Y-%m")
        logging.info(f"Month: {month}")

    def get_oil_data(self) -> dict:
        logging.info(f"Getting oil data from {self.date_start} to {self.date_end}")
        month_start = self.date_to_month(self.date_start)
        month_end = self.date_to_month(self.date_end)

        x_params = {
            "frequency": "monthly",
            "data": ["value"],
            "facets": {},
            "start": month_start,
            "end": month_end,
            "sort": [{"column": "period", "direction": "desc"}],
            "offset": 0,
            "length": 5000,
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "x-params": json.dumps(x_params),
        }

        params = {
            "api_key": self.api_key,
        }

        response = self.get_request(params, headers)
        logging.info(f"response: {response}")

        return response

    def write_to_file(self, data: dict, filename: str):
        logging.info(f"Writing data to {filename}")
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    extract=Extract(os.environ["EIA_API_kEY"], datetime(2024, 1, 1), datetime(2024, 5, 1))

    oil_data = extract.get_oil_data()
    

    extract.write_to_file(oil_data, "oil_data.json")
