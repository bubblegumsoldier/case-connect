from .i_data_reader import IDataReader
from caseconnect.model.patient import Patient
from typing import List

class CSVDataReader(IDataReader):
    def retrieve_patients(self, filepath) -> List[Patient]:
        import csv
        patient_list = []
        with open(filepath, 'r', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            i = 0
            for row in reader:
                if i == 0:
                    i += 1
                    continue #Skip header

                # Attention: This assumes that the attributes are in the same order as the CSV input.
                # In our case that is the case. If attributes will be added in the future take care
                # to add these at the correct index as a parameter or update this part to make it more specific,
                # e.g. Patient(pulmo=row[index], ...)
                patient_list.append(Patient(*row))
                i = i + 1
        return patient_list
    
    def retrieve_column_info(self, filepath):
        import csv
        d = {}
        with open(filepath, 'r', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            i = 0
            for row in reader:
                if i == 0:
                    i += 1
                    continue #Skip header
                d[row[0]] = {
                    "weight": float(row[1]),
                    "sim": self._calculator_instance_by_row(row)
                }
                i = i + 1
        return d
    
    def _calculator_instance_by_row(self, row):
        import importlib
        i = importlib.import_module(row[2])
        if(row[3] == "None"):
            return None
        calculator = eval("i.{}".format(row[3]))
        return calculator