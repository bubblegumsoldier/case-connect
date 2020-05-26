from .model.patient import Patient
from .cbr.results.global_similarity_result import GlobalSimilarityResult
class PatientSimilarityWrapper:
    """
    A data wrapper containing a patient and its corresponding global similarity for some other patient
    (The other patient is not given)
    """
    patient :Patient
    global_similarity :GlobalSimilarityResult
    def __init__(self, patient :Patient, global_similarity :GlobalSimilarityResult):
        self.patient = patient
        self.global_similarity = global_similarity