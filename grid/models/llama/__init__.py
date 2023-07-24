from grid.models.llama.block import WrappedLlamaBlock
from grid.models.llama.config import DistributedLlamaConfig
from grid.models.llama.model import (
    DistributedLlamaForCausalLM,
    DistributedLlamaForSequenceClassification,
    DistributedLlamaModel,
)
from grid.utils.auto_config import register_model_classes

register_model_classes(
    config=DistributedLlamaConfig,
    model=DistributedLlamaModel,
    model_for_causal_lm=DistributedLlamaForCausalLM,
    model_for_sequence_classification=DistributedLlamaForSequenceClassification,
)
