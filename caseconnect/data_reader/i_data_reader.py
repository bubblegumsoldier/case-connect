from caseconnect.model.patient import Patient
from typing import List

class IDataReader:
    def retrieve_patients(self, filepath) -> List[Patient]:
        pass