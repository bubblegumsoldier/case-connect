from .patient_repository import PatientRepository
from .data_writer.results_data_writer import ResultsDataWriter
import json
from yaml import dump
from yaml import load, dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

import json

def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""
    return obj.__dict__


class Program:
    def main(self):
        query_patient_id = 'A'
        patient_repository = PatientRepository(initialize=True)
        query_patient = patient_repository.retrieve_single_patient(query_patient_id)
        similar_patients = patient_repository.retrieve_similar_patients(query_patient_id)
        output_wrapper = {
            "query_patient": query_patient,
            "similar_patients": similar_patients
        }
        output = json.dumps(output_wrapper, default=serialize, ensure_ascii=False).encode('utf8')
        result_writer = ResultsDataWriter()
        result_writer.save_results(output, 'Patient' + query_patient_id)
        text_file = open("output.json", "wb")
        text_file.write(output)
        text_file.close()
        output = dump(output_wrapper, Dumper=Dumper, encoding='utf-8', allow_unicode=True)
        text_file = open("output.yml", "wb")
        text_file.write(output)
        text_file.close()
