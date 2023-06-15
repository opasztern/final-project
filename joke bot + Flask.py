# We're importing all the necessary modules from flask and the random module for picking a random joke
from flask import Flask, request, render_template, redirect, url_for
import random

# We're creating a new web application
app = Flask(__name__, static_url_path='/static')

# Function to read jokes from a text file and return them as a list
def read_jokes_from_file(file_name):
    # Open file and read lines
    with open(file_name, 'r') as file:
        return file.readlines()

# Here we're reading jokes from 3 different files and storing them in three lists
knock_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\knock_jokes.txt")
dad_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\dad_jokes.txt")
programming_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\programming_jokes.txt")

# The route() decorator tells Flask what URL should trigger our function
@app.route('/', methods=['GET', 'POST'])
def home():
    # If method is POST, that means the form on home.html is submitted
    if request.method == 'POST':
        # Redirect to joke page
        return redirect(url_for('joke', name=request.form.get('name')))
    # Otherwise render home.html
    return render_template('home.html')

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    # Get name from form submission, if not present then it's an empty string
    name = request.args.get('name', "")
    # Prepare an empty string for joke
    joke = ""
    # If method is POST, that means the form on joke.html is submitted
    if request.method == 'POST':
        # Get the category of joke selected
        category = request.form.get('category')
        # Depending on the category, select a random joke from the corresponding list
        if category=="knock knock":
            # Check if list is not empty
            if len(knock_jokes_list)>0:
                # Pick a random joke and remove it from the list
                joke = random.choice(knock_jokes_list)
                knock_jokes_list.remove(joke)
            else:
                # If no more jokes are left in the list
                joke = "Sorry, we have no more knock knock jokes left ):"
        elif category=="dad":
            # Repeat the same process for dad jokes
            if len(dad_jokes_list)>0:
                joke = random.choice(dad_jokes_list)
                dad_jokes_list.remove(joke)
            else:
                joke = "Sorry, we have no more dad jokes left ):"
        elif category=="programming":
            # Repeat the same process for programming jokes
            if len(programming_jokes_list)>0:
                joke = random.choice(programming_jokes_list)
                programming_jokes_list.remove(joke)
            else:
                joke = "Sorry, we have no more programming jokes left ):"
        else:
            # If the category selected is not valid
            joke = "Please only choose between 'knock knock', 'dad' or 'programming', otherwise we can't move forward :)"
    # Render the joke.html template and pass name and joke as variables
    return render_template('joke.html', name=name, joke=joke)

# This is the route that is called when the "Thanks" button is clicked
@app.route('/thanks', methods=['POST'])
def thanks():
    # Get name from form submission
    name = request.form.get('name')
    # If the 'again' form variable is 'yes', redirect to joke page
    if request.form.get('again') == 'yes':
        return redirect(url_for('joke', name=name))
    # Otherwise render the thanks.html page
    return render_template('thanks.html')

# If this script is run directly (rather than being imported), start the server
if __name__ == '__main__':
    app.run(debug=True)
