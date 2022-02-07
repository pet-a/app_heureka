from fastapi import FastAPI


def get_app():

    app = FastAPI(
        title="Language detector model API",
        description="An API which uses NLP model to predict the language of the given text.",
        version="0.1",
    )
    return app
