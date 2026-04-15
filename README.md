#  AI Travel Planner (Multi-Agent System)

This project is a dynamic multi-agent AI system that generates travel itineraries based on user input such as destination, budget, and number of days.

##  Features

- Multi-agent architecture (Planner, Budget, Booking)
- Dynamic agent-to-agent (A2A) communication
- State-based routing system
- Flask-based web interface
- Real-time itinerary generation

##  System Design

The system uses a central Communication Agent that dynamically routes tasks between specialized agents:

- Planner Agent → generates itinerary
- Budget Agent → adjusts plan based on budget
- Booking Agent → suggests hotel and transport

##  Project Structure

agents/
- planner_agent.py
- budget_agent.py
- booking_agent.py
- communication_agent.py

templates/
- index.html

app.py  
test.py  
requirements.txt  

##  How to Run

1. Install dependencies:
2. Run the app: python app.py
3. Open browser: http://127.0.0.1:5000/


##  Example

Input:
- Destination: Goa
- Days: 3
- Budget: 2000

Output:
- Generated itinerary
- Cost breakdown
- Hotel & transport suggestions

##  Key Concepts

- Multi-Agent Systems
- Dynamic Routing
- State-based Decision Making
- Full-stack AI Application (Flask + Python)

---
