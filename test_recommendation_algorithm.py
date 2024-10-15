from hypothesis import given, strategies as st
import numpy as np

def recommendation_algorithm(user_preferences, item_features):
    # Simplified recommendation algorithm
    return np.dot(user_preferences, item_features)

@given(
    st.lists(st.floats(min_value=-1, max_value=1), min_size=5, max_size=5),
    st.lists(st.lists(st.floats(min_value=-1, max_value=1), min_size=5, max_size=5), min_size=1, max_size=10)
)
def test_recommendation_algorithm(user_preferences, item_features_list):
    recommendations = [recommendation_algorithm(user_preferences, item) for item in item_features_list]
    
    # Property 1: Recommendations should be in the range [-5, 5] given our input ranges
    assert all(-5 <= r <= 5 for r in recommendations), "Recommendations out of expected range"
    
    # Property 2: Higher dot products should result in higher recommendations
    sorted_recommendations = sorted(zip(recommendations, item_features_list), reverse=True)
    for i in range(len(sorted_recommendations) - 1):
        assert np.dot(user_preferences, sorted_recommendations[i][1]) >= np.dot(user_preferences, sorted_recommendations[i+1][1]), "Recommendations not properly ordered"

# Run the test
test_recommendation_algorithm()