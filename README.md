# CGPTNoLogin-Wrapper

## Overview

CGPTNoLogin-Wrapper is a Python wrapper for [ChatGPT No Login](https://chatgptnologin.com/), designed to simplify interactions with OpenAI's language models. This wrapper acts as a "real" OpenAI server, serving as a reverse proxy for the ChatGPT No Login API. It eliminates the need for explicit API keys, making it seamless for developers to integrate OpenAI's powerful language models into their applications.

## Features

- **Flask Server**: Utilizes the Flask framework to create an HTTP server, offering a scalable solution for handling requests.

- **Reverse Proxy**: Acts as a reverse proxy for the ChatGPT No Login API, allowing developers to seamlessly make requests to the wrapper as if it were the actual OpenAI server.

- **Model Selection**: Supports multiple language models, with the default being "gpt-3.5-turbo." Developers can easily specify the desired model in their requests.

- **Temperature Control**: Allows users to control the randomness of the model's responses by setting the temperature parameter.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Recentaly/CGPTNoLogin-Wrapper.git
   cd CGPTNoLogin-Wrapper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the wrapper:
   ```bash
   python app.py
   ```

2. Make API requests to `http://localhost:5000`:

   - **Chat Completion Endpoint**: Send POST requests to `/chat/completions` with a JSON payload containing messages, model information, and optional temperature settings.

     Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d @example_payload.json http://localhost:5000/chat/completions
     ```

   - **Get Models Endpoint**: Send GET requests to `/models` to retrieve a list of available models.

     Example:
     ```bash
     curl http://localhost:5000/models
     ```

## Code Structure

- **app.py**: The main Flask application file that handles HTTP requests. It defines routes for chat completions and getting available models.

- **res/src/Api.py**: The API class responsible for interacting with the ChatGPT No Login API. It includes methods for fetching available models and initiating a chat.

## Configuration

- **Models**: Models are specified in the `models` dictionary within `app.py`. You can add or modify models by updating this dictionary.

- **Server Configuration**: The Flask server runs on `http://0.0.0.0:5000` by default. You can customize the host and port in the `if __name__ == "__main__":` block in `app.py`.

## Understanding Models

### Available Models

The wrapper provides support for multiple models. Some examples include:

- **gpt-3.5-turbo**: Default model for general-purpose language tasks.
- **gpt-4-0125-preview**: More advanced, newest OpenAI model.
- **gpt-4-1106-preview** Also more advanced but a tiny bit filtered.

### Fetching Model Information

To retrieve information about available models, make a GET request to `/models`. This will return a JSON object containing details about each model, including `id` and `name`.

Example Response:
```json
{
  "data": [
    {"id": "gpt-3.5-turbo", "name": "GPT-3.5 Turbo"},
    {"id": "gpt-4-0125-preview", "name": "GPT-4"},
    {"id": "gpt-4-1106-preview", "name": "GPT-4"}
  ]
}
```
