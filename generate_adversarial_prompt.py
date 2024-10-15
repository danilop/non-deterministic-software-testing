import json
import random
import string
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

# This is a mock LLM function for demonstration purposes
def mock_llm(input_text):
    return "The capital of France is Paris, a city known for its iconic Eiffel Tower."


def generate_adversarial_prompt(base_prompt, num_perturbations=3):
    perturbations = [
        lambda s: s.upper(),
        lambda s: s.lower(),
        lambda s: ''.join(random.choice([c.upper(), c.lower()]) for c in s),
        lambda s: s.replace(' ', '_'),
        lambda s: s + ' ' + ''.join(random.choices(string.ascii_letters, k=5)),
    ]
    
    adversarial_prompt = base_prompt
    for _ in range(num_perturbations):
        perturbation = random.choice(perturbations)
        adversarial_prompt = perturbation(adversarial_prompt)
    
    return adversarial_prompt

def test_llm_robustness(llm_function, base_prompt, expected_topic, num_tests=10):
    for _ in range(num_tests):
        adversarial_prompt = generate_adversarial_prompt(base_prompt)
        response = llm_function(adversarial_prompt)
        
        # Here I use my semantic similarity function to check if the response
        # is still on topic despite the adversarial prompt
        is_on_topic = semantic_similarity(response, expected_topic) > 0.7
        
        print(f"Prompt: {adversarial_prompt}")
        print(f"Response on topic: {is_on_topic}")
        print("---")

# Example usage (assuming I have my LLM function and semantic_similarity function from before)
base_prompt = "What is the capital of France?"
expected_topic = "Paris is the capital of France"

test_llm_robustness(mock_llm, base_prompt, expected_topic)
