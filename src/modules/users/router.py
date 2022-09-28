from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.models import User
from src.modules.users.schemas import UserIn
from src.modules.users.schemas import UserOut
from utils.database import create_or_modify_instance
from utils.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserOut)
def register(request: UserIn, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(phone_number=request.phone_number).first()

    if not user:
        user = User()
        create_or_modify_instance(user, request)
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
