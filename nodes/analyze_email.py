import requests
from langchain.prompts import PromptTemplate

from llms import get_model
from state import AgentState, BaseListing

analyze_email_prompt = """
You are tasked with analyzing the body of an email of a real estate listing alert and return back
an a list of objects.
The email body is below:
<email_body>
{email_body}
</email_body>
"""


def analyze_email(state: AgentState):
    email_body = state["messages"][-1].content
    model = get_model().with_structured_output(BaseListing)
    prompt = PromptTemplate(template=analyze_email_prompt)
    runnable = prompt | model
    response = runnable.invoke({"email_body": email_body})

    # augment state
    return {"listing_url": response}


analyze_listing_page_prompt = """
You are tasked with analyzing some raw HTML and return back a list of objects.
The HTML is not valid as it will be scrubbed of un-important markup for this task.

The HTML content is below
<html_content>
{html_content}
</email_body>
"""
