from app.agents.planning_agent import PlanningAgent
from app.agents.intent_agent import IntentAgent
from app.agents.email_action_agent import EmailActionAgent


class OrchestratorAgent:
    def __init__(self):
        self.planning_agent = PlanningAgent()
        self.intent_agent = IntentAgent()
        self.email_action_agent = EmailActionAgent()

    def run(self, user_request: str):
        # Step 1: Planning
        plan = self.planning_agent.run(user_request)

        # Step 2: Intent detection
        intent_result = self.intent_agent.run(user_request)
        intent = intent_result.get("intent", "inbox_cleanup")

        # DEBUG print (very useful)
        print("DEBUG PLAN:", plan)
        print("DEBUG INTENT:", intent_result)
        print("DEBUG FINAL INTENT USED:", intent)

        # Step 3: Execute email action
        result = self.email_action_agent.run(user_request, intent)

        return {
            "status": "success",
            "user_request": user_request,
            "plan": plan,
            "intent_result": intent_result,
            "result": result
        }