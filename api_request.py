import requests

def number_api(num):
    type = "math"
    response = requests.get(f"http://numbersapi.com/{num}/{type}")
    if response.status_code == 200:
        trivia = response.text
    return trivia




