from .results.i_similarity_result import ISimilarityResult

class ISimilarityCalculator:
    def get_similarity(self, a, b) -> ISimilarityResult:
        pass