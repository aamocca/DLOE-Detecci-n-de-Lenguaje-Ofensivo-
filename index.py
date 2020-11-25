from flask import Flask, render_template

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



if __name__ == '__main__':
  app.run(debug=True)