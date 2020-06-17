from .data_reader.csv_data_reader import CSVDataReader
from .result_retriever import ResultRetriever
from typing import List
from .patient_similarity_wrapper import PatientSimilarityWrapper

class PatientRepository:
    data_source = "./example_data/PreprocessingTabelle.csv"
    data_reader = CSVDataReader()
    result_retriever = ResultRetriever()
    patients = []

    def __init__(self, initialize=True):
        if initialize:
            self.initialize_data()
    
    def initialize_data(self):
        """
        Initializes the patients using the CSVDataReader and the given data_source

        The data_source can be changed by using something like:
        repo = PatientRepository(initialize=False)
        repo.data_source = 'file.csv'
        repo.initialize_data()
        """
        
        self.patients = self.data_reader.retrieve_patients(self.data_source)

    def retrieve_similar_patients(self, query_patient_id :str, n :int=8) -> List[PatientSimilarityWrapper]:
        """
        Method to retrieve similar patients for a patient

        Parameters
        ----------
        query_patient_id : int
            The id of the patient from the dataset to use as the query patient
        n :int
            The number of patients to retrieve maximally
        """

        return self.result_retriever.retrieve_result_for_patient_id(self.patients, query_patient_id, n)

    def retrieve_single_patient(self, query_patient_id :str):
        """
        Returns the patient with the given id
        """
        return [p for p in self.patients if p.id == query_patient_id][0]