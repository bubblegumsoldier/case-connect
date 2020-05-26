from .i_data_reader import IDataReader
from caseconnect.model.patient import Patient
from typing import List

class CSVDataReader(IDataReader):
    def retrieve_patients(self, filepath) -> List[Patient]:
        import csv
        patient_list = []
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i == 0:
                    i += 1
                    continue #Skip header
                patient_list.append(Patient(row[0], row[1], row[2], row[3]))
                i = i + 1
        return patient_list