from pydantic import BaseModel

class Resources(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: str

class ResourceDetails(BaseModel):
    id: int
    resource_id: int
    resource_link: str
    created_at: str
