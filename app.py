from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel   
from typing import List
import os

app = FastAPI()

db_config = {
    'user': 'root',
    'password': 'yahya9339',
    'host': '127.0.0.1',
    'database': 'task_database'
}

class Task(BaseModel):
    p_task_name: str
    p_completed: bool=False
    
# GET Method 
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('sp_get_tasks')
        
        # Fetch 
        tasks = []
        for result in cursor.stored_results():
            tasks = result.fetchall()
            
            cursor.close()
            conn.close()
            
            return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
# POST Method
@app.post("/tasks/")
def add_tasks(task: Task):
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # stored procedure to add task
        cursor.callproc('sp_add_tasks', [task.p_task_name, task.p_completed])
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"message": "Task Added Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    

        
        
