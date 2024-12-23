# AI Chatbot with Together.ai, Streamlit, and Python uv
Welcome to the AI Chatbot project! This repository provides the code and instructions needed to create a chatbot using Together.ai's models, Streamlit for the user interface, and the uv framework for managing your virtual environments.

## Table of Contents
- Introduction
- Features
- Requirements
- Installation
- Usage

# Contributing

# License

# Introduction
This project demonstrates how to create an AI-powered chatbot leveraging Together.ai's language models. We use Streamlit to build an interactive web application and manage our Python environment using the uv framework. This setup allows for a seamless development experience and efficient project management.

# Features
### AI-Powered Responses: Utilizes Together.ai's language models for generating conversational responses.

### User-Friendly Interface: Interactive web application built with Streamlit.

### Environment Management: Efficiently manage dependencies and environments using the uv framework.

## Requirements
- Python 3.8 or later
- uv framework
- Together.ai API key

## Streamlit

### Installation
## Step 1: Clone the Repository
```sh
bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

Step 2: Set Up Virtual Environment using uv
```
Install uv if you haven't already:
```

```
pip install uv
```

Create and activate a virtual environment:

```
uv venv chatbot-env
source chatbot-env/bin/activate
```

Step 3: Install Dependencies
Install the required packages:

```
uv pip install streamlit together
```
Step 4: Set Up Together.aiAPI Key

Sign up for a Together.aiaccount and generate an API key. Store this key in an `.env` file in the project root:

```
TOGETHER_API_KEY='your_together_api_key_here'
```

Step 5: Update Configuration
Make sure your app.py or main script includes the following environment variable setup:

````
python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
Usage
Step 1: Run the Chatbot
Run the Streamlit application:
````

```
streamlit run app.py
````
Step 2: Interact with the Chatbot
Open your web browser and navigate to the provided local URL (typically http://localhost:8501). Start chatting with the AI-powered assistant!


Detailed Tutorial : https://youtu.be/8HmE1VEthbw?feature=shared


Contributing
We welcome contributions! Please fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.
