from .patient_repository import PatientRepository

class Program:
    def main(self):
        patient_repository = PatientRepository(initialize=True)
        similar_patients = patient_repository.retrieve_similar_patients(0)
        print(similar_patients)