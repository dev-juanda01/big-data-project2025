from abc import ABC, abstractmethod
from typing import List
from src.core.entities.data_record import DataRecord

class ApiClient(ABC):
    @abstractmethod
    def fetch_data(self) -> List[DataRecord]:
        pass