# This script publishes a new version of an AWS Lambda layer.
# Usage: ./publish.sh <layer-name>
# Parameters:
#   <layer-name> - The name of the AWS Lambda layer to publish.
# Requirements:
#   - AWS CLI must be installed and configured with appropriate permissions.
#   - The 'layer_content.zip' file must be present in the same directory as the script.

# Publish the Lambda layer version using the AWS CLI
aws lambda publish-layer-version --layer-name $1 --zip-file fileb://layer_content.zip --compatible-runtimes python3.12 --compatible-architectures "x86_64"