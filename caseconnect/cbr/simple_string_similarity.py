from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

class SimpleStringSimilarityCalculator(ISimilarityCalculator):
    _punish_empty_values = False

    def __init__(self, punish_empty_values=False):
        self._punish_empty_values = punish_empty_values

    def get_similarity(self, a, b) -> ISimilarityResult:
        a = a.lower().strip().lstrip()
        b = b.lower().strip().lstrip()
        if not self._punish_empty_values:
            if a == "-" or b == '-':
                return LocalSimilarityResult(score=0, description="Empty value", empty=True)
        if a == b:
            return LocalSimilarityResult(score=1, description={"reason":"{} == {}".format(a, b)})
        else:
            return LocalSimilarityResult(score=0, description={"reason":"{} != {}".format(a, b)})