from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi import status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog import schemas
from fastapi import APIRouter
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}