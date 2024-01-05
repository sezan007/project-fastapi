from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import database,oauth2,schemas,models
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:int=Depends(oauth2.get_current_user)):
    vote=db.query(models.post).filter(vote.post_id==models.post.id).first()
    if not vote:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found")
    db_query=db.query(models.vote).filter(models.vote.user_id==current_user.id,models.vote.post_id==vote.post_id)
    found_vote=db_query.first()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f" user with id :{current_user.id} has already voted for the post with id :{vote.post_id}")
        # elif not found_vote:
        #     return {"message":"post doesn't exist"}
        new_vote= models.vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Successfully added vote"}
    
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"vote dosen't exist")
        
        db_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"successfully unvoted"}