# ✨ Social Media Caption Generator

This is a **Streamlit-based web app** that generates engaging captions for your social media posts using powerful **AI models from Hugging Face Transformers** like `T5` or `BART`.

---

## 🚀 Features

- 📱 Generate catchy social media captions from a short text or topic
- 🎯 Suitable for Instagram, LinkedIn, Twitter, and more
- 🧠 Built using state-of-the-art NLP models (`transformers`)
- ⚡ Fast, simple, and interactive UI with Streamlit

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend/Model**: Hugging Face Transformers (`T5-base`, `BART`, etc.)
- **Language**: Python 3
- **Deployment**: Streamlit CLI (local or Streamlit Cloud)

---

## 🧩 Dependencies

Install via:

```bash
pip install -r requirements.txt
```

### `requirements.txt` content:

```
streamlit
transformers
torch
sentencepiece
```

---

## ▶️ How to Run the App

1. **Clone the repository**

```bash
git clone https://github.com/your-username/social-caption-generator.git
cd social-caption-generator
```

2. **(Optional) Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate   # For macOS/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

> The app will open in your default browser at: `http://localhost:8501`

---

## 🖼️ Screenshots

> *(Add UI screenshots here if available)*  
Example:
![screenshot](screenshots/demo.png)

---

## 💡 Example Inputs

- **Input**: “Traveling to the mountains this weekend”  
- **Generated Caption**: “Adventure awaits! 🏔️ Who else loves mountain getaways?”

---

## 👨‍💻 Author

- **Utkarsh Maheshwari**
- 📧 utkarsh.maheshwari0106@gmail.com  
- 🔗 [LinkedIn](https://www.linkedin.com/in/utkarsh-maheshwari-6b9978266)

---

## 📜 License

This project is under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
