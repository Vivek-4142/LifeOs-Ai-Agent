class PlanningAgent:
    def run(self, user_request: str):
        text = user_request.lower()

        # Full optimization
        if (
            ("clean" in text or "cleanup" in text) and
            ("unsubscribe" in text or "remove subscription" in text) and
            ("summary" in text or "summarize" in text)
        ):
            return {
                "domain": "email",
                "intent": "full_email_optimization",
                "reason": "Detected cleanup + unsubscribe + summary"
            }

        # Inbox cleanup
        if any(word in text for word in ["clean", "cleanup", "delete promotions", "remove spam", "organize inbox"]):
            return {
                "domain": "email",
                "intent": "inbox_cleanup",
                "reason": "Fallback keyword match for cleaning inbox"
            }

        # Subscription management
        if any(word in text for word in ["unsubscribe", "remove newsletter", "stop emails", "cancel subscriptions"]):
            return {
                "domain": "email",
                "intent": "subscription_management",
                "reason": "Detected subscription management request"
            }

        # Summary
        if any(word in text for word in ["summary", "summarize", "important emails", "brief inbox"]):
            return {
                "domain": "email",
                "intent": "email_summary",
                "reason": "Detected email summary request"
            }

        # Default
        return {
            "domain": "email",
            "intent": "inbox_cleanup",
            "reason": "Default fallback to email cleanup"
        }