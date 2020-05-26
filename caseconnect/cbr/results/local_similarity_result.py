from .i_similarity_result import ISimilarityResult

class LocalSimilarityResult(ISimilarityResult):
    score :float = 0.0
    description :dict = {}
    def __init__(self, score :float, description :dict):
        self.score = score
        self.description = description