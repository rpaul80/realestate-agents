from typing import TypedDict

from langchain.prompts import PromptTemplate

from llms import get_model
from state import AgentState, RealEstateListing

analyze_listing_page_prompt = """
You are tasked with analyzing some raw HTML and return back a list of objects.
The HTML is not valid as it will be scrubbed of un-important markup for this task.

The HTML content is below
<html_content>
{html_content}
</email_body>
"""


def analyze_listing_page(state: AgentState):
    html_content = state.get("html_content")
    model = get_model().with_structured_output(RealEstateListing)
    prompt = PromptTemplate(template=analyze_listing_page_prompt)

    runnable = prompt | model
    response = runnable.invoke({"html_content": html_content})

    return {"listing": response}
