"""/mcp — a thin MCP wrapper over /api. Expose your /api functions as MCP tools here."""
from api.server import run


def tool_run(payload: str = "ping") -> str:
    """Exposed as an MCP tool; delegates to your business logic in /api."""
    return run(payload)
