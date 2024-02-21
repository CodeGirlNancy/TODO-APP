from flask import Flask,render_template,request,redirect,url_for

# Creating an instance
app = Flask(__name__,template_folder="templates")

tasks=[]

app.config['STATIC_FOLDER'] = 'static'  # Replace with your actual static folder path

# routing 
@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)

#creating anew task 
@app.route("/add_task",methods=["POST"])
def create_task():
    task=request.form.get("Add a new task")
    tasks.append(task)#add variables to alist
    return redirect(url_for("index"))# pass in the fuction name 

#The delete task deletes the user tasks when the user clicks the delete button
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    del tasks [task_id]
    return redirect(url_for('home'))

#ENABLING THE DEBUG MODE
# if __name__=="__main__":
   #app.run(debug= True)