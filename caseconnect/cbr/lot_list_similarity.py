from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult
from .string_similarity_initializer import get_calculator
from typing import List

delimiter = ","

class LOTListSimilarity(ISimilarityCalculator):
    """
    A similarity calculator which uses a look-up-table to decide on the score.
    There are two constructor parameters:
    child_calculator : str
        An id of the comparing similarity calculator that should be used. See also string_similarity_initializer.py
    threshold : float
        If a given score is larger than the given threshold the number of matches will be increased by one
    look_up_table : List[float]
        A list of which the index denotes the score that will be used for that number of matches. If no. of 
        matches is >= len(look_up_table) the score will be rounded to one.
        Example: [0, 0.2, 0.6, 0.9] will result in the scores
        0 matches: 0
        1 match: 0.2
        2 matches: 0.6
        3 matches: 0.9
        4 matches: 1.0
    """
    _child_calculator :ISimilarityCalculator = None
    _threshold :float = 0.9
    _look_up_table :List[float] = [0.0, 1.0]

    def __init__(self, threshold, look_up_table, calc_type :str = "simple_string", **kwargs):
        self.child_calculator = get_calculator(calc_type, **kwargs)
        self._threshold = threshold
        self._look_up_table = look_up_table
    
    def get_similarity(self, a :str, b :str) -> ISimilarityResult:
        if a.strip() == "-" or b.strip() == '-' or len(a) <= 0 or len(b) <= 0:
            return LocalSimilarityResult(0, {'reason': 'Empty value a: {}, b: {}'.format(a, b)}, True)
        a_values = a.split(delimiter)
        b_values = b.split(delimiter)
        matches :List[LocalSimilarityResult] = []
        non_matches :List[LocalSimilarityResult] = []
        for a_val in a_values:
            for b_val in b_values:
                child_score :LocalSimilarityResult = self.child_calculator.get_similarity(a_val, b_val)
                if child_score.score >= self._threshold:
                    matches.append(child_score)
                else:
                    non_matches.append(child_score)
        return LocalSimilarityResult(
            score = self._get_score_by_no_of_matches(len(matches)),
            description = {"matches": matches, "non_matches": non_matches, "l_o_t": str(self._look_up_table)})
        
    def _get_score_by_no_of_matches(self, no_of_matches :int) -> float:
        if no_of_matches > len(self._look_up_table):
            return 1.0
        else:
            return self._look_up_table[no_of_matches]