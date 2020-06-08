from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

class NumericalSimilarityCalculator(ISimilarityCalculator):
    """
    An example similarity calculator that can only compare two float values
    by dividing the smaller number through the larger number.

    There is no source for that approach and its suitability is questionable.
    """

    _dampening = 0
    def __init__(self, dampening_factor :float = 0):
        self._dampening = dampening_factor

    def get_similarity(self, a, b) -> ISimilarityResult:
        try:
            a = float(a)
            b = float(b)
            a_dampened = a - self._dampening
            b_dampened = b - self._dampening
        except ValueError:
            return LocalSimilarityResult(score=0, description={"reason":"One value couldn't be converted to float ({}, {})".format(a, b)})
        a_dampened = max(0, a_dampened) # may not be below zero
        b_dampened = max(0, b_dampened) # may not be below zero
        numerical_distance = float(min(a_dampened, b_dampened) / max(a_dampened, b_dampened))
        reason = "({:.2f}-{:.2f})/({:.2f}-{:.2f})={:.2f}/{:.2f}={:.2f}".format(
            min(a, b),
            self._dampening,
            max(a, b),
            self._dampening,
            min(a_dampened, b_dampened),
            max(a_dampened, b_dampened),
            numerical_distance)
        return LocalSimilarityResult(score=numerical_distance, description={"reason":reason})