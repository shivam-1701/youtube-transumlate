from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration


class TextSummarizer:
    def __init__(self, model_name=None):
        self.model_name = model_name

        if self.model_name:
            self.summarizer = pipeline("summarization", model=self.model_name)
        else:
            raise ValueError("Invalid model name. Please provide a valid model name.")

    def preprocess_text(self, text):
        # Add any necessary text preprocessing steps here

        # Limit the input length to the tokenizer's maximum sequence length
        max_length = self.summarizer.tokenizer.model_max_length
        if len(text) > max_length:
            text = text[:max_length]

        return text

    def summarize_text(self, text):
        preprocessed_text = self.preprocess_text(text)

        # Limit the input length to the model's maximum sequence length
        max_length = self.summarizer.model.config.max_position_embeddings
        if len(preprocessed_text) > max_length:
            preprocessed_text = preprocessed_text[:max_length]

        summary = self.summarizer(preprocessed_text, max_length=200, min_length=150, length_penalty=1.0, num_beams=4, early_stopping=True)
        return summary[0]['summary_text']
