class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self):
        self.llm = None
        self.memory = None
        self.tools = None
        self.planner = None

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""
        return f"Received: {task}"

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""
        return f"Executed action: {action}"