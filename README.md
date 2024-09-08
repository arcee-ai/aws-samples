This repository contains developer resources demonstrating how to deploy and use various Arcee models on Amazon SageMaker.

You're welcome to use them in your projects. Of course, we will always appreciate proper credit and a friendly message :)

For information or to discuss how Arcee can help your business, please contact julien@arcee.ai.

## Models

The following Arcee models are featured in the sample notebooks:

1. [Llama-Spark](https://huggingface.co/arcee-ai/Llama-Spark): A powerful 8B parameter model built on the foundation of Llama-3.1-8B, excelling in reasoning, creative writing, and coding tasks.

2. [Arcee-Scribe](https://huggingface.co/arcee-ai/Arcee-Scribe): A versatile 7B parameter chat model with strong reasoning abilities, particularly adept at creative writing tasks.

3. [Arcee-Nova](https://huggingface.co/arcee-ai/Arcee-Nova): A large language model with performance approaching that of GPT-4 (as of May 2023), built on Qwen2-72B-Instruct.

4. [Arcee-Spark](https://huggingface.co/arcee-ai/Arcee-Spark): A powerful 7B parameter model that outperforms many larger models, offering a 32 KB context size.

5. [Arcee-Lite](https://huggingface.co/arcee-ai/arcee-lite): A compact yet powerful 1.5B parameter model, ideal for embedded systems and resource-constrained environments.

6. [Arcee-Agent](https://huggingface.co/arcee-ai/Arcee-Agent): A 7B parameter model specifically designed for function calling and tool use, excelling at interpreting and executing function calls.

## Deployment options

You can deploy these models on Amazon SageMaker in different ways:

1. Deploy from the Hugging Face hub
   * `model_notebooks`: sample notebooks
   * `cloudformation/create_endpoint_from_hf_model*.yaml`: sample AWS CloudFormation templates
2. Deploy from a model artifact you have stored in S3
   * `cloudformation/create_endpoint_from_s3_model*.yaml`: sample AWS CloudFormation templates
3. Deploy from a model package that you have built yourself (not an AWS Marketplace model package)
   * `cloudformation/create_endpoint_from_model_package*.yaml`: sample AWS CloudFormation templates
4. Deploy from our [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-r7b33ivdczgs6) listings
   * This is the recommended approach if you cannot access Hugging Face in your AWS account, or if you want to start from an official package built and tested by Arcee.
   * You first need to subscribe to the model
   * You can then deploy the model using the built-in option, or with the sample notebooks in `model_package_notebooks`
   * This is the recommended approach if you cannot access Hugging Face in your AWS account, of if you prefer to deploy an official model package built and tested by Arcee.
