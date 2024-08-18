from langgraph.graph import END, MessagesState, StateGraph

from nodes.analyze_email import analyze_email
from nodes.analyze_listing_page import analyze_listing_page
from nodes.fetch_details import fetch_url
from nodes.finish import finish
from state import AgentState, OutputState


def get_agent():
    workflow = StateGraph(AgentState, input=MessagesState, output=OutputState)
    workflow.add_node(analyze_email)
    workflow.add_node(fetch_url)
    workflow.add_node(analyze_listing_page)
    workflow.add_node(finish)

    workflow.set_entry_point("analyze_email")
    workflow.add_edge("analyze_email", "fetch_url")
    workflow.add_edge("fetch_url", "analyze_listing_page")
    workflow.add_edge("analyze_listing_page", "finish")
    workflow.add_edge("finish", END)

    return workflow.compile()
