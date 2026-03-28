from app.services.llm_service import LLMService
from app.data.mock_emails import MOCK_EMAILS


class EmailAnalysisAgent:
    def __init__(self):
        self.llm = LLMService()

    def run(self, user_request=None, intent=None):
        """
        Analyze and classify all emails.
        """
        system_prompt = """
You are an email classification agent for a LifeOS system.

Classify each email into one of:
- important
- newsletter
- promotional

Return only valid JSON in this format:
{
  "emails": [
    {
      "id": 1,
      "classification": "important",
      "reason": "short reason"
    }
  ]
}
"""

        user_prompt = f"""
Classify the following emails:
{MOCK_EMAILS}
"""

        result = self.llm.chat_json(system_prompt, user_prompt, temperature=0.1)

        if not isinstance(result, dict) or result.get("error") or "emails" not in result:
            return self._fallback_analysis()

        analyzed = []
        valid_ids = {email["id"] for email in MOCK_EMAILS}

        for item in result["emails"]:
            if (
                isinstance(item, dict)
                and item.get("id") in valid_ids
                and item.get("classification") in ["important", "newsletter", "promotional"]
            ):
                analyzed.append({
                    "id": item["id"],
                    "classification": item["classification"],
                    "reason": item.get("reason", "No reason provided")
                })

        if not analyzed:
            return self._fallback_analysis()

        return {
            "emails": analyzed,
            "total_emails": len(analyzed)
        }

    def _fallback_analysis(self):
        analyzed = []

        for email in MOCK_EMAILS:
            analyzed.append({
                "id": email["id"],
                "classification": email.get("category_hint", "important"),
                "reason": "Fallback classification based on mock metadata"
            })

        return {
            "emails": analyzed,
            "total_emails": len(analyzed)
        }