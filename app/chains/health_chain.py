

class HealthBotChain:
    def __init__(self, agents):
        self.agents = agents

    def run(self, message):
        if not self.health_bot.is_healthy():
            return "Health check failed. Please try again later."
        
        response = self.health_bot.get_health_status()
        return f"Health check successful: {response}"