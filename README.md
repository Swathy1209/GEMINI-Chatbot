# Gemini Chatbot

## Overview
This project is a chatbot powered by Google's Gemini AI model using Streamlit. It provides conversational responses and image-based insights.

## Features
- Uses **Gemini-Pro** for text-based chat.
- Uses **Gemini Vision** for image-based responses.
- **Streamlit UI** for a user-friendly chatbot interface.
- **Maintains chat history** within a session.

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed along with `pip`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/gemini-chatbot.git
   cd gemini-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Google API Key (Replace with your actual key in a `.env` file):
   ```bash
   GOOGLE_API_KEY=your-api-key
   ```
4. Run the chatbot application:
   ```bash
   streamlit run QA.py
   ```

## Usage
### Text-Based Chatbot (QA.py)
- Open the **Streamlit web interface** in your browser.
- Enter a question in the chat input box.
- Click **Ask the Question** to get a response.
- View chat history displayed in the interface.

### Image-Based Chatbot (img_model.py)
- Upload an image.
- Enter a text prompt (optional).
- Click **Tell me about the image** to receive AI-generated insights.

## File Structure
```
gemini-chatbot/
│── QA.py          # Chatbot for text-based queries
│── img_model.py   # Chatbot for image-based responses
│── requirements.txt  # Required dependencies
│── README.md      # Project documentation
```

## Dependencies
- **Streamlit**: For the chatbot UI.
- **Google Generative AI SDK**: For accessing Gemini AI.
- **PIL**: For image handling in `img_model.py`.
- **Dotenv**: For managing API keys securely.

## Customization
- Modify `QA.py` to **change chat behavior**.
- Edit `img_model.py` to **enhance image-processing capabilities**.

## License
This project is licensed under the MIT License.

## Contributors
- **Swathiga S** (swathiga22@gmail.com)

## Acknowledgments
Special thanks to **Google Generative AI**, **Streamlit**, and the **open-source community** for enabling this project.

