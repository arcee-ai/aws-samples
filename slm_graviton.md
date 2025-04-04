# Running Virtuoso-Lite with llama.cpp

This guide demonstrates how to run the [Virtuoso-Lite model](https://huggingface.co/arcee-ai/Virtuoso-Lite) using llama.cpp.

## System Requirements
- Amazon Linux 2
- r8g instance (xlarge or larger)
- At least 128GB of storage

## Installation Steps

1. Install required dependencies:
```bash
sudo yum install cmake gcc g++ git git-lfs python3 python3-pip python3-virtualenv -y
```

2. Install large file support for got
```bash
git lfs install
```

3. Clone the model repository:
```bash
git clone https://huggingface.co/arcee-ai/Virtuoso-Lite
```

4. Clone and build llama.cpp:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B Build
cmake --build build --config Release -j16
```

5. Install python dependencies for llama.cpp
```bash
virtualenv env-llama-cpp
source env-llama-cpp/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

6. Convert and quantize the model:
```bash
pip3 install -r requirements.txt
python3 convert_hf_to_gguf.py ../Virtuoso-Lite
bin/llama-quantize ../Virtuoso-Lite/Virtuoso-Lite-10B-F16.gguf Q4_0
bin/llama-quantize ../Virtuoso-Lite/Virtuoso-Lite-10B-F16.gguf Q8_0
```

## Performance Comparison

### 16-bit Model
```bash
bin/llama-cli -m ../Virtuoso-Lite/Virtuoso-Lite-10B-F16.gguf -n 512 -p "<|im_start|>system \
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|> \
<|im_start|>user \
Explain step by step how the attention mechanism works in transformer models. \
<|im_end|> \
<|im_start|>assistant" --chat-template chatml -no-cnv
```

**Performance metrics:**
- Prompt eval: 21.65 ms per token, 46.18 tokens per second
- Eval time: 58.06 ms per token, 17.22 tokens per second

### 8-bit Model (Q8_0)
```bash
bin/llama-cli -m ../Virtuoso-Lite/ggml-model-Q8_0.gguf -n 512 -p "<|im_start|>system \
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|> \
<|im_start|>user \
Explain step by step how the attention mechanism works in transformer models. \
<|im_end|> \
<|im_start|>assistant" --chat-template chatml -no-cnv
```

**Performance metrics:**
- Prompt eval: 12.03 ms per token, 83.16 tokens per second
- Eval time: 35.10 ms per token, 28.49 tokens per second

### 4-bit Model (Q4_0)
```bash
bin/llama-cli -m ../Virtuoso-Lite/ggml-model-Q4_0.gguf -n 512 -p "<|im_start|>system \
You are a friendly and helpful AI assistant. Keep your answers precise and factual.<|im_end|> \
<|im_start|>user \
Explain step by step how the attention mechanism works in transformer models. \
<|im_end|> \
<|im_start|>assistant" --chat-template chatml -no-cnv
```

**Performance metrics:**
- Prompt eval: 6.64 ms per token, 150.50 tokens per second
- Eval time: 22.43 ms per token, 44.58 tokens per second

## Evaluating Model Quality

To evaluate the model's perplexity on WikiText-2:
```bash
# Download the test dataset
sh scripts/get-wikitext-2.sh

# Run perplexity evaluation
bin/llama-perplexity -m ../virtuoso-lite/Virtuoso-Lite-10B-F16.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m ../virtuoso-lite/ggml-model-Q8_0.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m ../virtuoso-lite/ggml-model-Q4_0.gguf -f wikitext-2-raw/wiki.test.raw
```

**Perplexity Results:**
- 16-bit (F16): 6.6953 +/- 0.04633
- 8-bit (Q8_0): 6.7001 +/- 0.04640 (0.06% worse than F16)
- 4-bit (Q4_0): 6.7627 +/- 0.04632 (1% worse than F16)


Choose the quantization level based on your specific needs:
- F16: Highest quality, largest size, slowest inference
- Q8_0: Balanced performance and quality
- Q4_0: Fastest inference, smallest size
