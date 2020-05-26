from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

import random

class MockSimilarityCalculator(ISimilarityCalculator):
    def get_similarity(self, a, b) -> ISimilarityResult:
        a = float(a)
        b = float(b)
        numerical_distance = float((max(a, b) - min(a, b))/max(a, b))
        reason = "({}-{})/{}".format(max(a, b), min(a, b), max(a, b))
        return LocalSimilarityResult(score=numerical_distance, description={"reason":reason})