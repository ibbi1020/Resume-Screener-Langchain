from typing import Dict, Any
import json
from openai import OpenAI

class BaseAgent:
    def __init__(self, name: str, instructions:str):
        self.name = name
        self.instructions = instructions
        self.ollama_client = OpenAI(
            base_url = "http://localhost:11434/v1",
            api_key = "ollama"
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Default run methof for all subclasses"""
        raise NotImplementedError("Subclasses must implement run()")
                                  
    async def _query_ollama(self, prompt:str) -> str:
        """Query ollama model using given prompt"""
        try:
            response = self.ollama_client.chat.completions.create(
                model = "llama3.2",
                messages = [
                    {"role": "system", "content":self.instructions},
                    {"role": "user", "content": prompt},
                ],
                temperature = 0.3,
                max_tokens = 2000,
            )
        except Exception as e:
            print(f"Error querying Ollama {str(e)}")
            raise
            
    def parse_json(self, text:str) -> Dict[str, Any]:
        """Safely parse JSON from text and handle any errors"""
        try:
            start = json.find("{")
            end = json.find("}")

            if start != -1 and end != -1:
                json_str  = text[start:end+1]
                return json.loads(json_str)
            return {"Error": "No JSON content found"}
        except json.JSONDecodeError:
            return {"Error": "Invalid JSON content"}
