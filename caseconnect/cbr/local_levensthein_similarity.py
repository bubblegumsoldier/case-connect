from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

import Levenshtein

class LocalLevenstheinSimilarityCalculator(ISimilarityCalculator):
    """
    An example similarity calculator that compares two strings
    using the levensthein distance and a maximal number from which
    a percentage is used to determine not the distance but the similarity.
    The max-number can be defined by column.
    """
    max_number :int = 0

    def __init__(self, max_number=10):
        self.max_number = max_number

    def get_similarity(self, a, b) -> ISimilarityResult:
        # pylint: disable=no-member
        distance = Levenshtein.distance(a, b)
        similarity = 1 - float(float(distance) / float(self.max_number))
        similarity = max(0, similarity) #min = 0
        reason = "{a} -> {b} = {d} distance | 1 - ({d}/{m}) = {s}".format(a=a, b=b, d=distance, m=self.max_number, s=similarity)
        return LocalSimilarityResult(score=similarity, description={"reason":reason})