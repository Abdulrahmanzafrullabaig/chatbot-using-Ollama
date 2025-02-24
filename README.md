# Chatbot with Ollama, Deepseek, Qwen, Python, and Flask

This repository contains the source code for a chatbot built using **Ollama**, **Deepseek**, and **Qwen** models. The chatbot runs entirely offline and is powered by **Python** and **Flask** to serve as a web-based interface.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Directory Structure](#directory-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

The chatbot leverages **Ollama** to run large language models like **Deepseek** and **Qwen** in an offline environment. It uses **Flask** to create a simple web interface where users can interact with the chatbot. This setup ensures that all data remains local, providing privacy and control over your interactions.

---

## Features

- **Offline Operation**: All models run locally, ensuring no external API calls or data leakage.
- **Multiple Models**: Supports both **Deepseek** and **Qwen** models via Ollama.
- **Web Interface**: A user-friendly web interface powered by Flask.
- **Customizable**: Easily extendable to support additional models or features.
- **Lightweight**: Minimal dependencies to ensure smooth operation on most systems.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Ollama**: Follow the installation instructions from the [Ollama official documentation](https://ollama.ai/).
- **Flask**: Install via `pip install flask`.
- **Deepseek & Qwen Models**: Download and configure these models using Ollama.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/chatbot-ollama.git
cd chatbot-ollama
```

### Step 2: Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Step 3: Install Ollama

Follow the instructions on the [Ollama website](https://ollama.ai/) to install Ollama on your system.

### Step 4: Download Models

Use Ollama to pull the **Deepseek** and **Qwen** models:

```bash
ollama pull deepseek
ollama pull qwen
```

### Step 5: Configure Environment Variables (Optional)

If you want to customize the model or other settings, create a `.env` file in the root directory:

```bash
MODEL=deepseek  # or qwen
FLASK_ENV=development
```

---

## Usage

### Step 1: Run the Flask Application

Start the Flask server:

```bash
python app.py
```

By default, the application will run on `http://127.0.0.1:5000/`.

### Step 2: Interact with the Chatbot

Open your browser and navigate to `http://127.0.0.1:5000/`. You should see the chatbot interface where you can type messages and receive responses.

### Switching Models

To switch between **Deepseek** and **Qwen**, modify the `MODEL` variable in the `.env` file or pass it as an environment variable:

```bash
export MODEL=qwen
python app.py
```

---

## Directory Structure

```
chatbot-ollama/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML template for the chatbot UI
├── static/
│   └── style.css         # CSS for styling the chatbot UI
├── .env                  # Environment variables (optional)
└── README.md             # This file
```

---

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- **Ollama**: For providing an easy way to run large language models locally.
- **Deepseek & Qwen**: For their powerful language models.
- **Flask**: For the lightweight web framework.

---

Feel free to reach out if you have any questions or need further assistance!
