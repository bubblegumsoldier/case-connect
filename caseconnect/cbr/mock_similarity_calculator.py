from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

class MockSimilarityCalculator(ISimilarityCalculator):
    """
    An example similarity calculator that can only compare two float values
    by dividing the smaller number through the larger number.

    There is no source for that approach and its suitability is questionable.
    """

    def get_similarity(self, a, b) -> ISimilarityResult:
        a = float(a)
        b = float(b)
        numerical_distance = float(min(a, b) / max(a, b))
        reason = "{}/{}".format(min(a, b), max(a, b))
        return LocalSimilarityResult(score=numerical_distance, description={"reason":reason})