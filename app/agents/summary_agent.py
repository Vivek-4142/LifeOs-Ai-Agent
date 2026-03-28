class SummaryAgent:
    def run(self, analysis_result: dict):
        emails = analysis_result.get("emails", [])

        important = [e for e in emails if e["classification"] == "important"]
        newsletters = [e for e in emails if e["classification"] == "newsletter"]
        promotional = [e for e in emails if e["classification"] == "promotional"]

        summary_text = (
            f"You have {len(important)} important emails, "
            f"{len(newsletters)} newsletters, and "
            f"{len(promotional)} promotional emails."
        )

        return {
            "status": "success",
            "summary_text": summary_text,
            "important_count": len(important),
            "newsletter_count": len(newsletters),
            "promotional_count": len(promotional),
            "important_emails": important
        }