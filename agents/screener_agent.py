from typing import Dict, Any
from .base_agent import BaseAgent

class ScreenerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name = "Screener",
            instructions= """Screen cadidates based on:
            - Qualification alignment
            - Experience releavance
            - Skill match percentage
            - Cultural fit indicators
            - Red flags or concerns

            Provide comprehensive screening reports."""
        )

    async def run(self, messages list) -> Dict[str, Any]:
        """Screen the candidate"""
        print("Screener: Condicting initial screening")

        workflow_context = eval(messages[-1]["content"])
        screening_result = self._query_ollama(str(workflow_context))

        return{
            "screening_report" : screening_result,
            "screening_timestamp "
            },

        
