from app.agents.email_analysis_agent import EmailAnalysisAgent
from app.agents.unsubscribe_agent import UnsubscribeAgent
from app.agents.summary_agent import SummaryAgent


class EmailActionAgent:
    def __init__(self):
        self.email_analysis_agent = EmailAnalysisAgent()
        self.unsubscribe_agent = UnsubscribeAgent()
        self.summary_agent = SummaryAgent()

    def run(self, user_request: str, intent: str):
        # Step 1: Analyze emails
        analysis = self.email_analysis_agent.run()

        emails = analysis.get("emails", [])

        # Step 2: Route by exact intent
        if intent == "inbox_cleanup":
            promotional_emails = [e for e in emails if e["classification"] == "promotional"]

            return {
                "status": "success",
                "action": "Inbox Cleanup",
                "message": f"Found {len(promotional_emails)} promotional emails for cleanup.",
                "emails": emails,
                "promotional_count": len(promotional_emails),
                "promotional_emails": promotional_emails
            }

        elif intent == "subscription_management":
            unsubscribe_result = self.unsubscribe_agent.run(analysis)

            return {
                "status": "success",
                "action": "Unsubscribe Newsletters",
                "message": f"Processed {unsubscribe_result['total_newsletters']} newsletter subscriptions.",
                "emails": emails,
                "unsubscribe_result": unsubscribe_result
            }

        elif intent == "email_summary":
            summary_result = self.summary_agent.run(analysis)

            return {
                "status": "success",
                "action": "Generate Summary",
                "message": "Generated inbox summary.",
                "emails": emails,
                "summary_result": summary_result
            }

        elif intent == "full_email_optimization":
            unsubscribe_result = self.unsubscribe_agent.run(analysis)
            summary_result = self.summary_agent.run(analysis)
            promotional_emails = [e for e in emails if e["classification"] == "promotional"]

            return {
                "status": "success",
                "action": "Full Email Optimization",
                "message": "Completed cleanup + unsubscribe + summary.",
                "emails": emails,
                "promotional_count": len(promotional_emails),
                "promotional_emails": promotional_emails,
                "unsubscribe_result": unsubscribe_result,
                "summary_result": summary_result
            }

        # Default fallback
        return {
            "status": "success",
            "action": "Default Email Analysis",
            "emails": emails,
            "message": f"Intent received: {intent}. No exact action matched, showing default email classification."
        }