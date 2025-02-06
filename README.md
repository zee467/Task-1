# Task-1


## **Overview**  

This project is a **DevOps Stage 1** task for the **HNG Internship** that involves creating a RESTful API to classify numbers based on their mathematical properties. It determines whether a number is prime, perfect, Armstrong, or odd/even. Additionally, it provides the sum of its digits and an interesting fun fact.

The API is built using **Flask**, supports **CORS**, and returns responses in **JSON format**.

## **Features**
- Accepts **GET** requests with a number as a query parameter.
- Returns:
  - Prime number check
  - Perfect number check
  - Armstrong number check
  - Odd/Even classification
  - Sum of digits
  - Fun fact (retrieved from an external API)
- Returns structured JSON responses.
- Provides appropriate HTTP status codes.
- Deployed on a publicly accessible endpoint.

---

## **API Specification**  

### **Endpoint**
```plaintext
GET <your-api-url>/api/classify-number?number=<integer>
```

### **Example Requests and Responses**

#### ✅ **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### ❌ **Error Response (400 Bad Request)**
```json
{
    "number": "alphabet",
    "error": true
}
```

---

## **Setup and Installation**  

### **1. Clone the Repository**
```bash
git clone https://github.com/zee467/Task-1.git
cd Task-1
```

### **2. Create and Activate a Virtual Environment**  
```bash
python -m venv venv
# Windows
source venv/Scripts/activate  
# macOS/Linux
source venv/bin/activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Run the Flask Server**  
```bash
python main.py
```
The API will be available at `http://127.0.0.1:5000/`.

---

## **How It Works**
### **1. Check if a Number is Prime**
- A prime number is only divisible by 1 and itself.
- Example: `is_prime(7) → True`, `is_prime(10) → False`

### **2. Check if a Number is Perfect**
- A perfect number equals the sum of its proper divisors.
- Example: `is_perfect(6) → True`, since `1 + 2 + 3 = 6`

### **3. Check if a Number is an Armstrong Number**
- Armstrong numbers satisfy `sum(digits^len(digits)) == number`
- Example: `371 → 3³ + 7³ + 1³ = 371` (Armstrong)

### **4. Identify Odd/Even**
- Even if `number % 2 == 0`, otherwise Odd.

### **5. Calculate Sum of Digits**
- Example: `sum_digits(371) → 3 + 7 + 1 = 11`

### **6. Fetch a Fun Fact**
- Uses `numbersapi` to retrieve fun mathematical trivia.
