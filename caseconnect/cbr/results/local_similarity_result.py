from .i_similarity_result import ISimilarityResult

class LocalSimilarityResult(ISimilarityResult):
    """
    A data wrapper class that can be used for scoring the similarity
    of two objects. It is important for backtracing the score-creation
    later on. Therefore the description object should be filled by the
    corresponding SimilarityCalculator.
    """

    score :float = 0.0
    description :dict = {}
    def __init__(self, score :float, description :dict):
        self.score = score
        self.description = description