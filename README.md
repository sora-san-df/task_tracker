# task_tracker
CLI project which is a todo app basically.


# What's this project about?

It is a project to practive the backend development skills. So that's what i'm doing. You can find this exact same project in https://roadmap.sh/projects/task-tracker.

You should be able to:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

Each task you create should generate a json file, where among the previous points i mentioned before, it must have too:

- id: A unique identifier for the task

- description: A short description of the task

- status: The status of the task (todo, in-progress, done)

- createdAt: The date and time when the task was created

- updatedAt: The date and time when the task was last updated

as properties

# What I'm gonna do specifically?

Since this is just for practice, nothing much really, but i have already planning a few extra concepts that i can add. :D 


## Plans

{
  "vault_id": 1,
  "description":"Text example",
  "tasks": [{
    "id": 1,
    "description": "Holaaa",
    "status": "todo, progress,done",
    "createdAt": "2025-03-14 12:00:00",
    "updatedAt": "2024-03-14 15:00:00"
  }]
}

this is how my code is gonna looks like, an extra requirement is that we should add a commanda to create a new vault. Our final file can be an array of vaults!

Added to that, we should have a dictionary where stores an array of vaults too.