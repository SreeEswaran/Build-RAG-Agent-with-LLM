from src.retrieval import retrieve
from src.generation import generate_response
from src.ranking import rank_responses
from src.training import fine_tune_model

def main():
    # Sample query for testing the pipeline
    query = "What is the capital of India?"

    # Step 1: Retrieve relevant documents
    retrieved_docs = retrieve(query)

    # Step 2: Generate a response based on the retrieved documents
    response =generate_response(retrieved_docs)

    # Step 3: Rank the response to find the best match
    ranked_response = rank_responses([response], query)

    # Output the top-ranked response
    print("Top response:", ranked_response[0])

if __name__ == "__main__":
    main()