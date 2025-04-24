# Development Assist Agent

The **Development Assist Agent** is an AI-powered virtual assistant designed to help developers solve technical problems and provide assistance on programming topics. The agent is composed of specialized subagents, such as the **Researcher**, which performs web searches to ensure that the information provided is always up-to-date. This project was developed with Google ADK (Agent Development Kit)

## What is ADK?

The Agent Development Kit (ADK) is a flexible, modular framework for developing and deploying AI agents. The ADK can be used with popular LLMs and open-source generative AI tools, and is designed with integration with the Google ecosystem and Gemini models in mind. The ADK makes it easy to get started with simple agents powered by Gemini models and Google AI tools, while providing the control and structure needed for more complex agent architectures and orchestrations.

To learn more: https://google.github.io/adk-docs/

## Features

- **Researcher**: Performs real-time web searches on topics related to development and programming, ensuring that answers are always based on the most recent information.
- **Development Assist**: Instructs the user, guiding them on a technical learning journey focused on programming languages, frameworks and tools.

## Architecture

The project consists of a set of agents that collaborate with each other to provide complete and detailed answers. The main agent's workflow includes:

1. **Greetings**: The agent introduces itself to the user in a joking manner and collects information about the request.
2. **Search**: The agent performs a real-time search, using the **Researcher** subagent, to ensure that the information provided is up-to-date.
3. **Tone**: Adjusts the response tone to a technical, friendly and jovial style. 4. **Key Constraints**: Targeted responses to solve problems in a practical and efficient way.

## How to Run

### Prerequisites

- Python 3.10 or higher
- Dependencies listed in the `requirements.txt` file

### Steps to run

1. Clone the repository:

```bash
git clone git@github.com:ju4nv1e1r4/agents-with-adk.git
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate # Linux/macOS
env\Scripts\activate # Windows
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set the environment variables in the `.env` file:

```bash
# If using Gemini via Google AI Studio
GOOGLE_GENAI_USE_VERTEXAI="False" GOOGLE_API_KEY="paste-your-actual-key-here"

# # If using Gemini via Vertex AI on Google CLoud
# GOOGLE_CLOUD_PROJECT="your-project-id"
# GOOGLE_CLOUD_LOCATION="your-location" #e.g. us-central1
# GOOGLE_GENAI_USE_VERTEXAI="True"

```

> If you are using Google Cloud, uncomment and set the appropriate variables for Vertex AI.

5. To run the agent in the terminal, use the following command:

```bash
adk run dev_assist/
```

6. To run the web interface locally:

```bash
adk web
```

Access the application at [http://localhost:8000](http://localhost:8000).

## How it Works

1. The **Development Assist** starts a conversation with the user, asking how it can help.
2. The **Researcher** subagent performs a web search to ensure that the answers are always up to date.
3. The **Development Assist** provides answers with examples and detailed explanations.
4. The agent adjusts its tone to be technical, friendly, and youthful, ensuring a light and informative learning experience.

## Deploy to Google Cloud
A bash script will be available in the `deployment` directory to perform the deployment manually.

## Author

Juan Vieira 

**Where can you find me?**

- [GitHub](https://github.com/ju4nv1e1r4)
- [LinkedIn](https://www.linkedin.com/in/juanvieira85/)
- [Medium](https://medium.com/@ju4nv1e1r4)

Thanks and I hope you enjoy it!