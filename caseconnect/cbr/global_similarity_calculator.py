from .i_similarity_calculator import ISimilarityCalculator

import column_info

class GlobalSimilarityCalculator(ISimilarityCalculator):
    custom_weights = {
        "main_diagnosis": 10
    }

    def get_similarity(self, a, b):
        patient_a_dir = dir(a)
        print("== Patient {a} with Patient {b} ==".format(a= a.id,b=b.id))
        column_rankings = [
            {
            "col_id": col_id,
            "ranking": column_info.get_similarity_calculator_for_column(col_id).get_similarity(
                a.__dict__[col_id],
                b.__dict__[col_id]
            )} for col_id in patient_a_dir if not col_id.startswith('__') and column_info.get_similarity_calculator_for_column(col_id) is not None]
        return self._get_overall_score(column_rankings)
        
    def _get_overall_score(self, column_rankings):
        default_score_weighted_sum = 0
        for ranking in column_rankings:
            # Simple score * default_weighting
            addition = float(
                float(ranking["ranking"])
                * float(column_info.get_default_weight_for_column(ranking["col_id"])))
            # If we have a custom weighting than multiply with given weight again
            if ranking["col_id"] in self.custom_weights:
                addition *= self.custom_weights[ranking["col_id"]]
                print("[{c}]\nScore: {r}\nDef.Weight: {a}\nCust.Weight: {b}\n= {d}".format(c=ranking["col_id"], r=float(ranking["ranking"]), a=float(column_info.get_default_weight_for_column(ranking["col_id"])), b=self.custom_weights[ranking["col_id"]], d=addition))
            else:
                print("[{c}]\nScore: {r}\nDef.Weight: {a}\n= {d}".format(c=ranking["col_id"], r=float(ranking["ranking"]), a=float(column_info.get_default_weight_for_column(ranking["col_id"])), d=addition))
            default_score_weighted_sum += addition
        return default_score_weighted_sum
        