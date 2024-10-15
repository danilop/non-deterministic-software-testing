import json
import boto3

from scipy.spatial.distance import cosine

AWS_REGION = "us-east-1"
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

bedrock_runtime = boto3.client('bedrock-runtime', region_name=AWS_REGION)

def get_embedding(text):
    body = json.dumps({"inputText": text})
    response = bedrock_runtime.invoke_model(
        modelId=EMBEDDING_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=body
    )
    response_body = json.loads(response['body'].read())
    return response_body['embedding']

def semantic_similarity(text1, text2):
    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)
    return 1 - cosine(embedding1, embedding2)

def test_llm_response(llm_function, input_text, acceptable_responses, similarity_threshold=0.8):
    llm_response = llm_function(input_text)
    print("llm_response:", llm_response)
    
    for acceptable_response in acceptable_responses:
        similarity = semantic_similarity(llm_response, acceptable_response)
        print("acceptable_response:", acceptable_response)
        if similarity >= similarity_threshold:
            print("similarity:", similarity)
            return True
    
    return False

# Example usage
def mock_llm(input_text):
    # This is a mock LLM function for demonstration purposes
    return "The capital of France is Paris, a city known for its iconic Eiffel Tower."

input_text = "What is the capital of France?"
acceptable_responses = [
    "The capital of France is Paris.",
    "Paris is the capital city of France.",
    "France's capital is Paris, known for its rich history and culture."
]

result = test_llm_response(mock_llm, input_text, acceptable_responses)
print(f"LLM response test passed: {result}")
