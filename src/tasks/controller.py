from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.utils.helpers import is_authenticated

def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(title=data['title'],
                        description=data['description'], 
                        is_completed=data['is_completed']
                        )



    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_task(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks


def get_one_task(task_id:int, db: Session):
    one_task = db.get(TaskModel, task_id)
    if one_task is None:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return one_task


def update_task(task_id:int, body: TaskSchema, db: Session):
    one_task = db.get(TaskModel, task_id)
    if one_task is None:
        raise HTTPException(status_code=404, detail="Task ID not found")
    
    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed

    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task

def delete_task(task_id:int, db: Session):
    one_task = db.get(TaskModel, task_id)
    if one_task is None:
        raise HTTPException(status_code=404, detail="Task ID not found")
    
    db.delete(one_task)
    db.commit()
    return None
