This repository contains developer resources to work with Arcee models on AWS. It includes sample notebooks demonstrating how to deploy and use various Arcee models on Amazon SageMaker.

## Models

The following Arcee models are featured in the sample notebooks:

1. [Llama-Spark](https://huggingface.co/arcee-ai/Llama-Spark): A powerful 8B parameter model built on the foundation of Llama-3.1-8B, excelling in reasoning, creative writing, and coding tasks.

2. [Arcee-Scribe](https://huggingface.co/arcee-ai/Arcee-Scribe): A versatile 7B parameter chat model with strong reasoning abilities, particularly adept at creative writing tasks.

3. [Arcee-Nova](https://huggingface.co/arcee-ai/Arcee-Nova): A large language model with performance approaching that of GPT-4 (as of May 2023), built on Qwen2-72B-Instruct.

4. [Arcee-Spark](https://huggingface.co/arcee-ai/Arcee-Spark): A powerful 7B parameter model that outperforms many larger models, offering a 32 KB context size.

5. [Arcee-Lite](https://huggingface.co/arcee-ai/arcee-lite): A compact yet powerful 1.5B parameter model, ideal for embedded systems and resource-constrained environments.

6. [Arcee-Agent](https://huggingface.co/arcee-ai/Arcee-Agent): A 7B parameter model specifically designed for function calling and tool use, excelling at interpreting and executing function calls.

## Sample Notebooks

Each model has a corresponding sample notebook demonstrating how to deploy and use it on Amazon SageMaker:

These notebooks guide you through the process of:
- Importing necessary dependencies
- Creating a SageMaker endpoint
- Performing real-time inference
- Visualizing the model output
- Cleaning up resources

## Usage

To use these sample notebooks:

1. Ensure you have access to Amazon SageMaker.
2. Clone this repository in Amazon SageMaker Studio or a SageMaker Notebook Instance.
2. Open the desired notebook.
3. Follow the instructions within each notebook to deploy and interact with the chosen Arcee model.
4. Add your own prompts and keep testing :)

## Prerequisites

An AWS account with access to Amazon SageMaker

## Contact

For more information or to discuss how Arcee can help your business, please contact julien@arcee.ai.

## License

[Apache License 2.0](LICENSE)
