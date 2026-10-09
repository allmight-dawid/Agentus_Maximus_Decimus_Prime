import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions
from prompts import system_prompt


def generate_content(client: OpenAI, messages: list, verbose: bool):
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages,
        tools=available_functions,
    )
    # Checking if any tool calls are present, if so, printing them
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            return print(f"Calling function: {tool_call.function.name}({function_args})")

    if response is not None and verbose == True:
        return print(
            f"""User prompt: {messages[1]["content"]}\n
            Prompt tokens: {response.usage.prompt_tokens}\n
            Response tokens: {response.usage.completion_tokens}\n
            {response.choices[0].message.content}"""
        )
    elif response is not None:
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
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.prompt
        }
    ]

    # Generating a response
    generate_content(
        client=clientus_agentus,
        messages=messagium_agentum,
        verbose=verbose_flag_bool
    )

if __name__ == "__main__":
    main()
