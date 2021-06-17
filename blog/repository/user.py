from blog import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from ..hashing import Hash



def create(req: schemas.User, db:Session):
    new_user = models.User(name = req.name, email = req.email, password = Hash.encrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_by_id(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = {
            'detail': f'User with the id {id} not available'})
    else:
        return user

