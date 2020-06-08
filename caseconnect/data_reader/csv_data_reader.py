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
                print(row)
                patient_list.append(Patient(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    row[14],
                    row[15],
                    row[16],
                    row[17],
                    row[18],
                    row[19],
                    row[20],
                    row[21],
                    row[22],
                    row[23]))
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