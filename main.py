from flask import Flask, request 
from datetime import datetime

app = Flask('MY First Application') 

@app.route('/')
def index():
    return """
    <h1>Claude Website</h1>
    <p>My name is Claude</p>
    """

@app.route('/nyandikira')
def contact_page():
    return "Contact me at habiclaude88@gmail.com or 0788597359"

@app.route('/date')
def date_page():
    date = str(datetime.now())
    return f"Today is {date}"

@app.route('/birthyear', methods=["POST", "GET"])
def calc_birthyear():
    if request.method == "POST":
        return f"""
        <form action='birthyear' method='POST'>
            <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
            <input type="submit" name="submit">
        </form>
        From your submition your age is {2022 - int(request.form.get('birthyear'))}
        """

    elif request.method == "GET":
        return """
        <form action='birthyear' method='POST'>
            <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
            <button type="submit">submit</button>
        </form>
        """
if __name__ == "__main__":
    app.run()
