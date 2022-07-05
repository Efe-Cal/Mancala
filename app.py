from flask import Flask,render_template,redirect,url_for,request
from mangala import Mangala

app = Flask(__name__)
mang=Mangala()

@app.route("/")
def play_game():
    return render_template("game_page.html",**mang.send_data())

@app.route("/play/<player>/<index>",methods=["POST"])
def play(player,index):
    mang.play(int(index),int(player))
    print(mang.tahta)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
