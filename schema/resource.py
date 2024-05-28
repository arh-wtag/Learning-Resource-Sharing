from pydantic import BaseModel
from datetime import datetime

class Resources(BaseModel):
    title: str
    created_at: datetime

class ResourceDetails(BaseModel):
    resource_link: str
    created_at: datetime
