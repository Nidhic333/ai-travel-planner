class BookingAgent:
    def handle(self, message):
        for day in message["plan"]:
            if day["estimated_cost"] < 1000:
                day["hotel"] = "Budget Hotel"
                day["transport"] = "Bus"
            else:
                day["hotel"] = "Standard Hotel"
                day["transport"] = "Cab"

        return message