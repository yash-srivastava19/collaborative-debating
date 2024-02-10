from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load models and tokenizers
models = [
    AutoModelForSeq2SeqLM.from_pretrained(model_name) for model_name in ["model1", "model2", ...]  # Replace with your models
]
tokenizers = [AutoTokenizer.from_pretrained(model_name) for model_name in models]

def debate_round(prompt, agents):
    responses = []
    for agent, model, tokenizer in zip(agents, models, tokenizers):
        response = agent.generate_response(prompt)
        responses.append(response)

    return responses

def vote_on_consensus(candidates):
    # Count occurrences of each unique candidate string
    counts = {}
    for candidate in candidates:
        counts[candidate] = counts.get(candidate, 0) + 1

    # Identify the majority vote (or threshold, e.g., 2/3 of agents)
    max_count = max(counts.values())
    if max_count >= len(agents) // 2 + 1:  # Check for majority or set your threshold
        consensus = [candidate for candidate, count in counts.items() if count == max_count]
        return consensus[0]  # Pick the first consensus candidate
    else:
        return None  # No consensus reached

def debate(initial_prompt, max_rounds=5):
    prompt = initial_prompt
    agents = models  # Use all models as agents

    for round_num in range(max_rounds):
        responses = debate_round(prompt, agents)
        prompt = f"{prompt} ".join(responses) + " Please debate further and try to reach a consensus:"

    # Extract the final consensus from the last round's prompt
    candidates = prompt.split(":")[-1].strip().split(" ")
    final_consensus = vote_on_consensus(candidates)
    return final_consensus

# Example usage
question = "What is the meaning of life?"
answer = debate(question)
print(answer)
