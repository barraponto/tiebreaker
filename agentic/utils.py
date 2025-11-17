from __future__ import annotations
from typing import TypeVar
from langchain.agents import AgentState
from langchain_core.messages import AnyMessage
from langchain_core.runnables import Runnable, RunnableLambda


def last_message(result: AgentState[str]) -> str:
    messages: list[AnyMessage] = result.get("messages", [])
    return messages[-1].text if messages else ""


def last_message_parser() -> Runnable[AgentState[str], str]:
    return RunnableLambda(last_message)


T = TypeVar("T")


def get_structured_response(result: AgentState[T]) -> T | None:
    return result.get("structured_response")


def structured_response_parser() -> Runnable[AgentState[T], T | None]:
    return RunnableLambda(get_structured_response)
