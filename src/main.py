from src.adapters.api_client_impl import ApiClientImpl
from src.adapters.database_impl import DatabaseImpl
from src.adapters.file_handler_impl import FileHandlerImpl
from src.core.use_cases.ingest_data import IngestData
from src.utils.logger import logger

def main():
    api_client = ApiClientImpl()
    database = DatabaseImpl()
    file_handler = FileHandlerImpl()

    ingest_data = IngestData(api_client, database, file_handler)
    ingest_data.execute()
    logger.info("Ingestion process completed.")

if __name__ == "__main__":
    main()