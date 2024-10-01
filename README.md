# Installation Guide for Speechy

This guide will help you set up and run a Flask application that utilizes Google's Gemini AI model for generating conversational responses.

> [!IMPORTANT]
> Before you begin, ensure you have the following installed on your system:

- [Python 3.10](https://python.org) or later
- pip (Python package installer) - comes installed with python usually
- Git (optional, for cloning the repository)
- Gemini API Key (get it from [here](https://aistudio.google.com/app/apikey))

## Step 1: Clone the Repository

If you have git installed, you can clone it using the following command:

```bash
git clone https://github.com/cashsoftworks/speechy/
cd speechy
```

If not, just download it. It's not hard.

## Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

    ```bash
    venv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

## Step 3: Install Dependencies

Install the required packages by running:

```bash
pip install Flask google-generativeai
```

## Step 4: Set Up Google Gemini API Key

1. Obtain your Google Gemini API key from the Google Cloud Console.
2. Open your application file (e.g., `main.py`), and replace the placeholder key in the following line with your actual key:

   ```python
   key = "YOUR_API_KEY"  # Replace with your own key from Google
   ```

## Step 5: Run the Flask Application

You can now run the Flask application with the following command:

```bash
python main.py
```

By default, the app will run on `http://0.0.0.0:1024`.

## Step 6: Access the Application

Open your web browser and go to `http://localhost:1024` to access the application.

## Step 7: Interact with the Chatbot

Once the application is running, you can interact with the AI chatbot through the web interface.

## Troubleshooting

- Ensure your Python environment is correctly set up and activated.
- Make sure your API key is valid and has the necessary permissions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
