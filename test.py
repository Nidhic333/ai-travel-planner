from agents.communication_agent import CommunicationAgent

agent = CommunicationAgent()

# 🔥 TAKE INPUT FROM USER
destination = input("Enter destination: ")
days = int(input("Enter number of days: "))
budget = int(input("Enter budget: "))

# run system
result = agent.run(destination, days, budget)

print("\n📊 FINAL OUTPUT")
print("Status:", result["status"])
print("Total Cost:", result["total_cost"])

print("\n📅 Detailed Itinerary:")
for day in result["plan"]:
    print(f"Day {day['day']}: {day['activity']}")
    print(f"  Cost: ₹{day['estimated_cost']}")
    print(f"  Hotel: {day['hotel']}")
    print(f"  Transport: {day['transport']}")
    print()