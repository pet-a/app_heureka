import requests

# add review
input_text = """As Western governments threaten Russia with a package of unprecedented sanctions
aimed at deterring President Vladimir Putin from ordering an invasion of Ukraine, there's one
measure in particular that appears to strike fear at the heart of the Kremlin: cutting the country
off from the global banking system."""

keys = {"input_text": input_text}

prediction = requests.get("http://127.0.0.1:8000/predict-language/", params=keys)

results = prediction.json()
print(results["prediction"])
