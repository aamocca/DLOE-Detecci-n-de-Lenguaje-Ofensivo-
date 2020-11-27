from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')
   
@app.route('/resultado')
def resultado():
 return render_template('resultado.html')

@app.route('/reportar')
def reportar():
 return render_template('reportar.html') 

@app.route('/quienessomos')
def quienessomos():
 return render_template('quienessomos.html') 

@app.route('/objetivo')
def objetivo():
 return render_template('objetivo.html')

@app.route('/notas')
def notas():
 return render_template('notas.html')

@app.route('/nota1')
def nota1():
  return render_template('nota1.html') 

@app.route('/nota2')
def nota2():
  return render_template('nota2.html')  

@app.route('/nota3')
def nota3():
  return render_template('nota3.html') 


if __name__ == '__main__':
  app.run(debug=True)