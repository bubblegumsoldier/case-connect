from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

class SimpleStringSimilarityCalculator(ISimilarityCalculator):
    def get_similarity(self, a, b) -> ISimilarityResult:
        a = a.lower().strip().lstrip()
        b = b.lower().strip().lstrip()
        if a == "-" or b == '-':
            return LocalSimilarityResult(score=0, description="Empty value", empty=True)
        if a == b:
            return LocalSimilarityResult(score=1, description={"reason":"{} == {}".format(a, b)})
        else:
            return LocalSimilarityResult(score=0, description={"reason":"{} != {}".format(a, b)})