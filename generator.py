from transformers import pipeline


class Generator:
    def __init__(self):
        self.generator = pipeline("text-generation", "gpt2")

    def generate_text(self, text: str, text_len: int):
        """Text generation using user input
        - **text**: input user text
        - **text_len**: count of output symbols
        """
        generated_text = self.generator(text, max_length=text_len)
        return generated_text[0]['generated_text']
