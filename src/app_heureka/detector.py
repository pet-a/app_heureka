from .main import get_app
import gcld3
import uvicorn

app = get_app()


def decode_language(utf_text: str):
    """
    A simple function that receive a text and decode it.
    :param utf_text:
    :return: result_text
    """
    # decoding from utf-8 format
    result_text = utf_text.encode()
    result_text = result_text.decode()
    return result_text


def count_words(input_text: str, limit_of_words=5):
    """
    A simple function that receive a text and counts the words.
    :param input_text:
    :return: none
    """
    number_of_words = 0
    # Splitting the data into separate lines
    lines = input_text.split()

    # Iterating over every word and adding it to the counter
    for word in lines:
        number_of_words += 1

    if number_of_words <= limit_of_words:
        raise Exception("Words in text should be more than", limit_of_words)
    else:
        return input_text


@app.get("/predict-language")
def predict_language(input_text: str):
    """
    A simple function that receive a paragraph of text and predict the language
    :param input_text:
    :return: prediction
    """
    # checks the number of words in a text
    input_text = count_words(input_text)

    # prediction
    lang_identifier = gcld3.NNetLanguageIdentifier(10, 1000)
    a_identifier = lang_identifier.FindLanguage(input_text)

    # outputs
    a_prediction = a_identifier.language
    a_decoded_text = decode_language(input_text)

    # show results
    result = {"prediction": a_prediction, "input_text": a_decoded_text}
    return result


def start():
    """
    Launched with `poetry run start` at root level
    """
    uvicorn.run("src.app_heureka.detector:app", host="0.0.0.0", port=8000, reload=True)
