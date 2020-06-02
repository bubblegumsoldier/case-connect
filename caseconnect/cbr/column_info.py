from .i_similarity_calculator import ISimilarityCalculator
# from .mock_similarity_calculator import MockSimilarityCalculator
# from .local_levensthein_similarity import LocalLevenstheinSimilarityCalculator
# column_info = {
#         'id': {
#             "weight": 0,
#             "sim": None
#         },
#         'main_diagnosis': {
#             "weight": 4,
#             "sim": MockSimilarityCalculator()
#         },
#         'secondary_diagnosis': {
#             "weight": 1,
#             "sim": MockSimilarityCalculator()
#         },
#         'text': {
#             "weight": 10,
#             "sim": LocalLevenstheinSimilarityCalculator(4)
#         }
#         # ...
#     }

from caseconnect.data_reader.csv_data_reader import CSVDataReader

column_info = CSVDataReader().retrieve_column_info("./example_data/AttributeGewichtung.csv")

def get_similarity_calculator_for_column(column_id) -> ISimilarityCalculator:
    return column_info[column_id]["sim"]

def get_default_weight_for_column(column_id) -> float:
    return column_info[column_id]["weight"]