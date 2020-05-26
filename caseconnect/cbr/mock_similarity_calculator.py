from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

import random

class MockSimilarityCalculator(ISimilarityCalculator):
    """
    An example similarity calculator that can only compare two float values
    by substracting the larger number from the smaller number and then dividing it by
    the larger number. This is the distance in percentage ([0.0-1.0]). 1 - that distance will then
    be the similarity.

    Example: 9, 3 will become 1-((9-3)/9) = 1-0.66 = 0.33 = 33% similarity

    There is no source for that approach and its suitability is questionable.
    """
    
    def get_similarity(self, a, b) -> ISimilarityResult:
        a = float(a)
        b = float(b)
        numerical_distance = 1 - float((max(a, b) - min(a, b))/max(a, b))
        reason = "({}-{})/{}".format(max(a, b), min(a, b), max(a, b))
        return LocalSimilarityResult(score=numerical_distance, description={"reason":reason})