from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult
from .string_similarity_initializer import get_calculator
from typing import List

class AvgListSimilarity(ISimilarityCalculator):
    """
    Compares each item of a given string list with the item
    with the same index in the other list.
    The score of each match will be summed up and
    will be divided by the number of matches.
    The min(1, sum) equals the score of the returned
    similarity.

    E.g. Blutdruck
    """
    child_calculator = None
    delimiter = ","
    
    def __init__(self, delimiter=",", calc_type :str = "simple_string", **kwargs):
        self.child_calculator = get_calculator(calc_type, **kwargs)
        self.delimiter = delimiter

    def get_similarity(self, a :str, b :str) -> ISimilarityResult:
        a_values = a.split(self.delimiter)
        b_values = b.split(self.delimiter)
        all_similarities = []
        for i, a_val in enumerate(a_values):
            all_similarities.append(self.child_calculator.get_similarity(a_val, b_values[i]))
        return LocalSimilarityResult(
            score=self._sum_of_similarities(all_similarities),
            description=all_similarities)
    
    def _sum_of_similarities(self, similarities :List[ISimilarityResult]) -> float:
        overall = 0
        for s in similarities:
            overall += s.score
        overall = overall/len(similarities)
        return min(overall, 1)