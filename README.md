# Todo App

## Overview

Todo application built with Flask and SQLAlchemy. The application allows users to add tasks, mark them as completed or pending, delete tasks, and view a history of deleted tasks with an option to permanently delete them.

## Technologies used

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Setup and Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**
    ```sh
    pip install flask flask-sqlalchemy

4. **Run the application:**
    ```sh
    flask run

The application will be available at http://127.0.0.1:5000/.

## Instructions
1. Enter the task content in the input box and click the "Add Task" button.
2. Click the "(Completed)" or "(Pending)" link next to the task to toggle its status.
3. Click the "Delete" link next to the task to move it to the deleted items history.
4. The deleted items will be listed under the "Deleted Items History" section.
5. Click the "Permanently Delete" link next to the deleted task.

## Design and Coding Choices
- Flask is a lightweight web framework that is easy to set up and use, and SQLAlchemy is a powerful ORM that simplifies database interactions.
- Todo application follows the MVC pattern, separating concerns and making the code easier to maintain and extend.
- Initially, adding new columns to the existing database schema caused issues. This was resolved by simplifying the implementation and focusing on core functionalities.
- Deciding how to handle the history of deleted items and ensuring that the user experience remains intuitive and seamless was a key challenge.

## Lessons Learned
- Planning the database schema and application flow beforehand can save a lot of time and effort during development.
- Understanding and debugging SQLAlchemy errors helped in learning more about ORM and database interactions.
- Simplifying the user interface and ensuring that the application is easy to use is crucial for creating a good user experience.