from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class OrganizationCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)


class OrganizationResponse(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
