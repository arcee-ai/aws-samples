This repository contains developer resources to work with Arcee models on AWS. It includes sample notebooks demonstrating how to deploy and use various Arcee models on Amazon SageMaker.


## Models

The following Arcee models are featured in the sample notebooks:

1. [Llama-Spark](https://huggingface.co/arcee-ai/Llama-Spark): A powerful 8B parameter model built on the foundation of Llama-3.1-8B, excelling in reasoning, creative writing, and coding tasks.

2. [Arcee-Scribe](https://huggingface.co/arcee-ai/Arcee-Scribe): A versatile 7B parameter chat model with strong reasoning abilities, particularly adept at creative writing tasks.

3. [Arcee-Nova](https://huggingface.co/arcee-ai/Arcee-Nova): A large language model with performance approaching that of GPT-4 (as of May 2023), built on Qwen2-72B-Instruct.

4. [Arcee-Spark](https://huggingface.co/arcee-ai/Arcee-Spark): A powerful 7B parameter model that outperforms many larger models, offering a 32 KB context size.

5. [Arcee-Lite](https://huggingface.co/arcee-ai/arcee-lite): A compact yet powerful 1.5B parameter model, ideal for embedded systems and resource-constrained environments.

6. [Arcee-Agent](https://huggingface.co/arcee-ai/Arcee-Agent): A 7B parameter model specifically designed for function calling and tool use, excelling at interpreting and executing function calls.

## Deployment options

You can deploy these models on Amazon SageMaker in two ways:

1. Dowloading the model from Hugging Face and using the `model_notebooks` notebooks.
2. Subscribing to the model package in the [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-r7b33ivdczgs6) and using the `model_package_notebooks` notebooks.

## Contact

For more information or to discuss how Arcee can help your business, please contact julien@arcee.ai.

## License

[Apache License 2.0](LICENSE)
