# language: en

Feature: To-do list manager
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Read paper"
        Then the to-do list should contain "Read paper"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks
            | Task |
            | Read paper |   
        When the user lists all tasks
        Then the output should contain:
            | Read paper |

    Scenario: Mark a task as completed
        Given the to-do list contains tasks
            | Task | Status |
            | Read paper | Pending |
        When the user marks task "Read Paper" as completed
        Then the to-do list should show task "Read paper" as completed

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
            | Task |
            | Read paper |
            | Pay bills |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Add duplicate task
        Given the to-do list is empty
        When the user adds a task "Read paper"
        And the user adds a task "Read paper"
        Then the to-do list should contain "Read paper" twice

    Scenario: Mark an already completed task
        Given the to-do list contains tasks
        When the user marks Task "Read Paper"
        And the user marks Task "Read paper"
        Then the to-do list should show task "Read paper" as completed
