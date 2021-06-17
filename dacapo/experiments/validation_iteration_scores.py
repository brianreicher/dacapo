from .tasks.evaluators import EvaluationScores
from .tasks.post_processors import PostProcessorParameters
from typing import List, Tuple
import attr


@attr.s
class ValidationIterationScores:

    iteration: int = attr.ib()
    parameter_scores: List[
        Tuple[
            PostProcessorParameters,
            EvaluationScores]] = attr.ib()