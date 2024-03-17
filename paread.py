import json
from googletrans import Translator
import os
translator = Translator(timeout=10) 
# Loop through file names from Map001.json to Map999.json
for i in range(90, 1000):
    file_number = str(i).zfill(3)  # Convert the file number to a 3-digit string with leading zeros
    file_path = f'E:\\[Kimochi] FUZ_V.1.17\\data\\Map{file_number}.json'
    print("trying map", file_number)
    try:
        # Load JSON data from file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Initialize translator
        translator = Translator()

        # Replace original parameters with translated ones and print the translated data
        for event in data.get("events", []):
            if event:
                for page in event.get("pages", []):
                    if page and page.get("list"):
                        for item in page["list"]:
                            original_parameters = item.get("parameters", [])
                            if isinstance(original_parameters, list) and all(isinstance(i, str) for i in original_parameters) and original_parameters:
                                translated_parameters = []
                                for text in original_parameters:
                                    try:
                                        translated_text = translator.translate(text, src='en', dest='ar').text if text.strip() else ''
                                    except Exception as e:
                                        print(f"An error occurred during translation: {e}")
                                        translated_text = ''
                                    translated_parameters.append(translated_text)
                                print("Translated text:", translated_parameters)  # Print translated text
                                item["parameters"] = translated_parameters

        # Write the updated JSON data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("endded map", file_number)
        os.system('cls')
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please provide the correct path to the JSON file.")
