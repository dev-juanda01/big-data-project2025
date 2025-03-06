from abc import ABC, abstractmethod
from typing import List
from src.core.entities.data_record import DataRecord

class FileHandler(ABC):
    @abstractmethod
    def generate_sample(self, data: List[DataRecord]):
        pass

    @abstractmethod
    def generate_audit(self, api_data: List[DataRecord], db_data: List[DataRecord]):
        pass