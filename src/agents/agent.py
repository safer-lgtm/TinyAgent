from agents.llm import Trajectory

class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self):
        self.llm = None
        self.memory = None
        self.tools = None
        self.planner = None

        self.trajectory = Trajectory()

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str | None:
        """Execute a tool action."""
        return f"Executed action: {action}"