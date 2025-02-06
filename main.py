from flask import Flask, request, jsonify
from flask_cors import CORS
from api_request import number_api


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    if num < 0:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num


def digitsum(num):
    return sum(int(digit) for digit in str(num))

def is_armstrong(num):
    str_digit = str(num)
    power = len(str_digit)
    
    if sum(int(digit) ** power for digit in str_digit) == num:
        return "armstrong"
    

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/classify_number")
    def get_num_details():
        number = request.args.get("number")
        if not number.isnumeric():
            return jsonify({
                "number": "alphabet",
                "error": True
            }), 400
        if number:
            number = int(number)
            number_details = {
                "number": number,
                "is_prime": is_prime(number),
                "is_perfect": is_perfect(number),
                "properties": [is_armstrong(number), even_or_odd(number)],
                "digit_sum": digitsum(number),
                "fun_fact": number_api(number)
                }
            return jsonify(number_details), 200
        
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()