# NLTK Layer for AWS Lambda

This example demonstrates how to create an AWS Lambda layer containing NLTK and its language data, properly configured for use in AWS Lambda functions.

## What This Example Does

This example:
1. Installs NLTK and its dependencies
2. Downloads specific NLTK data packages
3. Configures the data paths to work in AWS Lambda
4. Packages everything into a Lambda layer

## Prerequisites

- Docker installed and running
- AWS CLI configured (if you plan to publish the layer)

## Step-by-Step Instructions

### 1. Copy Files to Root Directory

Copy these files to the root of the python-layer-generator project:

```bash
cp -r examples/nltk/* .
```

This includes:
- `requirements.txt`: Contains NLTK and regex dependencies
- `script.py`: Downloads NLTK data and configures paths

### 2. Generate the Layer

Run the generator script:

```bash
./generator.sh
```

This will:
- Build the Docker image
- Install NLTK and dependencies
- Download the specified NLTK data packages
- Package everything into `layer_content.zip`

### 3. Publish the Layer (Optional)

```bash
./publish.sh nltk-layer
```

This will publish your layer to AWS with the name "nltk-layer".

## Using the NLTK Layer in Lambda Functions

After attaching the layer to your Lambda function, use this code to initialize NLTK:

```python
import nltk
import os

# Add the layer's NLTK data directory to the NLTK data path
nltk.data.path.append("/opt/python/nltk_data")

def lambda_handler(event, context):
    # Example: Tokenize text
    text = event.get('text', "Hello, this is a test of NLTK in AWS Lambda!")
    tokens = nltk.word_tokenize(text)
    
    # Example: Remove stopwords
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
    
    # Example: POS tagging
    pos_tags = nltk.pos_tag(tokens)
    
    # Example: Named Entity Recognition
    from nltk import ne_chunk
    named_entities = ne_chunk(pos_tags)
    
    return {
        "statusCode": 200,
        "body": {
            "original_text": text,
            "tokens": tokens,
            "filtered_tokens": filtered_tokens,
            "pos_tags": str(pos_tags),
            "named_entities": str(named_entities)
        }
    }
```

## Included NLTK Packages

This layer includes these NLTK data packages:

| Package | Description | Use Case |
|---------|-------------|----------|
| punkt | Tokenization models | Sentence and word tokenization |
| stopwords | Common stopwords | Removing common words like "the", "a", etc. |
| wordnet | WordNet lexical database | Word meanings, synonyms, lemmatization |
| averaged_perceptron_tagger | POS tagger | Part-of-speech tagging |
| vader_lexicon | VADER sentiment model | Sentiment analysis |
| omw-1.4 | Open Multilingual WordNet | Multi-language support |

## Customizing NLTK Data

To add more NLTK packages, modify the `nltk_packages` list in `script.py`:

```python
nltk_packages = [
    'punkt',
    'stopwords',
    'wordnet',
    'averaged_perceptron_tagger',
    'vader_lexicon',
    'omw-1.4',
    # Add more packages here, for example:
    'conll2000',        # For chunking
    'maxent_ne_chunker', # For named entity recognition
    'words',            # Words corpus
    'treebank',         # Treebank corpus
]
```

## Size Considerations

The NLTK data packages can be quite large. Consider including only the packages you need to keep your layer size under AWS Lambda's limits (250 MB unzipped).

## Troubleshooting

- **ImportError: No module named 'nltk'**: Ensure the layer is properly attached to your function
- **LookupError: Resource not found**: Ensure the path to NLTK data is correct and the package is included in `nltk_packages`
- **Layer size too large**: Reduce the number of NLTK packages in the `nltk_packages` list
