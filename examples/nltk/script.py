import sys
import os
import nltk

print(f"Python version: {sys.version}")
print("Attempting to import nltk...")

try:
    print(f"NLTK version: {nltk.__version__}")
    
    # Set NLTK data path inside the layer directory structure
    nltk_data_dir = os.path.join("/shared_space/python", "nltk_data")
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    # Add the current build path to NLTK's data path for immediate use
    nltk.data.path.append(nltk_data_dir)
    
    # Download popular NLTK packages
    nltk_packages = [
        'punkt',
        'stopwords',
        'wordnet',
        'averaged_perceptron_tagger',
        'vader_lexicon',
        'omw-1.4',
    ]
    
    # Download the NLTK packages to our custom directory
    for package in nltk_packages:
        print(f"Downloading NLTK package: {package}")
        nltk.download(package, download_dir=nltk_data_dir)
    
    print(f"NLTK data downloaded to {nltk_data_dir}")
    print(f"NLTK data path: {nltk.data.path}")
    print(f"In Lambda, this will be available at: /opt/python/nltk_data")
    nltk.data.path.append("/opt/python/nltk_data")
    
except Exception as e:
    print(f"Error importing or using NLTK: {e}")
    print("Detailed traceback:")
    import traceback
    traceback.print_exc()