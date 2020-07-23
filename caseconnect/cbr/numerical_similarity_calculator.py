from .i_similarity_calculator import ISimilarityCalculator
from .results.i_similarity_result import ISimilarityResult
from .results.local_similarity_result import LocalSimilarityResult

class NumericalSimilarityCalculator(ISimilarityCalculator):
    """
    An example similarity calculator that can only compare two float values
    by dividing the smaller number through the larger number. Prior to that from
    both numbers the ignore factor will be substracted. That can be used to compensate
    for very large numbers naturally lying quite close to each other
    (e.g. BMI, Temperature and Blood pressure). For temperature e.g. we will always be between
    36 and 40. So we can deduct 35 from each value to make the increase the impact
    of these minor differences. For BMI for example we can use the ignore factor 14.

    There is no source for that approach and its suitability is questionable.
    """

    _ignore = 0
    _punish_empty_values = False

    def __init__(self, ignore_factor :float = 0, punish_empty_values=False):
        self._ignore = ignore_factor
        self._punish_empty_values = punish_empty_values

    def get_similarity(self, a, b) -> ISimilarityResult:
        if not self._punish_empty_values:
            if a.strip() == "-" or b.strip() == '-':
                return LocalSimilarityResult(score=0, description="Empty value", empty=True)
        try:
            a = float(a)
            b = float(b)
            a_dampened = a - self._ignore
            b_dampened = b - self._ignore
        except ValueError:
            return LocalSimilarityResult(score=0, description={"reason":"One value couldn't be converted to float ({}, {})".format(a, b)})
        a_dampened = max(0, a_dampened) # may not be below zero
        b_dampened = max(0, b_dampened) # may not be below zero
        numerical_distance = float(min(a_dampened, b_dampened) / max(a_dampened, b_dampened))
        reason = "({:.2f}-{:.2f})/({:.2f}-{:.2f})={:.2f}/{:.2f}={:.2f}".format(
            min(a, b),
            self._ignore,
            max(a, b),
            self._ignore,
            min(a_dampened, b_dampened),
            max(a_dampened, b_dampened),
            numerical_distance)
        return LocalSimilarityResult(score=numerical_distance, description={"reason":reason})