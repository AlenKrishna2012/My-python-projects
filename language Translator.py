from translate import Translator

def translate_text():
    lang = input('Enter language code (e.g., "fr" for French, "es" for Spanish): ')#enter laguage code
    translator = Translator(to_lang=lang)  
    text_to_translate = input("Enter text to translate: ")
    
    translated_text = translator.translate(text_to_translate)# Translate the text
    print(f"Translated Text: {translated_text}")

while True:
    translate_text()
    # Call the translation function in a loop