
import openai
# update w. krishna's key 
openai.api_key = "put your api key here!"

#expand this dictionary
language_codes = {
    "es-es": "Spanish",
    "en": "English"
}

def translate_text_openai(text, source_language, target_language):
    prompt = f"Translate the following '{language_codes.get(source_language)}' text to '{language_codes.get(target_language)}': {text}"

    response = openai.ChatCompletion.create(

        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates math lectures"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translation = response.choices[0].message.content.strip()
    print(translation)
    return translation

def test(text):
  source_language = "English"
  target_language = "Spanish"
  translated_text = translate_text_openai(text, source_language, target_language)
  return translated_text

#print(test(text = "Your ideas are terrifying and your hearts are faint. 
# Your acts of pity and cruelty are absurd, committed with no calm, as if they were irresistible. 
# Finally, you fear blood more and more. Blood and time"))

