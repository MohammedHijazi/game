from flask import Flask,request,render_template
import dataset


app = Flask(__name__)

db=dataset.connect("sqlite:///gamesLebrery")

games=db["games"]




@app.route("/")
def home():
	return render_template("index.html",Games=db["games"])


@app.route("/addGame", methods=["get","post"])
def showGame():
	if(request.method=="POST"):
		name=request.form["name"]
		Developer=request.form["Developer"]
		publisher=request.form["publisher"]
		desp=request.form["desp"]
		games.insert(dict(name=name,Developer=Developer,publisher=publisher,desp=desp))
		return render_template("index.html",Games=db["games"])
	else:
		return render_template("addGame.html")



@app.route("/showMore/<gameId>")
def showMore(gameId):
	sm=games.find_one(id=gameId)
	return render_template("ShowMore.html",game=sm)



@app.route("/delete/<gameId>",methods=["post"])
def delete(gameId):
	games.delete(id=gameId)
	return render_template("index.html",Games=db["games"])



@app.route("/edit/<gameId>",methods=["post","get"])
def editGame(gameId):
	if (request.method=="GET"):
		ed=games.find_one(id=gameId)
		return render_template("editGame.html",game=ed)
	else:
		name=request.form["name"]
		Developer=request.form["Developer"]
		publisher=request.form["publisher"]
		desp=request.form["desp"]
		data=dict(id = gameId , name=name,Developer=Developer,publisher=publisher,desp=desp)
		games.update(data,["id"])
		return render_template("index.html",Games=db["games"])


if __name__ == "__main__":
	app.run(port=5050)

	


