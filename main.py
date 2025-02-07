from flask import Flask, request, jsonify
from flask_cors import CORS
from api_request import number_api


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return False

def is_perfect(num):
    if num < 1:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num


def digitsum(num):
    return sum(int(digit) for digit in str(abs(int(num))))

def is_armstrong(num):
    str_digit = str(abs(int(num)))
    power = len(str_digit)
    
    if sum(int(digit) ** power for digit in str_digit) == abs(num):
        return "armstrong"
    return None

def even_or_odd(num):
    return "even" if num % 2 == 0 else "odd"


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/classify_number")
    def get_num_details():
        number = request.args.get("number")

        try:
            # Convert input to float first
            float_val = float(number)

            if float_val.is_integer():
                parsed_value = int(float_val)  # Convert float to int safely
            else:
                parsed_value = float_val
            
            # Determine if integer-based properties should be calculate
            is_integer = isinstance(parsed_value, int) or float_val.is_integer()

            number_details = {
                "number": parsed_value,
                "is_prime": is_prime(int(parsed_value)) if is_integer and parsed_value >= 0 else False,
                "is_perfect": is_perfect(int(parsed_value)) if is_integer and parsed_value >= 0 else False,
                "properties": list(filter(None, [is_armstrong(int(parsed_value)) if is_integer else False, even_or_odd(int(parsed_value))])),
                "digit_sum": digitsum(parsed_value) if is_integer else None,
                "fun_fact": number_api(parsed_value) if is_integer else "Fun facts are available for integers only."
            }
            return jsonify(number_details), 200
        except ValueError:
            return jsonify({
                "number": "alphabet",
                "error": True
            }), 400        
               
    return app