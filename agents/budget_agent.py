class BudgetAgent:
    def handle(self, message):
        itinerary = message["plan"]
        budget = message["budget"]

        total_cost = sum(day["estimated_cost"] for day in itinerary)

        if total_cost > budget:
            for day in itinerary:
                day["estimated_cost"] *= 0.8
            message["status"] = "Adjusted ⚠️"
        else:
            message["status"] = "Within Budget ✅"

        message["total_cost"] = total_cost
        return message