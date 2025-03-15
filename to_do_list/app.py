from flask import Flask, render_template, request

app = Flask(__name__)

todol = []  

@app.route("/todo", methods=["GET", "POST"])
def todo():
    global todol  

    if request.method == "POST":
        action = request.form.get("submit")  

        if action == "Add Task":  
            task = request.form.get("task")  
            if task:
                todol.append(task)

        elif action == "Delete First Todo" and todol: 
            todol.pop(0)

        elif action == "Delete Last Todo" and todol: 
            todol.pop()

    return render_template("form.html", todo=todol)  

if __name__ == "__main__":
    app.run(debug=True)
