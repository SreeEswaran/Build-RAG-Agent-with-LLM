from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rank_responses(responses, query_embedding, model):
    response_embeddings = [model.encode(resp) for resp in responses]
    similarities = cosine_similarity([query_embedding], response_embeddings)
    ranked_indices = np.argsort(similarities[0])[::-1]
    return [responses[i] for i in ranked_indices]