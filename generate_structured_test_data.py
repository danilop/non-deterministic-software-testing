import json
import boto3

AWS_REGION = "us-east-1"

MODEL_ID = "us.anthropic.claude-3-5-sonnet-20240620-v1:0"	

bedrock_runtime = boto3.client('bedrock-runtime', region_name=AWS_REGION)

def generate_structured_test_data(prompt, num_samples=5):
    response = bedrock_runtime.converse(
        modelId=MODEL_ID,
        messages=[{
            'role': 'user',
            'content': [{ 'text': prompt }]
        }]
    )
    generated_data = response['output']['message']['content'][0]['text']
    try:
        json_data = json.loads(generated_data)
    except json.JSONDecodeError:
        print("Generated data is not valid JSON")
        return None  # or raise an exception
    
    return json_data

# Example usage
prompt = """Generate 5 JSON objects representing potential user inputs for a weather forecasting app.
Each object should have 'location' and 'query' fields.
Output the result as a valid JSON array.
Output JSON and nothing else.
Here's a sample to guide the format:
[
  {
    "location": "New York",
    "query": "What's the temperature tomorrow?"
  }
]"""

test_inputs = generate_structured_test_data(prompt)

print(json.dumps(test_inputs, indent=2))
