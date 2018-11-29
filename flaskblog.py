from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        "author":"Ashwin",
        "title":"Blog 1",
        "content":"First Post",
        "date_posted":"Today"
    },

    {
        "author":"Ashwin Chandlapur",
        "title":"Blog 1",
        "content":"First Post By ",
        "date_posted":"Today Not Tomorrow"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = "About")

if __name__ == "__main__":
    app.run(debug=True)