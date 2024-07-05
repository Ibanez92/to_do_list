from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Todo class for Todo items
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Define the DeletedTodo class for deleted Todo items
class DeletedTodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create the SQLite database
with app.app_context():
    db.create_all()

# READ
# Route to display all todos
@app.route("/")
def show_todos():
    todos = Todo.query.all()
    deleted_todos = DeletedTodo.query.all()
    return render_template("index.html", todos=todos, deleted_todos=deleted_todos)

# Route to add a new todo
@app.route("/add", methods=["POST"])
def add_todo():
    content = request.form["content"]
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("show_todos"))

# Route to toggle todo completion status
@app.route("/toggle/<int:id>")
def toggle_complete(id):
    todo = Todo.query.get(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("show_todos"))

# Route to delete a todo (move to history)
@app.route("/delete/<int:id>")
def delete_todo(id):
    todo = Todo.query.get(id)
    deleted_todo = DeletedTodo(content=todo.content)
    db.session.add(deleted_todo)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("show_todos"))

# Route to permanently delete a todo from history
@app.route("/permanent_delete/<int:id>")
def permanent_delete_todo(id):
    deleted_todo = DeletedTodo.query.get(id)
    db.session.delete(deleted_todo)
    db.session.commit()
    return redirect(url_for("show_todos"))

if __name__ == "__main__":
    app.run(debug=True)
