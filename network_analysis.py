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

result = network_analysis('mexican')
print(result)

