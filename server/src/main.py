import translation

def main():
    translator = translation.SubtitleTranslator(
        from_lang='en', 
        to_lang='pt',
        input_path='../input/example.srt',
        output_path='../output/translated_example.srt'
    )
    translator.run()

if __name__ == "__main__":
    main()