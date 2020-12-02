from flask import Flask, render_template, request,redirect, url_for, render_template


app= Flask(__name__)

#Script abierto#

def write_to_csv(new_text):
    import csv
    with open('test.csv', "w") as test_file:
        test_writer = csv.writer(test_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='')
        test_writer.writerow(['','text'])
        test_writer.writerow(['0', new_text])
    
#script cerrado#


#Script Inteligencia#

def network_analysis(language): #mexican or spanish
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

    import pandas as pd
    from keras.models import load_model
    # Importando librerias
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences
    from keras.layers import Embedding, Dense, GlobalMaxPool1D, Dropout, Flatten, Bidirectional, LSTM
    from keras.models import Sequential

    if language == 'mexican':
        train_data = pd.read_csv('text_data_clean.csv')
        train_data = train_data[['Category','text']]
        model_name = 'Mexicanspanish_OLD_model.h5'
    elif language == 'spanish': 
        train_data = pd.read_csv('tweets_data_clean.csv')
        train_data.text = train_data.text.astype(str)
        model_name = 'spanish_OLD_model.h5'
    else:
        return None
    
    new_model = load_model(model_name)
    test = pd.read_csv('test.csv')
    test = test.text.astype(str)
    # num_words=(2000)
    max_len=200
    tokenizer=Tokenizer(2000)
    tokenizer.fit_on_texts(train_data.text)
    # train_sequences=tokenizer.texts_to_sequences(train_data.text)
    test_sequences=tokenizer.texts_to_sequences(test)
    padded_test = pad_sequences(test_sequences, maxlen=max_len)
    result = new_model.predict(padded_test)[0][0] 
    return result # Number between 0 and 1, closer to 1 means offensive, closer to 0 means not offensive

#Cierra inteligencia#


@app.route('/', methods=["POST", "GET"])
def home():
  if request.method == "POST":
    lang = request.form.get('lang') 
    text = request.form[lang]
    write_to_csv(text)
    return redirect (url_for("user",text = text, lang=lang))
    
  else:
    return render_template("home.html")
  
 

@app.route("/<text>-<lang>")
def user(text,lang):
  resultado= network_analysis(lang)
  print(text)
  return render_template('resultado.html',resultado=resultado, user=text)



   


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