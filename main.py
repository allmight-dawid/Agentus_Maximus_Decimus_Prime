import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI


def generate_content(client: OpenAI, messages, verbose: bool):
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages
    )

    if response != None and verbose == True:
        return print(
            f"User prompt: {messages[0]["content"]}\nPrompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n{response.choices[0].message.content}"
        )
    elif response != None:
        return print(response.choices[0].message.content)
    else:
        raise RuntimeError("Failed API request, please try again and/or later")


def main():
    # Opening message, API key check
    print("Hello from agentus-ai!")
    load_dotenv()
    api_key: str | None = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("API key is empty, check the .env file")

    # Creating client instance, prompt parser to accept user prompts
    clientus_agentus = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
    )

    parser = argparse.ArgumentParser(description="Agentus Mechanicus")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose",action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    verbose_flag_bool = args.verbose

    # Creating a dict of roles & corresponding responses
    messagium_agentum = [
        {
            "role": "user",
            "content": args.prompt
        },
    ]

    # Generating a response
    generate_content(
        client=clientus_agentus,
        messages=messagium_agentum,
        verbose=verbose_flag_bool
    )

if __name__ == "__main__":
    main()
