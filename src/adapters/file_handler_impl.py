import pandas as pd
import json
from typing import List
from src.core.entities.data_record import DataRecord
from src.ports.file_handler import FileHandler


class FileHandlerImpl(FileHandler):
    def generate_sample(self, data: List[DataRecord]):
        df = pd.DataFrame(
            [
                {
                    'id': record.id,
                    'title': record.title,
                    'price': record.price,
                    'description': record.description,
                    'category': json.dumps(record.category),
                    'images': json.dumps(record.images),
                }
                for record in data
            ]
        )
        df.to_excel('src/static/xlsx/ingestion.xlsx', index=False)

    def generate_audit(self, api_data: List[DataRecord], db_data: List[DataRecord]):
        api_ids = {record.id for record in api_data}
        db_ids = {record.id for record in db_data}
        differences = api_ids.symmetric_difference(db_ids)
        with open('src/static/auditoria/ingestion.txt', 'w') as f:
            f.write(f'Registros en API: {len(api_data)}\n')
            f.write(f'Registros en DB: {len(db_data)}\n')
            f.write(f'Diferencias (IDs): {differences}\n')
