from langchain.agents import AgentState
from langchain_core.runnables import RunnableLambda
from langgraph.graph.state import Runnable

from agentic.summarizer import SummarizerState, build_summarizer_agent
from agentic.composer import ReviewPost, build_composer_agent
from agentic.utils import structured_response_parser


class CreatorChainState(AgentState[ReviewPost]):
    summaries: list[str]


def build_creator_chain() -> Runnable[list[SummarizerState], ReviewPost]:
    summarizer_agents = build_summarizer_agent().map()
    composer_agent = build_composer_agent()

    summaries_loader = RunnableLambda[list[str], CreatorChainState](
        lambda summaries: {"messages": [], "summaries": summaries}
    )

    return (
        summarizer_agents
        # pass the summarizer agent outputs as input to the writer agent prompts
        | summaries_loader
        | composer_agent
        # return only the writer agent structured response
        | structured_response_parser()
    )
