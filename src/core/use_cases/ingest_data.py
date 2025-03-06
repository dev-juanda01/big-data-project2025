class IngestData:
    def __init__(self, api_client, database, file_handler):
        self.api_client = api_client
        self.database = database
        self.file_handler = file_handler

    def execute(self):
        data = self.api_client.fetch_data()
        self.database.save_data(data)
        self.file_handler.generate_sample(data)
        self.file_handler.generate_audit(data, self.database.get_data())