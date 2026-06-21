#opemai_client.py
from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key, openai_model) -> None:
        """
        Initializes the OpenAIClient with API key and model.
        """
        self.api_key = api_key
        self.model = openai_model
        self.system_message = None
        self.text = None
        self.prompt = None

    def openai_client(self, system_message=None, text=None, prompt=None):
        """
        Sends a request to the OpenAI API with the provided system message, text, and prompt.
        
        Args:
            system_message (str): The system's role message for the assistant.
            text (str): The user-provided input text to process.
            prompt (str): The prompt template, which may include placeholders.
        
        Returns:
            str: The response content from the OpenAI API.
        
        Raises:
            ValueError: If any of system_message, text, or prompt is missing.
        """

        if system_message is not None:
            self.system_message = system_message
        if text is not None:
            self.text = text
        if prompt is not None:
            self.prompt = prompt

        if not self.system_message or not self.text or not self.prompt:
            raise ValueError("system_message, text, and prompt are required")

        formatted_prompt = self.prompt.format_map({"text": self.text})

        client = OpenAI(api_key=self.api_key)

        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": formatted_prompt}
            ]
        )
        return completion.choices[0].message.content
