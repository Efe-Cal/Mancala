from flask import Flask,render_template,redirect,url_for,request
from mangala import Mangala
from socket import gethostbyname,gethostname

app = Flask(__name__)
ip_addr = gethostbyname(gethostname())
mang=Mangala()
app.config["DEBUG"] = False
def secret_key_maker(app,e=10):
    i =1
    karakterler=["a","b","c","d","e","f","g","ı","i","j","1","2","3","4","5","6","7","8","9","!","'","^","$",",","*","?","{","}","-","_","#","æ","€","´","@","¹","│","Å","┘","à","┴","ê","╚"]
    secret_key = ""
    from random import randint
    while i <= e:
        secret_key+=karakterler[randint(0,len(karakterler)-1)]
        i+=1
    app.config["SECRET_KEY"]=secret_key
secret_key_maker(app)


@app.route("/")
def play_game(reload=False):
    
    return render_template("game_page.html",**mang.send_data())

@app.route("/play/<player>/<index>",methods=["POST"])
def play(player,index):
    mang.play(int(index),int(player))
    print(mang.tahta)
    return redirect(url_for('play_game'))
    
if __name__ == "__main__":
    app.run(debug=False,host=ip_addr)
