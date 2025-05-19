from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

HF_API_TOKEN = "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"
MODEL_ID = "tiiuae/falcon-7b-instruct"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-meal-plan', methods=['POST'])
def generate_meal_plan():
    data = request.json
    image_url = data.get('image_url')

    if not image_url:
        return jsonify({'error': 'Image URL is required'}), 400

    prompt = (
        f"Analyze this Indian food image and suggest a 7-day Indian vegetarian meal plan inspired by it:\n{image_url}\n\nMeal plan:"
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL_ID}",
            headers=HEADERS,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            meal_plan = result[0]['generated_text']
        else:
            meal_plan = "Model returned an unexpected format."

        return jsonify({'meal_plan': meal_plan})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f"HTTP error occurred: {str(e)}"}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
