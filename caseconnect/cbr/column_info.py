from .i_similarity_calculator import ISimilarityCalculator
from .mock_similarity_calculator import MockSimilarityCalculator
column_info = {
        'id': {
            "weight": 0,
            "sim": None
        },
        'main_diagnosis': {
            "weight": 4,
            "sim": MockSimilarityCalculator()
        },
        'secondary_diagnosis': {
            "weight": 1,
            "sim": MockSimilarityCalculator()
        }
        # ...
    }

def get_similarity_calculator_for_column(column_id) -> ISimilarityCalculator:
    return column_info[column_id]["sim"]

def get_default_weight_for_column(column_id):
    return column_info[column_id]["weight"]