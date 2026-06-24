from api.server import run
from mcp.server import tool_run


def test_run_returns_a_string():
    # Placeholder smoke test so the pipeline is green out of the box.
    # Replace this with real tests for your agent.
    assert isinstance(run("ping"), str)


def test_mcp_wrapper_delegates():
    assert tool_run("ping") == run("ping")
