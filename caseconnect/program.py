from .patient_repository import PatientRepository
from yaml import dump
from yaml import load, dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

class Program:
    def main(self):
        patient_repository = PatientRepository(initialize=True)
        similar_patients = patient_repository.retrieve_similar_patients(0)
        output = dump(similar_patients, Dumper=Dumper)
        text_file = open("output.yml", "w")
        text_file.write(output)
        text_file.close()
