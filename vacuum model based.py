class VacuumAgent:
    def __init__(self):
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }
        self.location = "A"

    def perceive(self, status):
        self.model[self.location] = status

    def decide_action(self):
        if self.model[self.location] == "Dirty":
            return "Suck"

        elif self.location == "A":
            return "Move Right"

        elif self.location == "B":
            return "Move Left"

        return "NoOp"

    def perform_action(self, action):
        if action == "Suck":
            self.model[self.location] = "Clean"

        elif action == "Move Right":
            self.location = "B"

        elif action == "Move Left":
            self.location = "A"


agent = VacuumAgent()

environment = {
    "A": "Dirty",
    "B": "Dirty"
}

for i in range(4):
    status = environment[agent.location]

    print("Location:", agent.location)
    print("Status:", status)

    agent.perceive(status)
    action = agent.decide_action()

    print("Action:", action)
    agent.perform_action(action)

    if action == "Suck":
        environment[agent.location] = "Clean"

    print()
