from django.shortcuts import render, HttpResponse
from django.contrib import messages  # Import the messages module
from translate import Translator  # Import the Translator class

def home(request):
    if request.method == 'POST':
        try:
            text = request.POST.get('translate', '').strip()
            language = request.POST.get('language', '')
            
            if not text or not language:
                raise ValueError("Invalid input. Please provide text and select a language.")
            
            translator = Translator(to_lang=language)
            translation = translator.translate(text)
            
            print(f"Input Text: {text}, Selected Language: {language}, Translation: {translation}")
            
            return render(request, 'main/index.html', {'translation': translation, 'input_text': text, 'selected_language': language})
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            print(f"Error: {e}")
    return render(request, 'main/index.html')
