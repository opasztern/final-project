from flask import Flask, request, render_template
import random

app = Flask(__name__)

def read_jokes_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

knock_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\knock_jokes.txt")
dad_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\dad_jokes.txt")
programming_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\programming_jokes.txt")

@app.route('/', methods=['GET', 'POST'])
def joke_bot():
    joke = ""
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category').lower()
        if category=="knock knock":
            if knock_jokes_list:
                joke = random.choice(knock_jokes_list)
                knock_jokes_list.remove(joke)
            else:
                joke = "Sorry, we have no more knock knock jokes left ):"
        elif category=="dad":
            if dad_jokes_list:
                joke = random.choice(dad_jokes_list)
                dad_jokes_list.remove(joke)
            else:
                joke = "Sorry, we have no more dad jokes left ):"
        elif category=="programming":
            if programming_jokes_list:
                joke = random.choice(programming_jokes_list)
                programming_jokes_list.remove(joke)
            else:
                joke = "Sorry, we have no more programming jokes left ):"
        else:
            joke = "Please only choose between 'knock knock', 'dad' or 'programming', otherwise we can't move forward :)"
    return render_template('joke.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
