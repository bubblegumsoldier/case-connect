from .local_similarity_result import LocalSimilarityResult
from .i_similarity_result import ISimilarityResult

class LocalSimilarityResultWrapper(ISimilarityResult):
    """
    A wrapper object that contains the local similarity but also the weighted
    scores and the weights that were used. This class is important for backtrace
    decisions and scores. The LocalSimilarity class does not contain information
    about the weights as its not the concern of the local similarity. LocalSimilarity 
    contains information about the similarity of two objects, no about its context
    within the parent object. That's what this class is for.
    """

    default_weight :float = 1.0
    custom_weight :float = 1.0
    default_weighted_score :float = 0
    custom_weighted_score :float = 0
    local_similarity :LocalSimilarityResult = None
    column_id :str = ""
    def __init__(self,
        default_weighted_score :float,
        custom_weighted_score :float,
        local_similarity :LocalSimilarityResult,
        default_weight :float,
        custom_weight :float,
        column_id :str):
        self.default_weighted_score = default_weighted_score
        self.custom_weighted_score = custom_weighted_score
        self.local_similarity = local_similarity
        self.default_weight = default_weight
        self.custom_weight = custom_weight
        self.column_id = column_id