from uuid import UUID, uuid4

from fastapi import APIRouter

from app.schemas.organization import OrganizationCreate, OrganizationResponse

router = APIRouter()

_demo_orgs: dict[UUID, OrganizationResponse] = {}


@router.post("", response_model=OrganizationResponse, status_code=201)
def create_organization(payload: OrganizationCreate):
    organization = OrganizationResponse(id=uuid4(), name=payload.name)
    _demo_orgs[organization.id] = organization
    return organization


@router.get("", response_model=list[OrganizationResponse])
def list_organizations():
    return list(_demo_orgs.values())
