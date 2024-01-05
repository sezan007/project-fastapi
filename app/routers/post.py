from .. import models,schemas
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List,Optional
from .. import oauth2
from sqlalchemy import func

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/",response_model=List[schemas.PostOut])
#@router.get("/")
def get_posts(db: Session = Depends(get_db),limit:int =10,skip:int =0,search:Optional[str]=""):
    #cur.execute("""SELECT * FROM posts""")
    #posts=cur.fetchall()
    #print(search)
    posts=db.query(models.post).filter(models.post.content.contains(search)).limit(limit).offset(skip).all()
    #print(posts)
    result=db.query(models.post,func.count(models.vote.post_id).label("votes")).join(models.vote,models.vote.post_id==models.post.id,
        isouter=True).group_by(models.post.id).filter(models.post.content.contains(search)).limit(limit).offset(skip)

    print(result)
    return result.all()
@router.get("/mypost",response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    #cur.execute("""SELECT * FROM posts""")
    #posts=cur.fetchall()
    print(current_user.id)
    posts=db.query(models.post).filter(current_user.id==models.post.owner_id).all()
    #posts=db.query(models.post).all()
    #print(posts)
    return posts
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post:schemas.PostCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cur.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published) )
    # new_post=cur.fetchone()
    # print(new_post)
    # conn.commit()
    #user_id=schemas.Tokendata(id=user_id)
    print(current_user.email)
    print("hellooo")
    new_post=models.post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post
@router.get("/latest",response_model=schemas.Post)
def get_latest_post():
    post=mypost[len(mypost)-1]
    return post
#@router.get("/{id}")
@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,resposnse:Response,db: Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    ##print(type(id))
    # post=find_post(id)
    # cur.execute(""" SELECT * FROM posts WHERE id =%s""",(str(id),))
    # post=cur.fetchone()
    post=db.query(models.post).filter(models.post.id==id).first()
    #print(post)
    if  post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
        ##resposnse.status_code=status.HTTP_404_NOT_FOUND
        ##return{"message ": f"post with id {id} not found"}
    # elif post.owner_id!=current_user.id :
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"unauthorizrd to perform action")
    result=db.query(models.post,func.count(models.vote.post_id).label("votes")).join(models.vote,models.vote.post_id==models.post.id,isouter=True).group_by(models.post.id).filter(models.post.id==id)

    print(result)
    results=result.first()
    return results
    #return  post
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
   ## index=find_index_post(id)
    # cur.execute(""" DELETE FROM posts WHERE id =%s RETURNING *""",(str(id),))
    # deleted_post=cur.fetchone()
    post_query=db.query(models.post).filter(models.post.id==id)
    post=post_query.first()
    if post==None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"No post found with id {id}")
    elif post.owner_id!=current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"unauthorizrd to perform action")       
    else:
        # print(deleted_post)
        # conn.commit()
        post_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int ,updated_post: schemas.PostCreate, db: Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cur.execute(""" UPDATE posts SET title=%s ,content=%s,published=%s  WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cur.fetchone()
    post_query = db.query(models.post).filter(models.post.id == id)
    post= post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No post found with id {id}")
    elif post.owner_id!=current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"unauthorizrd to perform action")   
    else:
        # print(update_post)
        post_query.update(updated_post.dict(),synchronize_session=False)
        db.commit()
    
    return post_query.first()