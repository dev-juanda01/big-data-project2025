from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DataRecord:
    id: int
    title: str
    price: float
    description: str
    category: Dict[str, any]
    images: List[str]