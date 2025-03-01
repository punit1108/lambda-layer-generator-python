import nltk
import os

# Set NLTK data path inside the layer directory structure
# During build: /shared_space/python/nltk_data
# When deployed to Lambda: /opt/python/nltk_data
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
    nltk.download(package, download_dir=nltk_data_dir)

print(f"NLTK data downloaded to {nltk_data_dir}")
print(f"NLTK data path: {nltk.data.path}")
print(f"In Lambda, this will be available at: /opt/python/nltk_data")

