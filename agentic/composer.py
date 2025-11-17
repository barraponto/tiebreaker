from langchain.agents import AgentState, create_agent
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langgraph.graph.state import Runnable
from pydantic import BaseModel


class ReviewPost(BaseModel):
    title: str
    body: str


class ComposerState(AgentState[ReviewPost]):
    summaries: list[str]


def build_composer_agent() -> Runnable[ComposerState, AgentState[ReviewPost]]:
    system_prompt = SystemMessage("""
    You are a board game content creator looking to write a review for a board game.
    Based on what you have been told, write a review for the board game.
    Make sure to use markdown formatting for the review.
    """)
    human_prompt = HumanMessagePromptTemplate.from_template(
        template="""
        Please write a review with highlights taking these summaries into account:
        {% for summary in summaries %}

            <summary-{{loop.index}}>
                {{summary}}
            </summary-{{loop.index}}>

        {% endfor %}
        Make sure to use markdown formatting for the review.
        """.strip(),
        template_format="jinja2",
    )
    prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    agent = create_agent(
        model="gpt-5-nano", response_format=ReviewPost, state_schema=ComposerState
    )

    return prompt | agent
