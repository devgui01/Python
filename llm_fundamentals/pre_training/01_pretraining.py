from supplementary import (
    calc_loss_batch,
    evaluate_model,
    generate_and_print_sample,
    calc_loss_loader,
    create_dataloader_v1,
    generate_text_simple
)
import torch
from supplementary import GPTModel
import tiktoken
from supplementary import plot_losses

GPT_CONFIG_500M = {
    "vocab_size": 200256,    # Vocabulary size
    "context_length": 1024, # Context length
    "emb_dim": 768,         # Embedding dimension
    "n_heads": 12,          # Number of attention heads
    "n_layers": 12,         # Number of layers
    "drop_rate": 0.0,       # Dropout rate
    "qkv_bias": False       # Query-Key-Value bias
}


torch.manual_seed(123)
model = GPTModel(GPT_CONFIG_500M)
model.eval();  # Disable dropout during inference


def text_to_token_ids(text, tokenizer):
    encoded = tokenizer.encode(text, allowed_special={'
