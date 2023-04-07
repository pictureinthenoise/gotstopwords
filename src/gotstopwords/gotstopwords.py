import os
from typing import Any
from gotstopwords.iso6391codes import CODES

BANKS = ["nltk", "other"]
DATA_PATH = "./src/gotstopwords/data/"

def input_to_lower(string: str) -> str:
    '''
    The `input_to_lower` method transforms a string to lowercase.

    @param {str} `string`: The original string.
    @return {str} _: The lowercase string. 
    @raise none
    '''
    try:
        return string.lower()
    except:
        return ""

def get_iso_639_1_code(lang: str) -> str:
    '''
    The `get_iso_639_1_code` method retrieves the associated ISO 639-1 code based on a language string via the
    `LANGS` dictionary.

    @param {str} `lang`: User input string for language.
    @return {str} `_code`: The ISO 639-1 code for the specified language.
    @raise none
    '''
    try:
        _code = list(CODES.keys())[list(CODES.values()).index(lang)]
        return _code
    except:
        return ""

def get_lang_name_with_iso_639_1_code(code: str) -> str:
    '''
    The `get_lang_name_with_iso_639_1_code` method retrieves the associated language based on a ISO 639-1 code
    via the `LANGS` dictionary.

    @param {str} `code`: ISO 639-1 code.
    @return {str} `_name`: The name of the language.
    @raise none
    '''    
    try:
        _name = list(CODES.values())[list(CODES.keys()).index(code)]
        return _name
    except:
        return ""

def sanitize_inputs(inputs: dict) -> dict:
    '''
    The `sanitize_inputs` method accepts a dictionary of user inputs and sanitizes them before loading a
    stop words list.

    @param {dict} `inputs`: Dictionary of user inputs.
    @return {dict} _:Dictionary of sanitized user inputs.
    @raise none
    '''
    # If `list_num` value was specified, ensure it is a string.
    if None != inputs["list_num"]:
        inputs["list_num"] = str(inputs["list_num"])

    # Transform all input values to lowercase.
    inputs = {_key: input_to_lower(inputs[_key]) for _key in inputs}

    # If `lang` value is 2 characters, try to get the language name using `lang` value as the ISO 639-1 code.
    if 2 == len(inputs["lang"]):
        inputs["lang"] = get_lang_name_with_iso_639_1_code(inputs["lang"])

    return inputs

def sanitize_list(stop_words: list) -> list:
    '''
    The `sanitize_list` method removes any empty list or empty string values from a retrieved stop words list.

    @param {list} `stop_words`: A retrieved stop words list.
    @return {list} _: The sanitized list.
    @raise none
    '''
    return [_word for _word in stop_words if not _word == [] and not _word == ""]

def validate_inputs(inputs: dict) -> bool:
    '''
    The `validate_inputs` method checks a dictionary of user input values to ensure they are valid before
    loading a stop words list.

    @param {dict} `inputs`: Dictionary of user inputs.
    @return {bool} _: True if inputs are valid; False otherwise.
    @raise none
    '''
    if (inputs["bank"] in BANKS) and (inputs["lang"] in list(CODES.values())):
        return True
    else:
        return False

def load(bank: str, lang: str, list_num: Any = None) -> list:
    '''
    The `load` methods loads a stop words list using user-supplied inputs.

    @param {str} `bank`: The stop words list bank.
    @param {str} `lang`: The stop words list language.
    @param {Any} `list_num`: The list number for a language with more than 1 stop words list.
    @return {list} `_stop_words`: The specified stop words list.
    @raise {Exception}
    '''
    _stop_words = []
    
    # Set dictionary of user inputs.
    _inputs = {
        "bank": bank,
        "lang": lang,
        "list_num": list_num
    }
    
    # Sanitize the inputs
    _inputs = sanitize_inputs(_inputs)

    # Get the list if inputs are valid.
    if validate_inputs(_inputs):
        if None == _inputs["list_num"]:
            _file = _inputs["lang"]
        else:
            _file = _inputs["lang"] + _inputs["list_num"]
        
        _full_path = DATA_PATH + _inputs["bank"] + "/" + _file

        if os.path.isfile(_full_path):
            try:
                with open (_full_path, "r", encoding="utf-8") as f:
                    _data = f.read()
                _stop_words = _data.split("\n")
            
                _stop_words = sanitize_list(_stop_words)
            except Exception as e:
                print(e)

    return _stop_words