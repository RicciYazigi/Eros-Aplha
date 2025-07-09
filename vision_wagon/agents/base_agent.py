class BaseAgent:
    def __init__(self, name: str, capabilities: list[str]):
        self.name = name
        self.capabilities = capabilities

    def __str__(self):
        return f"Agent: {self.name}, Capabilities: {', '.join(self.capabilities)}"

    def has_capability(self, capability: str) -> bool:
        return capability in self.capabilities
