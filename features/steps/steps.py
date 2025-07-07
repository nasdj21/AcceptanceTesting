from behave import given, when, then # pylint: disable=no-name-in-module
from todo_list import ToDoList
from task import Task
import re



#Scenario #1: Add a task to the to-do list


#Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_given_empty_list(context):
    #Set the to-do list as an empry list
    context.todo = ToDoList()

#Step 2: When the user adds a task "Read paper"
@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    #Add the task to the to-do list
    context.todo.add_task(task)

#Step 3: Then, the to-do list should contain "Read paper"
@then('the to-do list should contain "{task}"')
def step_then_list_contains_task(context, task):
    #CHeck if the task is in the to-do list
    output = context.todo.list_tasks()
    assert task.description in output, f'Task "{task.description}" not found in the to-do list'



#Scenario #2: List all tasks in the to-do list

#Step 1: Given the to-do list contains tasks
@given('the to-do list contains tasks')
def step_given_list_contains_task(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task_by_hand(row['Task'])

@when('the user lists all tasks')
def step_when_user_lists_tasks(context):
    context.output = context.todo.list_tasks()

@then('the output should contain:')
def step_then_output_contains(context):
    for row in context.table:
        assert row['Task'] in context.output

#Scenario #3: Mark a task as completed
@when('the user marks task "{description}" as completed')
def step_when_mark_completed(context, description):
    context.todo.complete_task(description)

@then('the to-do list should show task "{description}" as completed')
def step_then_task_completed(context, description):
    output = context.todo.list_tasks()
    pattern = f"{description}.*Completed"
    assert re.search(pattern, output)


