import sys
import os
import importlib

def check_import(module_name):
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'unknown version')
        print(f"✓ Successfully imported {module_name} ({version})")
        return True
    except ImportError as e:
        print(f"✗ Failed to import {module_name}: {e}")
        return False

print(f"Python version: {sys.version}")
print("\nTesting LangChain imports:")

# Test core LangChain imports
check_import('langchain')
check_import('langchain.chains')
check_import('langchain.prompts')
check_import('langchain.schema')

# Test OpenAI integration
check_import('langchain_openai')
check_import('openai')

# Test community modules
check_import('langchain_community')
check_import('langchain_community.vectorstores')
check_import('langchain_community.document_loaders')

# Test dependencies
check_import('tiktoken')
check_import('numpy')
check_import('faiss')

print("\nCreating sample README for lambda users...")

readme_content = """# LangChain for AWS Lambda

This Lambda layer provides LangChain and its common dependencies for use in Lambda functions.

## Available Packages

- langchain: Core LangChain framework
- langchain-openai: OpenAI integration for LangChain
- langchain-community: Community integrations for LangChain
- pydantic: Data validation library
- openai: OpenAI API client
- tiktoken: OpenAI tokenizer
- numpy: Numerical computing library
- faiss-cpu: Vector similarity search library

## Usage in Lambda Functions

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

def lambda_handler(event, context):
    # Initialize an OpenAI model
    llm = OpenAI(temperature=0.7, openai_api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    
    # Create a chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run the chain
    product = event.get("product", "colorful socks")
    result = chain.run(product)
    
    return {
        "statusCode": 200,
        "body": result
    }
```

## Environment Variables

When using this layer with OpenAI integration, set up these environment variables:
- OPENAI_API_KEY: Your OpenAI API key

## Memory Management

Lambda functions have memory limits. If using embeddings or vector databases like FAISS,
monitor your memory usage and consider:
- Limiting the number of documents
- Using smaller embeddings
- Processing data in batches
"""

with open("/shared_space/python/langchain_lambda_readme.md", "w") as f:
    f.write(readme_content)

print("Setup complete! LangChain layer is ready for Lambda.")
