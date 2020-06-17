from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult
from .string_similarity_initializer import get_calculator
delimiter = ","

class HighestResultInListSimilarityCalculator(ISimilarityCalculator):
    """
    Uses a list cell and compares each item of one input
    value with each item of the other one. The highest 
    matching result will be used as the overall cell score.
    """
    child_calculator = None

    def __init__(self, calc_type :str = "simple_string", **kwargs):
        self.child_calculator = get_calculator(calc_type, **kwargs)

    def get_similarity(self, a :str, b :str) -> ISimilarityResult:
        if a.strip() == "-" or b.strip() == '-' or len(a) <= 0 or len(b) <= 0:
            return LocalSimilarityResult(0, {'reason': 'Empty value a: {}, b: {}'.format(a, b)}, True)
        a_values = a.split(delimiter)
        b_values = b.split(delimiter)
        highest_score = 0
        highest_score_reasoning = None
        for a_val in a_values:
            for b_val in b_values:
                sim = self.child_calculator.get_similarity(a_val, b_val)
                if sim.score > highest_score:
                    highest_score = sim.score
                    highest_score_reasoning = sim
        return LocalSimilarityResult(score=highest_score, description=highest_score_reasoning)