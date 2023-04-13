"""Defines all the functions related to the database"""
from app import postgres


def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """
    cursor = postgres.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id ASC;")
    data = cursor.fetchall()
    postgres.commit()
    cursor.close()
    todo_list = []
    for result in data:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated description
    Returns:
        None
    """
    cursor = postgres.cursor()
    query = "UPDATE tasks SET task = '{}' WHERE id = {};".format(text, task_id)
    cursor.execute(query)
    postgres.commit()
    cursor.close()


def insert_new_task(text: str, id: int) -> int:
    """Insert new task to todo table.
    Args:
        text (str): Task description
    Returns:
        The task ID for the inserted entry
    """
    cursor = postgres.cursor()
    query = "INSERT INTO tasks (id, task, status) VALUES ({},'{}', '{}');".format(
        id, text, 'Todo')
    cursor.execute(query)
    postgres.commit()
    cursor.close()

    return query


def remove_task_by_id(task_id: int) -> None:
    """ Remove entries based on task ID """
    try:
        cursor = postgres.cursor()
        query = 'DELETE FROM tasks WHERE id={}'.format(task_id)
        cursor.execute(query)
        postgres.commit()
        cursor.close()
    except:
        print("test")



def fetch_max_id() -> int:
    try:
        cursor = postgres.cursor()
        query = "SELECT MAX(id) from tasks"
        cursor.execute(query)
        data = cursor.fetchall()
        postgres.commit()
        cursor.close()

        return data
    except:
        print("Failed")

    


# #Creating a connection cursor
# cursor = postgres.cursor()

# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')

# #Saving the Actions performed on the DB
# postgres.commit()

# #Closing the cursor
# cursor.close()
