class LanguageModelAgent:
    def __init__(self, model_name):
        # Load the model.
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        # Load the tokenizer.
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def _generate_response(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def process_query(self, query):
        # This will be different for different agent class. Inherit and change this, in the end, call self._generate_response after handling the query.
        raise NotImplementedError()

class CohereModelAgent:
    def __init__(self, api_key):
        self.co = cohere.Client(api_key)  ## Enter your API Key here.
    
    def _generate_response(self, prompt):
        response = self.co.generate(prompt=prompt)
        return response.generations[0].text 

    def process_query(self, query):
        # TODO: Might change this to something else.
        return self._generate_response(query)

# Some agents which we'll use for our experiments.

class BartAgent(LanguageModelAgent):
    def __init__(self, model_name="facebook/bart-base"):
        super().__init__(model_name)

    def process_query(self, query):
        return self._generate_response(query)

class GPT3Agent(LanguageModelAgent):
    def __init__(self, model_name="gpt3"):
        super().__init__(model_name)

    def process_query(self, query):
        return self._generate_response(query)

class T5Agent(LanguageModelAgent):
    def __init__(self, model_name="t5-base"):
        super().__init__(model_name)

    def process_query(self, query):
        return self._generate_response(query)
