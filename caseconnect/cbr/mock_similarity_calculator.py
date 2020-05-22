from .i_similarity_calculator import ISimilarityCalculator

class MockSimilarityCalculator(ISimilarityCalculator):
    def get_similarity(self, a, b):
        return 1