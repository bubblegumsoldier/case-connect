from .cbr.global_similarity_calculator import GlobalSimilarityCalculator

class ResultRetriever:
    global_similarity_calculator = GlobalSimilarityCalculator()

    def split_patients(self, patients, patient_id):
        return ([p for p in patients if p.id == str(patient_id)][0], [p for p in patients if p.id != str(patient_id)])

    def retrieve_result_for_patient_id(self, patients, patient_id, n=8):
        query_patient, case_base = self.split_patients(patients, patient_id)
        return self.retrieve_result_for_patient(case_base, query_patient, n)
    
    def retrieve_result_for_patient(self, case_base, patient, n=8):
        rankings = [{"patient": p, "ranking": self.get_similarity(patient, p)} for p in case_base]
        sorted_patients = sorted(rankings, key=lambda x: x["ranking"], reverse=True)
        return sorted_patients
    
    def get_similarity(self, query_patient, case_base_patient):
        return self.global_similarity_calculator.get_similarity(query_patient, case_base_patient)