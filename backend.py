from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "replace_with_secret_key"  # Needed for flash messages

# Example projects
projects = [
    {"name": "Market Forecast Dashboard", "description": "A Flask + Plotly app visualizing macroeconomic trends.", "link": "https://github.com/yourusername/project1"},
    {"name": "Trade Policy Analyzer", "description": "Python tool analyzing EU-US trade data.", "link": "https://github.com/yourusername/project2"},
    {"name": "Portfolio Tracker", "description": "A React + Flask app for tracking stock portfolios.", "link": "https://github.com/yourusername/project3"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def show_projects():
    return render_template("projects.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Here you could integrate email sending (e.g., with smtplib)
        print(f"New message from {name} ({email}): {message}")
        flash("Thanks for reaching out! I’ll get back to you soon.")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
