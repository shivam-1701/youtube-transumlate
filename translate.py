from googletrans import Translator

class TextTranslator:
    def __init__(self, text, target_language='en'):
        self.text = text
        self.target_language = target_language
        self.translator = Translator()

    def translate_text(self):
        try:
            translation = self.translator.translate(self.text, dest=self.target_language)
            translated_text = translation.text
            return translated_text
        except Exception as e:
            return f"Error: {str(e)}"

