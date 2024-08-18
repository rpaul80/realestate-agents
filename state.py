from typing import List, TypedDict

from langgraph.graph import MessagesState
from pydantic import BaseModel, Field


class BaseListing(BaseModel):
    listing_detail_url: str = Field(
        description="The url to the real estate site where the details of the listing can be seen"
    )


class RealEstateListing(BaseListing):
    price: float = Field(description="The price of the property")
    building_style: str = Field(
        description="The kind of property, example detached, split-level, duplex, apartment, etc"
    )
    bedroom_count: str = Field(description="The number of bedrooms in the property")
    full_bathroom_count: int = Field(
        description="The number of full bathrooms on the property"
    )
    half_bathroom_count: int = Field(
        description="The number of powder rooms or half baths on the property"
    )
    year_built: int = Field(description="The year the property was built")
    lot_size: int = Field(description="The size of the lot")
    garage_spaces: int = Field(
        description="The number of parking spaces in the garage. If there is no evidence of a garage, use the value 0."
    )


class AgentState(MessagesState):
    email_body: str
    listing_url: BaseListing
    html_content: str
    listing: List[RealEstateListing]
    done: bool


class OutputState(TypedDict):
    listing: List[RealEstateListing]
    done: bool
