# Running Virtuoso-Small with llama.cpp

This guide demonstrates how to run the [Virtuoso-Small model](https://huggingface.co/arcee-ai/Virtuoso-Small) using llama.cpp.

## System Requirements
- Amazon Linux 2
- r8g.8xlarge instance
- At least 128GB of storage

## Installation Steps

1. Install required dependencies:
```bash
sudo yum install cmake gcc g++ git python3 python3-pip -y
```

2. Install Huggingface CLI and login:
```bash
pip3 install huggingface_hub
```

3. Login to Huggingface Hub:
```bash
huggingface-cli login
```

4. Download the model:
```bash
huggingface-cli download arcee-ai/Virtuoso-Small --local-dir virtuoso-small
```

5. Build llama.cpp:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake .
make -j16
```

6. Convert and quantize the model:
```bash
pip3 install -r requirements.txt
python3 convert_hf_to_gguf.py ../virtuoso-small
bin/llama-quantize ../virtuoso-small/Virtuoso-Small-F16.gguf Q4_0
bin/llama-quantize ../virtuoso-small/Virtuoso-Small-F16.gguf Q8_0
```

## Performance Comparison

### 16-bit Model
```bash
bin/llama-cli -m ../virtuoso-small/Virtuoso-Small-F16.gguf -n 512 -p "<|im_start|>system
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|>
<|im_start|>user
Explain step by step how the attention mechanism works in transformer models.
<|im_end|>
<|im_start|>assistant" --chat-template chatml -fa
```

**Performance metrics:**
- Prompt eval: 28.03 ms per token (35.67 tokens/sec)
- Eval time: 123.01 ms per token (8.13 tokens/sec)

### 8-bit Model (Q8_0)
```bash
bin/llama-cli -m ../virtuoso-small/ggml-model-Q8_0.gguf -n 512 -p "<|im_start|>system
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|>
<|im_start|>user
Explain step by step how the attention mechanism works in transformer models.
<|im_end|>
<|im_start|>assistant" --chat-template chatml -fa
```

**Performance metrics:**
- Prompt eval: 15.04 ms per token (66.51 tokens/sec)
- Eval time: 56.30 ms per token (17.76 tokens/sec)

### 4-bit Model (Q4_0)
```bash
bin/llama-cli -m ../virtuoso-small/ggml-model-Q4_0.gguf -n 512 -p "<|im_start|>system
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|>
<|im_start|>user
Explain step by step how the attention mechanism works in transformer models.
<|im_end|>
<|im_start|>assistant" --chat-template chatml -fa
```

**Performance metrics:**
- Prompt eval: 5.53 ms per token (180.92 tokens/sec)
- Eval time: 31.40 ms per token (31.85 tokens/sec)

## Evaluating Model Quality

To evaluate the model's perplexity on WikiText-2:
```bash
# Download the test dataset
sh scripts/get-wikitext-2.sh

# Run perplexity evaluation
bin/llama-perplexity -m ../virtuoso-small/Virtuoso-Small-F16.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m ../virtuoso-small/ggml-model-Q8_0.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m ../virtuoso-small/ggml-model-Q4_0.gguf -f wikitext-2-raw/wiki.test.raw
```

**Perplexity Results:**
- 16-bit (F16): 5.8443 +/- 0.03782
- 8-bit (Q8_0): 5.8518 +/- 0.03788
- 4-bit (Q4_0): 6.2136 +/- 0.04043

Choose the quantization level based on your specific needs:
- F16: Highest quality, largest size, slowest inference
- Q8_0: Balanced performance and quality
- Q4_0: Fastest inference, smallest size, potentially a bit lower quality
