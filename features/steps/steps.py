from behave import given, when, then # pylint: disable=no-name-in-module
from todo_list import ToDoList
from task import Task
import re



#Scenario #1: Add a task to the to-do list


@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo = ToDoList()

@when('the user adds a task "{description}"')
def step_when_add_task(context, description):
    context.todo.add_task(description)

@then('the to-do list should contain "{description}"')
def step_then_list_contains(context, description):
    output = context.todo.list_tasks()
    assert description in output


#Scenario #2: List all tasks in the to-do list

#Step 1: Given the to-do list contains tasks
@given('the to-do list contains tasks')
def step_given_tasks(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@when('the user lists all tasks')
def step_when_list_all(context):
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


