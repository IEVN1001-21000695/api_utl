from flask import Flask, render_template
 
app =Flask(__name__)
 
@app.route("/")
def index():
    titulo="SOy un titulo"
    list=['Pedro','Juan','Fulanito']
    return render_template('uno.html',titulo=titulo,list=list)
 
@app.route("/user/<string:user>")
def user(user):
    return "el usuario es {}".format(user)
 
@app.route("/numero/<int:n1>")
def numero(n1):
    return "el numero es {}".format(n1)
 
 
@app.route("/user/<string:nom>/<int:id>")
def user2(nom, id):
    return "<h1> ID:{} Nombre: {}</h1>".format(id, nom)
 
@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1, n2):
    return "<h1> la suma es: {}</h1>".format(n1 + n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def nom2(nom='kas'):
    return "<h1> el nombre es {}</h1>".format(nom)
 
 
 
if __name__=="__main__":
    app.run(debug=True)
   