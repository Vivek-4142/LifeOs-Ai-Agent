class IntentAgent:
    def run(self, user_request: str):
        text = user_request.lower()

        # Full optimization first (combined intent)
        if (
            ("clean" in text or "cleanup" in text) and
            ("unsubscribe" in text or "remove subscription" in text) and
            ("summary" in text or "summarize" in text)
        ):
            return {
                "intent": "full_email_optimization",
                "reason": "Detected cleanup + unsubscribe + summary request"
            }

        # Inbox cleanup
        if any(word in text for word in ["clean", "cleanup", "delete promotions", "remove spam", "organize inbox"]):
            return {
                "intent": "inbox_cleanup",
                "reason": "Detected inbox cleanup request"
            }

        # Subscription management
        if any(word in text for word in ["unsubscribe", "remove newsletter", "stop emails", "cancel subscriptions"]):
            return {
                "intent": "subscription_management",
                "reason": "Detected unsubscribe / subscription management request"
            }

        # Email summary
        if any(word in text for word in ["summary", "summarize", "important emails", "what should i read", "brief inbox"]):
            return {
                "intent": "email_summary",
                "reason": "Detected email summary request"
            }

        # Fallback
        return {
            "intent": "inbox_cleanup",
            "reason": "Fallback to inbox cleanup for email-related requests"
        }