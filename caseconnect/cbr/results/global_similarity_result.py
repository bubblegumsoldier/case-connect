from .i_similarity_result import ISimilarityResult
from .local_similarity_result_wrapper import LocalSimilarityResultWrapper
from typing import List

class GlobalSimilarityResult(ISimilarityResult):
    """
    A data wrapper class that can be used for documenting the similarity of
    two objects but also storing the scores and local similarities of children.
    """

    overall_score :float = 0
    local_similarity_wrappers :List[LocalSimilarityResultWrapper] = []
    def __init__(self, overall_score :float, local_similarity_wrappers :List[LocalSimilarityResultWrapper]):
        self.overall_score = overall_score
        self.local_similarity_wrappers = local_similarity_wrappers