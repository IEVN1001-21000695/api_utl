from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import config
 
app =Flask(__name__)
con = MySQL(app)
 
@app.route("/alumnos",methods=['GET'])
def lista_alumnos():
    try:
        cursor = con.connection.cursor()
        sql = "select * from alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno={"matricula":fila[0],"nombre":fila[1],"apaterno":fila[2],"amaterno":fila[3],"correo":fila[4]}
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos,'mensake':'Lista de Alumnos','exito':True})
    except Exception as ex:
        return jsonify({"massage":"errors {}".format(ex),'exito':False}),500

@app.route("/alumnos/<mat>",methods=['GET'])
def leer_alumno(mat):
    try:
        alumno = leer_alumno_bd(mat)
        cursor = con.connection.cursor()
        sql = "select * from alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno={"matricula":fila[0],"nombre":fila[1],"apaterno":fila[2],"amaterno":fila[3],"correo":fila[4]}
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos,'mensake':'Lista de Alumnos','exito':True})
    except Exception as ex:
        return jsonify({"massage":"errors {}".format(ex),'exito':False}),500
  
if __name__=="__main__":
    app.run(debug=True)
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(host="0.0.0.0",port=5000)
   