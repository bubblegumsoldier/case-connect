from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult
from .string_similarity_initializer import get_calculator
from typing import List

class ListMatchSumSimilarityCalculator(ISimilarityCalculator):
    """
    Compares each item of a given string list a
    with each item of a given string list b.
    The score of each match will be summed up.
    The min(1, sum) equals the score of the returned
    similarity.
    """
    child_calculator = None
    delimiter = ","
    
    def __init__(self, delimiter=",", calc_type :str = "simple_string", **kwargs):
        self.child_calculator = get_calculator(calc_type, **kwargs)
        self.delimiter = delimiter

    def get_similarity(self, a :str, b :str) -> ISimilarityResult:
        if a.strip() == "-" or b.strip() == '-' or len(a) <= 0 or len(b) <= 0:
            return LocalSimilarityResult(0, {'reason': 'Empty value a: {}, b: {}'.format(a, b)}, True)
        a_values = a.split(self.delimiter)
        b_values = b.split(self.delimiter)
        all_similarities = []
        for a_val in a_values:
            for b_val in b_values:
                all_similarities.append(self.child_calculator.get_similarity(a_val, b_val))
        return LocalSimilarityResult(
            score=self._sum_of_similarities(all_similarities),
            description=all_similarities)
    
    def _sum_of_similarities(self, similarities :List[ISimilarityResult]) -> float:
        overall = 0
        for s in similarities:
            overall += s.score
        return min(overall, 1)