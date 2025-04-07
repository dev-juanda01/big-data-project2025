from abc import ABC, abstractmethod
from typing import List
from core.entities.data_record import DataRecord

class Database(ABC):
    @abstractmethod
    def save_data(self, data: List[DataRecord]):
        pass

    @abstractmethod
    def get_data(self) -> List[DataRecord]:
        pass