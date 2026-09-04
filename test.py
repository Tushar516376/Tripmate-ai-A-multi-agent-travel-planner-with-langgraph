from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res=tavily_search("best hotels in INDIA")

# res =search_flights("Plan a 7 days Japan trip from Bangladesh")
print("backend imported OK") 
user_input=input("Enter travel request:")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)
print(response["answer"])