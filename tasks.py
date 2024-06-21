#Tasks that need to be run on backend to power the routes
from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

#switch to t5-large later
tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=512) #from_pretrained means dont have to create tokenizer, #t5-small is google dl model that can translate between some langs, max_length is how many characters 
translator = T5ForConditionalGeneration.from_pretrained("t5-base")


# store translation: take in translation request and save it todatabase
def store_translation(t):
    model = TranslationModel(text=t.text, base_lang=t.base_lang, final_lang=t.final_lang)
    model.save()
    return model.id

# run translation: runs pre-trained deep learning model
def run_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id) #query db for translation id

    prefix = f"translate {model.base_lang} to {model.final_lang}: {model.text}"
    input_ids = tokenizer(prefix, return_tensors="pt").input_ids #converts text to numbers

    outputs = translator.generate(input_ids, max_new_tokens=512)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True) #turns output from numbers into text, skip_special tokens skips internal model tokens that dont make sense to us
    model.translation = translation
    model.save()

# find translation: retrieve a translation from the database

def find_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id)

    translation = model.translation
    if translation is None:
        translation = "Processing, check back later."
    return translation