from .simple_string_similarity import SimpleStringSimilarityCalculator
#from .local_levenshtein_similarity import LocalLevenshteinSimilarityCalculator
from .i_similarity_calculator import ISimilarityCalculator
from .numerical_similarity_calculator import NumericalSimilarityCalculator

TYPES = {
    "simple_string": SimpleStringSimilarityCalculator,
    #"levenshtein": LocalLevenshteinSimilarityCalculator,
    "numerical": NumericalSimilarityCalculator
}

child_calculator = None

def get_calculator(calc_type :str = "simple_string", **kwargs) -> ISimilarityCalculator:
    return TYPES[calc_type](**kwargs)