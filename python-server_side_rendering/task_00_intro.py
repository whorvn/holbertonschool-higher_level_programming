from flask import Flask, render_template

app = Flask(__name__, template_folder='subfolder/templates')

# Data for the invitations
invitations_data = [
    {"name": "Alice", "event": "Gala Dinner", "date": "July 25th, 2024", "location": "The Grand Ballroom"},
    {"name": "Bob", "event": "Tech Summit", "date": "August 10th, 2024", "location": "Convention Center"},
    # Add more invitations as needed
]

@app.route('/')
def invitations():
    return render_template('invitation.html', invitations=invitations_data)

if __name__ == '__main__':
    app.run(debug=True)