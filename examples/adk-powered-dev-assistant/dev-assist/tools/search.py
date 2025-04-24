from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search
from ..shared_libraries import constants

_researcher = Agent(
    model=constants.BASE_MODEL,
    name="researcher",
    description="Web research on a topic.",
    instruction="""
        Answer the user's question directly using Google's search engine; provide a brief but concise answer.
        Instead of a detailed answer, provide the developer with an immediate action item in a single sentence.
        Don't ask the user to verify or look up information on their own; that's your job; do your best to be informative.
        """,
    tools=[google_search]
)

google_search_grounding = AgentTool(agent=_researcher)
