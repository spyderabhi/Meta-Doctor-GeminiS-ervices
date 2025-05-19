# 🥗 7-Day Indian Vegetarian Meal Plan Generator

A full-stack AI web application that generates a 7-day Indian vegetarian meal plan based on a food image URL you provide. Initially powered by **Google Gemini API**, it has now evolved through **OpenAI GPT models** and finally settled on **Hugging Face open-source AI** for cost-free testing and broad accessibility.

---

## 🚀 Features

- Paste a **food image URL** to generate a meal plan  
- Uses **AI to understand food content and context**  
- Returns a **7-day vegetarian Indian meal plan**  
- Supports **multiple AI providers** (Google, OpenAI, Hugging Face)  
- Runs locally using **Flask** and a clean **HTML+JS** frontend  

---

## 🧠 Tech Stack

| Layer     | Technology                                |
|-----------|--------------------------------------------|
| Frontend  | HTML + JavaScript (Vanilla)                |
| Backend   | Python + Flask                             |
| AI Models | Gemini, GPT-4 (OpenAI), Hugging Face (Mistral, GPT-J) |
| Hosting   | Localhost (easily deployable to Render, Railway, etc.) |

---

## 🔄 API/Model Timeline

This project went through several AI platforms due to access limits, billing errors, or quota restrictions. Here's the full journey:

### ✅ 1. Google Gemini API (Initial)
- **Model Used**: `gemini-pro`, `gemini-pro-vision`, `text-bison`  
- **Status**: Deprecated due to 404 errors and quota limits  
- **Notes**: Required Google Cloud setup and access configuration  

### ✅ 2. OpenAI GPT (Midway)
- **Model Used**: `gpt-4`, `gpt-3.5-turbo`  
- **Status**: Dropped due to quota exhaustion and paywall  
- **Notes**: Worked well with structured prompt-based completion  

### ✅ 3. Hugging Face Inference API (Current)
- **Model Used**: `mistralai/Mistral-7B-Instruct-v0.1`, `EleutherAI/gpt-j-6B`  
- **Status**: ✅ Active — No payment required (with API token)  
- **Notes**: Requires text prompts instead of images (e.g., descriptions or image-derived captions)  

---

## 📸 Example Image URLs for Testing

Try these image URLs to test the app:

- Veg Thali → `https://upload.wikimedia.org/wikipedia/commons/1/15/Veg_Thali.jpg`  
- Dosa Plate → `https://upload.wikimedia.org/wikipedia/commons/6/6e/Dosa_and_Sambar.jpg`  
- Shahi Paneer → `https://upload.wikimedia.org/wikipedia/commons/3/3d/Shahi_Paneer.jpg`  

---

## 🛠️ Installation & Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/veg-meal-planner.git
cd veg-meal-planner
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Token in `.env`

Create a file `.env` in your root project folder and add:

```
HF_TOKEN=your_huggingface_token_here
```

You can get a free token at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## ▶️ Run the Flask App

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 Sample Output (Text)

```
Day 1:
  - Breakfast: Poha with peanuts and lemon
  - Lunch: Rajma chawal and cucumber raita
  - Dinner: Aloo gobi with chapati

...

Day 7:
  - Breakfast: Masala dosa with coconut chutney
  - Lunch: Chole with jeera rice
  - Dinner: Vegetable khichdi with curd and salad
```

---

## 📂 Project Structure

```
veg-meal-planner/
│
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # Web form and frontend
├── .env                 # Your API token (keep private)
├── requirements.txt     # Dependencies
└── README.md            # You're reading it!
```

---

## 🌐 Deployment Tips

Want to take it live?

- [Render](https://render.com) — Free Flask app hosting  
- [Railway](https://railway.app)  
- [Fly.io](https://fly.io)  

Make sure to set your environment variable `HF_TOKEN` securely in your hosting platform.

---

## 🛣️ Roadmap / To-Do

- ✅ Support multiple APIs (Google, OpenAI, HF)  
- ✅ Fallback for unavailable/paid models  
- 🔄 Add real-time image captioning (e.g., BLIP, CLIP)  
- 📝 PDF export of the generated meal plan  
- 🎤 Text-to-speech output for accessibility  
- 👥 User login, saved plan history  

---

## 📜 License

MIT License — you’re free to use, modify, and share with attribution.

---

## 🙏 Credits & Acknowledgments

- 💡 [Google Gemini API](https://ai.google.dev/)  
- 🤖 [OpenAI API](https://platform.openai.com/)  
- 🧠 [Hugging Face Inference API](https://huggingface.co/inference-api)  
- 🌍 Wikimedia Commons for food images  
- 🧩 Flask, Requests, Dotenv Python libraries  
