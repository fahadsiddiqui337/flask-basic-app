from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app (like starting a new project)
app = Flask(__name__)

# This is our "database" - just a list that stores tasks
# In real apps, you'd use a real database, but this is simpler!
tasks = []

# HOME PAGE - Shows all tasks
@app.route('/')
def index():
    """
    This function runs when someone visits your website.
    It shows the main page with all tasks.
    """
    return render_template('index.html', tasks=tasks)

# ADD TASK - When someone submits the form
@app.route('/add', methods=['POST'])
def add_task():
    """
    This function runs when someone clicks "Add Task".
    It takes the task from the form and adds it to our list.
    """
    # Get the task text from the form
    task_content = request.form.get('task')
    
    # Only add if the task isn't empty
    if task_content:
        # Create a task dictionary (like a mini database entry)
        task = {
            'id': len(tasks) + 1,  # Give it a unique number
            'content': task_content,
            'completed': False  # New tasks aren't completed yet
        }
        tasks.append(task)  # Add to our list
    
    # Go back to the home page
    return redirect(url_for('index'))

# COMPLETE TASK - Mark a task as done
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """
    This function runs when someone clicks "Complete" on a task.
    It marks that task as finished.
    """
    # Find the task with this ID
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True  # Mark it as done!
            break
    
    return redirect(url_for('index'))

# DELETE TASK - Remove a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """
    This function runs when someone clicks "Delete" on a task.
    It removes that task from the list.
    """
    # Remove the task with this ID
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return redirect(url_for('index'))

# Start the web server
if __name__ == '__main__':
    print(" Starting Task Manager...")
    print(" Open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)