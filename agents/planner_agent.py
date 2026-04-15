class PlannerAgent:
    def handle(self, message):
        destination = message["destination"]
        days = message["days"]

        attractions = {
            "goa": ["Beach", "Fort Aguada", "Water Sports", "Night Market"],
            "delhi": ["Red Fort", "India Gate", "Qutub Minar", "Lotus Temple"]
        }

        places = attractions.get(destination.lower(), ["City Tour"])
        itinerary = []

        for day in range(1, days + 1):
            itinerary.append({
                "day": day,
                "activity": places[(day - 1) % len(places)],
                "estimated_cost": 1000 + day * 200
            })

        message["plan"] = itinerary
        return message