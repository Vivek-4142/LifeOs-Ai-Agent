import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()


class LLMService:
    def __init__(self):
        """
        Initializes the OpenAI client and model config.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing in your .env file")

        self.client = OpenAI(api_key=self.api_key)

    def chat(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
        """
        Standard text response from the LLM.
        Returns plain text.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=temperature,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"LLM Error: {str(e)}"

    def chat_json(self, system_prompt: str, user_prompt: str, temperature: float = 0.1) -> dict:
        """
        Structured JSON response from the LLM.
        Attempts to parse the output as JSON.
        If parsing fails, returns an error dict.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=temperature,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            content = response.choices[0].message.content.strip()

            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON returned by model",
                    "raw_response": content
                }

        except Exception as e:
            return {
                "error": f"LLM API Error: {str(e)}"
            }