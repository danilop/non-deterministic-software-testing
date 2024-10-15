# Testing Non-Deterministic Software

This repository showcases examples of how to test non-deterministic software, including applications using generative AI and Large Language Models (LLMs). It demonstrates various techniques and tools to ensure the reliability and robustness of systems with unpredictable outputs.

This code is used and explained in the [Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a) article.

## Features

- Property-based testing using Hypothesis
- Semantic similarity checks for LLM outputs
- Adversarial prompt generation
- Anomaly detection
- Test case generation from historical data
- Structured test data generation using LLMs
- LLM-assisted output validation

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/danilop/non-deterministic-software-testing.git
   cd non-deterministic-software-testing
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your AWS credentials for Bedrock access (required for some examples):
   ```
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-east-1
   ```

## Usage

```
python <file_name>.py
```

Each Python file in the repository demonstrates a different technique for testing non-deterministic software. Here's a brief description of each file:

1. `anomaly_detector.py`: Implements an anomaly detection system using statistical methods to identify outliers in a stream of data.

2. `check_output_with_llm.py`: Uses an LLM to validate the reasonableness of outputs from another system or model.

3. `generate_adversarial_prompt.py`: Creates adversarial prompts to test the robustness of LLM-based systems.

4. `generate_structured_test_data.py`: Utilizes an LLM to generate structured test data for various scenarios.

5. `generate_test_cases_from_historical_test_data.py`: Generates new test cases based on patterns in historical test data.

6. `non_deterministic_function.py`: Demonstrates a simple non-deterministic function for testing purposes.

7. `property_based_testing.py`: Shows how to use property-based testing with Hypothesis for non-deterministic functions.

8. `semantic_similarity.py`: Implements semantic similarity checks using embeddings to compare LLM outputs.

9. `test_recommendation_algorithm.py`: Provides an example of testing a recommendation algorithm using property-based testing.

Each file contains detailed comments and example usage to help you understand and apply these testing techniques to your own non-deterministic software projects.

## Using Hypothesis for Property-Based Testing

This project uses [Hypothesis](https://hypothesis.works/), a powerful library for property-based testing in Python. Here's why and how we use it:

### Why use Hypothesis?

1. **Comprehensive Testing**: Hypothesis generates a wide range of test cases, including edge cases that might be overlooked in manual testing.

2. **Reproducibility**: When a test fails, Hypothesis provides the exact input that caused the failure, making debugging easier.

3. **Flexibility**: It works well with existing unittest-style test cases and can be integrated into various testing frameworks.

4. **Shrinking**: When a failing input is found, Hypothesis automatically tries to find the simplest possible example that still causes the failure.

5. **Non-Deterministic Testing**: Hypothesis is particularly useful for testing non-deterministic functions, as it can run multiple iterations to catch intermittent failures.

### How we use Hypothesis

In this project, Hypothesis is primarily used in `property_based_testing.py` and `test_recommendation_algorithm.py`. Here's a brief overview:

1. We define properties that should always hold true for our functions, regardless of the input.

2. We use Hypothesis strategies to generate a wide range of inputs for our tests.

3. Hypothesis runs the tests multiple times with different inputs, trying to find cases where the properties don't hold.

For example, in `property_based_testing.py`, we test a non-deterministic sorting function:

```python
@given(st.lists(st.integers()))
def test_non_deterministic_sort(lst):
    result = non_deterministic_sort(lst)
    # ... assertions to check properties ...
```

Here, `@given(st.lists(st.integers()))` tells Hypothesis to generate lists of integers as inputs for our test.

By using Hypothesis, we can more thoroughly test our non-deterministic functions and increase confidence in their correctness across a wide range of inputs.
