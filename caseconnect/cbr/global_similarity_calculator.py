from .i_similarity_calculator import ISimilarityCalculator
from .results.local_similarity_result import LocalSimilarityResult
from .results.global_similarity_result import GlobalSimilarityResult
from .results.local_similarity_result_wrapper import LocalSimilarityResultWrapper
from .column_info import get_similarity_calculator_for_column
from .results.empty_similarity_result_wrapper import EmptySimilarityResultWrapper
from .column_info import get_default_weight_for_column
from typing import List

class GlobalSimilarityCalculator(ISimilarityCalculator):
    """
    A class that should be used for comparing to patients with each other.

    It will use default weights for each parameter of a Patient (defined in .column_info)
    and furthermore will use the attribute custom_weights for weighting the already weighted
    scores again.

    For each column the SimilarityCalculator that is defined in column_info will be used. Of None is
    present that column will be skipped.
    """

    custom_weights = {
        "main_diagnosis": 10
    }

    def get_similarity(self, a, b):
        patient_a_dir = dir(a)
        local_similarity_results = [
            {
                "col_id": col_id,
                "local_similarity": get_similarity_calculator_for_column(col_id).get_similarity(
                    a = a.__dict__[col_id],
                    b = b.__dict__[col_id],
                )
            } for col_id in patient_a_dir if not col_id.startswith('__') and get_similarity_calculator_for_column(col_id) is not None]
        return self._get_overall_score(self._get_local_result_wrappers(local_similarity_results))
        
    def _get_local_result_wrappers(self, column_rankings) -> List[LocalSimilarityResultWrapper]:
        local_result_wrappers = []
        for ranking in column_rankings:
            # Simple score * default_weighting
            if ranking["local_similarity"].empty:
                local_result_wrappers.append(EmptySimilarityResultWrapper(ranking["local_similarity"], ranking["col_id"]))
                continue
            default_weight = get_default_weight_for_column(ranking["col_id"])
            custom_weight = 1
            default_weighted_score = ranking["local_similarity"].score * default_weight
            custom_weighted_score = default_weighted_score
            if ranking["col_id"] in self.custom_weights:
                custom_weight = self.custom_weights[ranking["col_id"]]
                custom_weighted_score = default_weighted_score * custom_weight
            local_similarity_result_wrapper = LocalSimilarityResultWrapper(
                default_weighted_score,
                custom_weighted_score,
                ranking["local_similarity"],
                default_weight,
                custom_weight,
                ranking["col_id"])
            local_result_wrappers.append(local_similarity_result_wrapper)
        return local_result_wrappers
    
    def _get_overall_score(self, local_result_wrappers) -> GlobalSimilarityResult:
        sum_of_weights = 0
        sum_of_custom_weighted_scores = 0
        for local_result_wrapper in local_result_wrappers:
            if type(local_result_wrapper) is EmptySimilarityResultWrapper:
                continue
            sum_of_custom_weighted_scores += local_result_wrapper.custom_weighted_score
            sum_of_weights += local_result_wrapper.default_weight + local_result_wrapper.custom_weight
        overall_score = sum_of_custom_weighted_scores / sum_of_weights
        return GlobalSimilarityResult(overall_score, local_result_wrappers, sum_of_weights, sum_of_custom_weighted_scores)