from deep_translator import GoogleTranslator 
import pysrt

class SubtitleTranslator:
    def __init__(self, from_lang='en', to_lang='pt-BR', input_path=None, output_path=None):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.input_path = input_path
        self.output_path = output_path

        self.subs = None
        self.translator : GoogleTranslator = GoogleTranslator(source=self.from_lang if self.to_lang else "auto", target=self.to_lang)
        
    def load_file(self, file_path):
        self.subs = pysrt.open(file_path)
        
    def translate_subtitles(self):
        translated = self.translator.translate_batch([sub.text for sub in self.subs])
        
        print(translated)

        for translated_text, sub in zip(translated, self.subs):
            sub.text = translated_text

    def save_output(self):
        if self.subs is not None:
            self.subs.save(self.output_path, encoding='utf-8') 
            
    def run(self):
        self.subs = pysrt.open(self.input_path) if self.input_path else None        
        
        self.translate_subtitles()
            
        self.save_output()