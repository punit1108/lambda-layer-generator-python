# NLTK Layer for AWS Lambda

This example demonstrates how to create an AWS Lambda layer containing NLTK and its corpora data.

## Steps to Create the NLTK Layer

1. Copy the files in this directory to the root of the python-layer-generator project:
   - `requirements.txt`: Contains NLTK as a requirement
   - `main.py`: Downloads NLTK data and configures paths

2. Run the generator script:
   ```bash
   ./generator.sh
   ```

3. Publish the layer (optional):
   ```bash
   ./publish.sh nltk-layer
   ```

## Using the NLTK Layer in Lambda Functions

After attaching the layer to your Lambda function, use the following code to initialize NLTK:

```python
import nltk
import os

# Add the layer's NLTK data directory to the NLTK data path
nltk.data.path.append("/opt/python/nltk_data")

# Now you can use NLTK features
def lambda_handler(event, context):
    # Example: Tokenize text
    tokens = nltk.word_tokenize("Hello, this is a test of NLTK in AWS Lambda!")
    
    # Example: Get stopwords
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    
    # Example: POS tagging
    pos_tags = nltk.pos_tag(tokens)
    
    return {
        "statusCode": 200,
        "body": {
            "tokens": tokens,
            "pos_tags": str(pos_tags)
        }
    }
```

## Included NLTK Packages

The following NLTK packages are included in this layer:
- punkt (tokenization)
- stopwords
- wordnet
- averaged_perceptron_tagger (for POS tagging)
- vader_lexicon (for sentiment analysis)
- omw-1.4 (Open Multilingual WordNet)

## Customizing

To add more NLTK packages, modify the `nltk_packages` list in `main.py`:

```python
nltk_packages = [
    'punkt',
    'stopwords',
    'wordnet',
    'averaged_perceptron_tagger',
    'vader_lexicon',
    'omw-1.4',
    # Add more packages here
]
```
