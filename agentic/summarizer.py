from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.agents import AgentState, create_agent
from langgraph.graph.state import Runnable

from integrations.bgg import BGGThread
from agentic.utils import last_message_parser


class SummarizerState(AgentState[str]):
    review: BGGThread


def build_summarizer_agent() -> Runnable[SummarizerState, str]:
    human_prompt = HumanMessagePromptTemplate.from_template(
        template="""
        Please find the key idea and the most important game feature in the following review:
        <review-title>
        {{review.subject}}
        </review-title>
        <review-body>
        {{review.comments|map(attribute='body')|join('\n\n')}}
        </review-body>
        """.strip(),
        template_format="jinja2",
    )
    system_prompt = SystemMessage(
        """
    You are an eager board game player looking for what makes a game special and unique.
    Make sure you highlight the key game features when summarizing a board game review.
    """.strip()
    )

    prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    agent = create_agent(model="gpt-5-nano")

    return prompt | agent | last_message_parser()
