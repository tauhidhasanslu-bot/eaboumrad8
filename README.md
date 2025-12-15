# Role-Based LLM

This project allows Large Language Models (LLMs) to generate role-specific responses by integrating Google and HuggingFace models. It's designed to improve contextual relevance and accuracy through tailored prompting. To use it, clone the repository, set up your API keys in a `.env` file, and run the provided FastAPI server.

## Run Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd role_based_llm
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys, for example:
    ```
    GOOGLE_API_KEY=your_google_api_key
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
    ```
4.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
    Or for the multipi API:
    ```bash
    uvicorn multipi_api:app --reload
    ```
5.  **Run the interactive script (optional):**
    ```bash
    python 1.py
    ```
## Folder Structure

```
root
 |
 ---> .gitignore
 |
 ---> main.py
 |
 |
 ---> README.md
 |
 ---> requirements.txt
 |
 ---> component
 |    |
 |    ---> core
 |    |    |
 |    |    ---> db_config.py
 |    |    |
 |    |    ---> gemini_model.py
 |    |    |
 |    |    ---> hug_model.py
 |    |
 |    ---> model
 |    |    |
 |    |    ---> chat_history.py
 |    |    |
 |    |    ---> crud_repo.py
 |    |
 |    ---> services
 |         |
 |         ---> prompt.py
```
## File Descriptions

*   `.gitignore`: This `.gitignore` file specifies files and directories to be excluded from Git version control. It prevents sensitive environment configuration files (`.env`) and Python's compiled bytecode cache (`venv/`, `__pycache__/`) from being tracked, ensuring a cleaner and more secure repository.
*   `main.py`: This FastAPI application serves as an API for a role-based LLM system. It handles user queries, generates prompts based on user roles, and interacts with a Gemini LLM. The system stores user and AI responses in a database, linking them to chat sessions. It also provides functionality to retrieve chat history.
*   `requirements.txt`: This `requirements.txt` file lists essential Python packages for a role-based LLM application. It includes FastAPI for building the API, LangChain and its related libraries for LLM orchestration, Hugging Face and Google GenAI integrations for model access, and PyMongo for MongoDB connectivity. These dependencies enable the development of a sophisticated LLM-powered backend.
*   `component/core/db_config.py`: This Python script establishes a connection to a MongoDB database using credentials loaded from environment variables. It utilizes `dotenv` for managing secrets and `pymongo` for database interaction. The `get_dbconnection` function returns a specific database object, `naturopath_db`, after successfully pinging the server.
*   `component/core/gemini_model.py`: This Python code defines a function `model` that initializes and returns a `ChatGoogleGenerativeAI` model. It's designed to be a reusable component for interacting with Google's Gemini language models. The function allows specifying the `model_name` and configures parameters like `temperature` and `top_p` for controlling the model's output creativity and focus.
*   `component/core/hug_model.py`: This Python code defines a function `model` that initializes and returns a chat model from Hugging Face. It utilizes `HuggingFaceEndpoint` to connect to a specified model repository (defaulting to "openai/gpt-oss-120b") for text generation. The `ChatHuggingFace` wrapper then makes this endpoint accessible as a chat-style model.
*   `component/model/chat_history.py`: This Python code retrieves chat history for a given `chat_id`. It fetches user messages from 'user_collection' and AI messages from 'ai_collection' using a `get_all` function. The function then combines these into a dictionary, returning a structured representation of the chat's conversational flow.
*   `component/model/crud_repo.py`: This Python code defines a simple CRUD (Create, Read, Update, Delete) repository for interacting with a MongoDB database. It provides functions to `insert` new documents into a specified collection and `get_all` documents associated with a particular `chat_id`. The `get_dbconnection` function is assumed to handle establishing the database connection.
*   `component/services/prompt.py`: This Python code defines a function `prompt_generate` that dynamically constructs a prompt for a language model. It combines a system message, a user's query, and a specified user role into a formatted `PromptTemplate`. This allows the LLM to respond with context tailored to the given role, enhancing the specificity and accuracy of its output.
