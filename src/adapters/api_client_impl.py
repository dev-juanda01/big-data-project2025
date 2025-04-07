import requests
from typing import List
from core.entities.data_record import DataRecord
from ports.api_client import ApiClient

class ApiClientImpl(ApiClient):
    def fetch_data(self) -> List[DataRecord]:
        response = requests.get('https://api.escuelajs.co/api/v1/products')
        response.raise_for_status()
        json_data = response.json()
        data = [
            DataRecord(
                d['id'],
                d['title'],
                d['price'],
                d['description'],
                d['category'],
                d['images'],
            )
            for d in json_data
        ]
        return data