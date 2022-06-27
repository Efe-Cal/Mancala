from flask import Flask,render_template,redirect,send_file,url_for,request

app = Flask(__name__)

@app.route("/play/<id>")
def play_game(id):
    return render_template("game_page.html")

if __name__ == "__main__":
    app.run(debug=True)
