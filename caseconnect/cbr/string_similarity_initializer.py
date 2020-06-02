from .simple_string_similarity import SimpleStringSimilarityCalculator
from .local_levenshtein_similarity import LocalLevenshteinSimilarityCalculator

TYPES = {
    "simple_string": SimpleStringSimilarityCalculator,
    "levenshtein": LocalLevenshteinSimilarityCalculator
}

child_calculator = None

def get_calculator(calc_type :str = "simple_string", **kwargs):
    return TYPES[calc_type](**kwargs)