class UnsubscribeAgent:
    def run(self, analysis_result: dict):
        emails = analysis_result.get("emails", [])
        newsletters = [e for e in emails if e["classification"] == "newsletter"]

        unsubscribed = []
        for email in newsletters:
            unsubscribed.append({
                "id": email["id"],
                "status": "unsubscribed",
                "reason": "Detected newsletter email"
            })

        return {
            "status": "success",
            "total_newsletters": len(newsletters),
            "unsubscribed_emails": unsubscribed
        }