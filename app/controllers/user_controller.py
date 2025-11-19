from fastapi import APIRouter
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate):
    return service.create_user(data)

@router.get("/", response_model=list[UserResponse])
def get_users():
    return service.get_users()
