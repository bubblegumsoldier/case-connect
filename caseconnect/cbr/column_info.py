from .i_similarity_calculator import ISimilarityCalculator

from caseconnect.data_reader.csv_data_reader import CSVDataReader

column_info = CSVDataReader().retrieve_column_info("./example_data/AttributeGewichtung.csv")

def get_similarity_calculator_for_column(column_id) -> ISimilarityCalculator:
    return column_info[column_id]["sim"]

def get_default_weight_for_column(column_id) -> float:
    return column_info[column_id]["weight"]