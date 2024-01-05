from fastapi import APIRouter,Depends,status,HTTPException,responses
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session

from ..import database,schemas,models,utils,oauth2

router=APIRouter(tags=['Authentication'])

@router.post('/login',response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:session=Depends(database.get_db)):
    # if not user_credentials:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"give something")
    user=db.query(models.User).filter(user_credentials.username==models.User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    #create a token
    #return token
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token" :access_token, "token_type" :"bearer"}
    