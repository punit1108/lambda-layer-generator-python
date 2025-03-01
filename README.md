# Python Lambda Layer Generator

A tool to create AWS Lambda layers with Python dependencies using Docker. This project simplifies the process of packaging Python dependencies for AWS Lambda, ensuring compatibility with the Lambda runtime environment.

## Overview

AWS Lambda layers allow you to include additional code and content in your Lambda functions. This project automates the creation of Lambda layers for Python dependencies, ensuring they are compiled for the correct architecture and Python version.

## Prerequisites

- **Docker**: Required to build the Lambda layer in an environment similar to AWS Lambda
- **AWS CLI** (optional): Required only if you want to publish the layer directly to AWS

## Quick Start

### 1. Define Your Dependencies

Edit `requirements.txt` to include the Python packages you want in your layer:

```plaintext
# Example requirements.txt
openai
pydantic-core
importlib-metadata
```

### 2. Generate the Layer

Run the generator script:

```bash
./generator.sh
```

This will:
- Build a Docker image with a Lambda-like environment
- Install your Python dependencies
- Package them into a ZIP file (`layer_content.zip`)

### 3. Publish Your Layer (Optional)

If you have AWS CLI configured, you can publish the layer directly:

```bash
./publish.sh my-lambda-layer
```

Replace `my-lambda-layer` with your preferred layer name.

## Project Structure

- **Dockerfile**: Configures the Docker environment for building the layer
- **requirements.txt**: Lists the Python dependencies to include in the layer
- **script.py**: Optional script to run before packaging (useful for post-install tasks)
- **generator.sh**: Script to build the Docker image and generate the layer
- **publish.sh**: Script to publish the layer to AWS

## Advanced Usage

### Custom Scripts

You can modify `script.py` to perform custom tasks before the layer is packaged. This is useful for:
- Downloading additional resources
- Configuring packages that require post-install setup
- Testing the installed packages

### Examples

Check the `examples/` directory for specific use cases:
- `examples/nltk/`: How to create a layer with NLTK and download language data

## Troubleshooting

### Common Issues

1. **Binary Compatibility**:
   - If you see errors related to binary compatibility, ensure you're using the `--platform manylinux2014_x86_64` flag in the Dockerfile

2. **Missing Dependencies**:
   - Some packages require system libraries. You may need to modify the Dockerfile to install them

3. **Layer Size Limits**:
   - AWS Lambda layers have a size limit of 250 MB (unzipped). Monitor your layer size

## Architecture

This project uses a multi-stage Docker build process:
1. **Builder Stage**: Installs dependencies and packages them
2. **Export Stage**: Copies the generated ZIP file to your local system

The Docker image uses the `amazon/aws-lambda-python` base image to ensure compatibility with the actual Lambda runtime environment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
