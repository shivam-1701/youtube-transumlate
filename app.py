from flask import Flask, render_template, request
from transcribe import YouTubeTranscriber
from summarize import TextSummarizer
from translate import TextTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        youtube_link = request.form['youtube_link']

        # Transcribe
        transcriber = YouTubeTranscriber(youtube_link)
        transcription = transcriber.get_transcription()

        print("Transcription:")
        print(transcription)

        # Summarize
        summarizer = TextSummarizer(model_name='facebook/bart-large-cnn')
        summarized_text = summarizer.summarize_text(transcription)

        print("Summarized Text:")
        print(summarized_text)

        # Translate (if needed)
        target_language = request.form.get('target_language', 'es')  # Default to 'es' if not provided
        translator = TextTranslator(summarized_text, target_language=target_language)
        translated_text = translator.translate_text()

        print(f"Translated Text to {target_language}:")
        print(translated_text)

        return render_template('result.html', transcription=transcription, summarized_text=summarized_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
