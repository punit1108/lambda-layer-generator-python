# LangChain Layer for AWS Lambda (Untested)

This example demonstrates how to create an AWS Lambda layer containing LangChain and its dependencies for building LLM applications.

## What This Example Does

This example:
1. Installs LangChain and common integrations
2. Tests that all packages import correctly
3. Creates a readme file with usage instructions
4. Packages everything into a Lambda layer

## Prerequisites

- Docker installed and running
- AWS CLI configured (if you plan to publish the layer)

## Step-by-Step Instructions

### 1. Copy Files to Root Directory

Copy these files to the root of the python-layer-generator project:

```bash
cp -r examples/langchain/* .
```

This includes:
- `requirements.txt`: Contains LangChain and its dependencies
- `script.py`: Tests LangChain imports and creates documentation

### 2. Generate the Layer

Run the generator script:

```bash
./generator.sh
```

This will:
- Build the Docker image
- Install LangChain and dependencies
- Test that packages are working correctly
- Package everything into `layer_content.zip`

### 3. Publish the Layer (Optional)

```bash
./publish.sh langchain-layer
```

This will publish your layer to AWS with the name "langchain-layer".

## Using the LangChain Layer in Lambda Functions

After attaching the layer to your Lambda function, you can use LangChain like this:

```python
import os
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

def lambda_handler(event, context):
    # Initialize an OpenAI model
    llm = OpenAI(temperature=0.7, openai_api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Answer the following question: {query}",
    )
    
    # Create a chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Get the query from the event
    query = event.get("query", "What are the main features of LangChain?")
    
    # Run the chain
    result = chain.run(query)
    
    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
```

## Example Use Cases

### 1. Simple Q&A System

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

def lambda_handler(event, context):
    llm = OpenAI(temperature=0.7)
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Question: {query}\nAnswer:",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(event.get("query", "What is AWS Lambda?"))
    return {"result": result}
```

### 2. Document Retrieval with Vector Search

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
import json

# This could be initialized outside the handler for better performance
# (but note Lambda cold start considerations)
def initialize_retrieval_qa():
    # Load vector store from a file (could be in S3)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("/tmp/faiss_index", embeddings)
    
    # Create a retrieval chain
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa

def lambda_handler(event, context):
    qa = initialize_retrieval_qa()
    query = event.get("query", "What information do you have about AWS services?")
    result = qa.run(query)
    return {
        "statusCode": 200,
        "body": json.dumps({"answer": result})
    }
```

### 3. Conversational Agent with Memory

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI
import json

def lambda_handler(event, context):
    # Get conversation history from the event or initialize empty
    conversation_history = event.get("conversation_history", [])
    user_input = event.get("input", "Hello!")
    
    # Create memory with previous history
    memory = ConversationBufferMemory()
    
    # Restore conversation history
    for exchange in conversation_history:
        memory.chat_memory.add_user_message(exchange["user"])
        memory.chat_memory.add_ai_message(exchange["ai"])
    
    # Create conversation chain
    conversation = ConversationChain(
        llm=OpenAI(temperature=0.7),
        memory=memory,
        verbose=False
    )
    
    # Get response
    response = conversation.predict(input=user_input)
    
    # Add current exchange to history
    conversation_history.append({"user": user_input, "ai": response})
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": response,
            "conversation_history": conversation_history
        })
    }
```

## Environment Variables

When using this layer, you may need to set these environment variables in your Lambda function:

- `OPENAI_API_KEY`: Your OpenAI API key (required for OpenAI models)
- `LANGCHAIN_TRACING`: Set to "true" to enable LangChain tracing
- `LANGCHAIN_ENDPOINT`: LangChain API endpoint (if using LangSmith)
- `LANGCHAIN_API_KEY`: LangChain API key (if using LangSmith)

## Size Considerations

The full LangChain ecosystem with all dependencies can be large. This example includes common packages, but you might want to customize the requirements.txt file to include only what you need.

## Troubleshooting

- **ImportError**: Ensure the layer is attached to your function and the required packages are in requirements.txt
- **Memory errors**: LangChain operations, especially with embeddings, can be memory-intensive. Consider increasing your Lambda function's memory allocation
- **Timeout issues**: Set an appropriate timeout for your Lambda function, as LLM calls can take several seconds
