from agents.planner_agent import PlannerAgent
from agents.budget_agent import BudgetAgent
from agents.booking_agent import BookingAgent

class CommunicationAgent:
    def __init__(self):
        self.agents = {
            "planner": PlannerAgent(),
            "budget": BudgetAgent(),
            "booking": BookingAgent()
        }

    def decide_next(self, message):
        if not message["plan"]:
            return "planner"

        if "total_cost" not in message:
            return "budget"

        if "hotel" not in message["plan"][0]:
            return "booking"

        return None

    def run(self, destination, days, budget):
        message = {
            "destination": destination,
            "days": days,
            "budget": budget,
            "plan": []
        }

        while True:
            next_agent = self.decide_next(message)

            if next_agent is None:
                break

            print(f"📩 Routing to {next_agent}")

            agent = self.agents[next_agent]
            message = agent.handle(message)

        return message