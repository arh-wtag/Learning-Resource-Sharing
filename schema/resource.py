from pydantic import BaseModel
from datetime import datetime

class Resources(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime

class ResourceDetails(BaseModel):
    id: int
    resource_id: int
    resource_link: str
    created_at: datetime
