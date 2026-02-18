# 🤖 LLM Fundamentals

Learn to build Large Language Models from scratch.

## Prerequisites

- Python basics
- PyTorch fundamentals
- Linear algebra basics

## What's Inside

| Folder | Description |
|--------|-------------|
| `architecture/` | Build GPT from scratch |
| `pre_training/` | Train transformer models |
| `fine_tuning/` | Fine-tune LLMs |
| `weight_loading/` | Load pre-trained weights |

## Learning Path

### 1. Architecture
Build a complete GPT-style transformer model from scratch.

```bash
cd architecture
python 01_transformer_architecture.py
```

### 2. Pre-training
Learn to pre-train transformer models.

```bash
cd pre_training
python 01_pretraining.py
```

### 3. Weight Loading
Load pre-trained GPT-2 weights.

```bash
cd weight_loading
python 01_weight_loading.py
```

### 4. Fine-tuning
Fine-tune models for specific tasks.

```bash
cd fine_tuning
python 01_fine_tuning.py
```

## Requirements

```bash
pip install torch transformers tiktoken
```

## Note

⚠️ **GPU Recommended:** Training and inference run faster with CUDA.
⚠️ **Large Downloads:** Some models require downloading GBs of weights.

## Next Steps

Start with `architecture/` to understand the model structure!
