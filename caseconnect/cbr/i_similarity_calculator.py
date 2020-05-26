from .results.i_similarity_result import ISimilarityResult

class ISimilarityCalculator:
    """
    An interface for a similarity calculator.
    """
    
    def get_similarity(self, a, b) -> ISimilarityResult:
        """
        Will retrieve the similarity of two given objects which is logically the opposite of distance.
        
        Parameters
        ----------
        a : object
            This can be anything that should be compared to b
        b : object
        """

        pass