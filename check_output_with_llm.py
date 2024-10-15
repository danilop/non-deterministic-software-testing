import boto3

AWS_REGION = "us-east-1"

MODEL_ID = "us.anthropic.claude-3-5-sonnet-20240620-v1:0"	

bedrock_runtime = boto3.client('bedrock-runtime', region_name=AWS_REGION)

def check_output_with_llm(input_text, test_output, prompt_template):
    prompt = prompt_template.format(input=input_text, output=test_output)

    response = bedrock_runtime.converse(
        modelId=MODEL_ID,
        messages=[{
            'role': 'user',
            'content': [{ 'text': prompt }]
        }]
    )

    response_content = response['output']['message']['content'][0]['text'].strip().lower()
    if response_content not in ["yes", "no"]:
        raise ValueError(f"Unexpected response from LLM: {response_content}")
    return response_content == "yes"

# Example usage
input_text = "What's the weather like today?"
test_output = "It's sunny with a high of 75°F (24°C) and a low of 60°F (16°C)."
prompt_template = "Given the input question '{input}', is this a reasonable response: '{output}'? Answer yes or no and nothing else."

is_valid = check_output_with_llm(input_text, test_output, prompt_template)

print('input_text:', input_text)
print('test_output:', test_output)
print(f"Is the test output a reasonable response? {is_valid}")
