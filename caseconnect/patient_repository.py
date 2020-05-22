from .data_reader.csv_data_reader import CSVDataReader
from .result_retriever import ResultRetriever

class PatientRepository:
    data_source = "./data/patients.csv"
    data_reader = CSVDataReader()
    result_retriever = ResultRetriever()
    patients = []

    def __init__(self, initialize=True):
        if initialize:
            self.initialize_data()
    
    def initialize_data(self):
        self.patients = self.data_reader.retrieve_patients(self.data_source)

    def retrieve_similar_patients(self, query_patient_id, n=8):
        return self.result_retriever.retrieve_result_for_patient_id(self.patients, query_patient_id, n)