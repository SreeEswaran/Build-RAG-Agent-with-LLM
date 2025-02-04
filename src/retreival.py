from datasets import load_dataset

def retrieve(query, top_k=5):
    dataset = load_dataset('wikipedia', '20220301.en')['train']
    return dataset.select(range(top_k))
