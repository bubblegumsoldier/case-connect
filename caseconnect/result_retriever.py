from .cbr.global_similarity_calculator import GlobalSimilarityCalculator
from typing import List, Tuple
from .patient_similarity_wrapper import PatientSimilarityWrapper
from .cbr.results.global_similarity_result import GlobalSimilarityResult
from .model.patient import Patient

class ResultRetriever:
    global_similarity_calculator = GlobalSimilarityCalculator()

    def retrieve_result_for_patient_id(self, all_patients :List[Patient], patient_id :int, n=8) -> List[PatientSimilarityWrapper]:
        """
        Retrieves similar patients for a patient with a given ID. The id has to be within the parameter all_patients

        Parameters
        ----------
        all_patients : List[Patient]
            A list of the whole case base

        patient_id : int
            The id of the patient that should be used as the query patient (The patient for which to find similar other patients)
        """

        query_patient, case_base = self._split_patients(all_patients, patient_id)
        return self._retrieve_result_for_patient(case_base, query_patient, n)

    def _split_patients(self, patients, patient_id :str) -> Tuple[Patient, List[Patient]]:
        """
        Will split a given list of patients into the patient with the given ID and all other patients
        """

        return ([p for p in patients if p.id == str(patient_id)][0], [p for p in patients if p.id != str(patient_id)])
    
    def _retrieve_result_for_patient(self, case_base :List[Patient], patient :Patient, n=8) -> List[PatientSimilarityWrapper]:
        """
        Will retrieve similar patients from a given case base and a query patient.

        Paarameters
        ----------
        case_base : List[Patient]
            The case base to search through
        patient : Patient
            The query patient
        """

        rankings = [PatientSimilarityWrapper(p, self._get_global_similarity(patient, p)) for p in case_base]
        sorted_patients = sorted(rankings, key=lambda x: x.global_similarity.overall_score, reverse=True)
        return sorted_patients
    
    def _get_global_similarity(self, query_patient :Patient, case_base_patient :Patient) -> GlobalSimilarityResult:
        """
        Will return the global similarity for a query patient and another patient

        Parameters
        ----------
        query_patient : Patient
            The query patient
        case_base_patient : Patient
            The patient to which to compare the given query_patient to
        """
        
        return self.global_similarity_calculator.get_similarity(query_patient, case_base_patient)