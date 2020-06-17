from .local_similarity_result import LocalSimilarityResult
from .i_similarity_result import ISimilarityResult

class EmptySimilarityResultWrapper(ISimilarityResult):
    local_similarity :LocalSimilarityResult = None
    column_id :str = ""
    def __init__(self, local_similarity :LocalSimilarityResult, column_id :str):
        self.local_similarity = local_similarity
        self.column_id = column_id