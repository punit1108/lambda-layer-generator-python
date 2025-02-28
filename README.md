
# python-lambda-layer-generator

This project helps in generating an AWS Lambda layer with the required Python dependencies. The generated layer can be used to package and deploy Python dependencies for AWS Lambda functions.

## Prerequisites

- Docker: Ensure Docker is installed and running on your machine.
- AWS CLI: Ensure AWS CLI is installed and configured with appropriate permissions (optional for publishing the layer).

## Steps for Usage

### 1. Populate `requirements.txt` with the Required Python Dependencies

Add the required Python dependencies to the `requirements.txt` file. For example:

```plaintext
openai
pydantic-core
```

### 2. Run `generator.sh`

This step builds the Docker image, creates a virtual environment, installs the dependencies, and packages them into a zip file.

```bash
./generator.sh
```

### 3. Run `publish.sh` (Optional Step)

This step publishes a new version of an AWS Lambda layer using the AWS CLI. Ensure the `layer_content.zip` file is present in the same directory as the script.

```bash
./publish.sh <layer-name>
```

Replace `<layer-name>` with the name of the AWS Lambda layer you want to publish.

## File Descriptions

### `requirements.txt`

This file contains the list of Python dependencies required for the AWS Lambda layer.

### `generator.sh`

This script builds the Docker image and generates the `layer_content.zip` file containing the Python dependencies.

### `publish.sh`

This script publishes a new version of an AWS Lambda layer using the AWS CLI.

### `Dockerfile`

The Dockerfile used to build the Docker image, create the virtual environment, install the dependencies, and package them into a zip file.

## Example

1. Populate `requirements.txt`:

    ```plaintext
    openai
    pydantic-core
    ```

2. Run `generator.sh`:

    ```bash
    ./generator.sh
    ```

3. Run `publish.sh` (optional):

    ```bash
    ./publish.sh my-layer
    ```

This will create and publish an AWS Lambda layer named `my-layer` with the specified Python dependencies.

## Notes

- Ensure Docker is installed and running before executing `generator.sh`.
- Ensure AWS CLI is installed and configured with appropriate permissions before executing `publish.sh`.
