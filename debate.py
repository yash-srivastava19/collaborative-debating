from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load models and tokenizers
model_1 = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")
tokenizer_1 = AutoTokenizer.from_pretrained("facebook/bart-base")
model_2 = AutoModelForSeq2SeqLM.from_pretrained("gpt2")
tokenizer_2 = AutoTokenizer.from_pretrained("gpt2")

def debate_round(prompt, agent_1, agent_2):
    # Generate responses from both agents
    response_1 = agent_1.generate_response(prompt)
    response_2 = agent_2.generate_response(response_1)

    # Combine responses into a new prompt for the next round
    combined_prompt = f"{prompt} {response_1} {response_2} Please debate further and try to reach a consensus:"
    return combined_prompt

def debate(initial_prompt, max_rounds=5):
    prompt = initial_prompt
    for round_num in range(max_rounds):
        prompt = debate_round(prompt, model_1, model_2)

    # Extract the final consensus from the last round's prompt
    final_response = extract_consensus(prompt)  # Implement this function based on your criteria
    return final_response

# Example usage
question = "What is the meaning of life?"
answer = debate(question)
print(answer)
