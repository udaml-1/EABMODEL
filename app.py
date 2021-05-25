import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

col1, col2 = st.beta_columns([1,2])
col1.image('Kyobi Labs.png', width=200)
col2.title('Identificador de equipo de laboratorio')

#import streamlit as st
#from img_classification import teachable_machine_classification
#import keras
#from PIL import Image, ImageOps
#import numpy as np

st.sidebar.image('Plano.png', width=200)


import streamlit as st
st.sidebar.title('E. A. B. M. O. D. E. L')



st.write('''Este programa está hecho con el fin de auxiliar al usuario, en la identificación de equipo de laboratorio, su respectiva función y manejo.
Para utilizar este programa, deberás cargar una imagen (en formato jpg), en su respectiva celda para su posterior identificación.
 El programa también cuenta con un Chatbot, el cual te ayudará en la resolución de tus posibles dudas sobre el de este equipo.''')

st.video("https://www.youtube.com/watch?v=Pm29jq_7SKs")
st.write("""[Si desean mas informacion seguir el siguente Link ](https://www.youtube.com/channel/UChB2uat-2Pl8mWxakNUa_pg)
""")

st.sidebar.header('UDA introduccion al machine learning')


st.sidebar.write('''
Integrantes:

* Michelle Itzuri Torres Avitia
* Nicol Rodriguez Silva 
* Isaac Ramirez Loya
* Neira Yanitsia Favela Rodriguez 
* Yara Georgina Bravo Borunda

''')



st.sidebar.write( '@uach.mx')

uploaded_file = st.file_uploader("Choose a Dog/Cat jpg pic ...", type="jpg")
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded pic.', use_column_width=True)
  st.write("")
  st.write("Classifying...")
  label = teachable_machine_classification(image, 'keras_model.h5') # Name of the model from Teachablemachine
  if label == 0:
    st.write("Probeta")

  if label == 1:
    st.write("Propipeta")
  
  if label == 2:
    st.write("Refrigerador de Laboratorio ")

  if label == 3:
    st.write("Rejilla de asbesto")

  if label == 4:
    st.write("Reómetro")

  if label == 5:
    st.write("Soporte universal de Laboratorio")

  if label == 6:
    st.write("Triángulo de porcelana")

  if label == 7:
    st.write("Tubo refrigerante o condensador")

  if label == 8:
    st.write("Vaso precipitado")

  if label == 9:
    st.write("Vidrio de reloj")
    
  if label == 10:
    st.write("Abatelenguas")

  if label == 11:
    st.write("Balanza Granataria")
  
  if label == 12:
    st.write("Cubre Objetos")

  if label == 13:
    st.write("Frasco de reactivos")

  if label == 14:
    st.write("Fiola")

  if label == 15:
    st.write("Gradilla")

  if label == 16:
    st.write("Horno de laboratorio")

  if label == 17:
    st.write("Mechero de alcohol")

  if label == 18:
    st.write("Pipeta graduada")

  if label == 19:
    st.write("Porta objetos")

  if label == 20:
    st.write("Tubo de ensayo")

  if label == 21:
    st.write("Escobilla de laboratorio")
  
  if label == 22:
    st.write("Mortero de laboratorio")

  if label == 23:
    st.write("Embudo Büchner ")

  if label == 24:
    st.write("Mechero Bunsen")
  if label == 25:
    st.write("Tubo capilar")

  if label == 26:
    st.write("Mufla")

  if label == 27:
    st.write("Papel filtro")

  if label == 28:
    st.write("Papel tornasol o papel pH")

  if label == 29:
    st.write("pHmetro")

  if label == 30:
    st.write("Pinza de crisol")

  if label == 31:
    st.write("Espatula")

    
  if label == 32:
    st.write("Microscopio")

    
  if label == 33:
    st.write("Matras de Erlenmeyer")

    
  if label == 34:
    st.write("Matras de aforo")

    
  if label == 35:
    st.write("Incubadora de Laboratorio")

    
  if label == 36:
    st.write("Embudo de decantacion")

    
  if label == 37:
    st.write("Embudo")

    
  if label == 38:
    st.write("Doble nuez")


  if label == 39:
    st.write("Desecador")

    
  if label == 40:
    st.write("Densimetro")

    
  if label == 41:
    st.write("Cristol de porcelana")

    
  if label == 42:
    st.write("Centrifuga de Laboratorio")

    
  if label == 43:
    st.write("Agitador vortex")


  if label == 44:
    st.write("Aparato de kipp")
      

  if label == 45:
    st.write("Argolla metalica")
    
  if label == 46:
    st.write("Autoclave")


  if label == 47:
    st.write("Balanza")
    

  if label == 48:
    st.write("Matraz de destilación")

  if label == 49:
    st.write("Baño maría")


  if label == 50:
    st.write("Bureta")
    

  if label == 51:
    st.write("Capsula de porcelana")


  if label == 52:
    st.write("Varilla")


#import streamlit as st
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
#import pandas as pd


#df = pd.read_csv('chatlab - chatlab.csv')

#input_text = st.text_input('Yo','Hola')

#talk = df['bot0'].tolist()
#talk= talk + df['bot1'].tolist()

#talk= talk + df['bot2'].tolist()
#talk= talk + df['bot3'].tolist()
#talk= talk + df['bot4'].tolist()
#talk= talk + df['bot5'].tolist()
#talk= talk + df['bot6'].tolist()
#talk= talk + df['bot7'].tolist()
#talk= talk + df['bot8'].tolist()
#talk= talk + df['bot9'].tolist()
#talk= talk + df['bot10'].tolist()
#talk= talk + df['bot11'].tolist()
#talk= talk + df['bot12'].tolist()
#talk= talk + df['bot13'].tolist()
#talk= talk + df['bot14'].tolist()
#talk= talk + df['bot15'].tolist()
#talk= talk + df['bot16'].tolist()
#talk= talk + df['bot17'].tolist()
#talk= talk + df['bot18'].tolist()
#talk= talk + df['bot19'].tolist()
#talk= talk + df['bot20'].tolist()
#talk= talk + df['bot21'].tolist()
#talk= talk + df['bot22'].tolist()
#talk= talk + df['bot23'].tolist()
#talk= talk + df['bot24'].tolist()
#talk= talk + df['bot25'].tolist()
#talk= talk + df['bot26'].tolist()
#talk= talk + df['bot27'].tolist()
#talk= talk + df['bot28'].tolist()
#talk= talk + df['bot29'].tolist()
#talk= talk + df['bot30'].tolist()
#talk= talk + df['bot31'].tolist()
#talk= talk + df['bot32'].tolist()
#talk= talk + df['bot33'].tolist()
#talk= talk + df['bot34'].tolist()
#talk= talk + df['bot35'].tolist()
#talk= talk + df['bot36'].tolist()
#talk= talk + df['bot37'].tolist()
#talk= talk + df['bot38'].tolist()
#talk= talk + df['bot39'].tolist()
#talk= talk + df['bot40'].tolist()
#talk= talk + df['bot41'].tolist()
#talk= talk + df['bot42'].tolist()
#talk= talk + df['bot43'].tolist()
#talk= talk + df['bot44'].tolist()
#talk= talk + df['bot45'].tolist()
#talk= talk + df['bot46'].tolist()
#talk= talk + df['bot47'].tolist()
#talk= talk + df['bot48'].tolist()
#talk= talk + df['bot49'].tolist()
#talk= talk + df['bot50'].tolist()
#talk= talk + df['bot51'].tolist()
#talk= talk + df['bot52'].tolist()
#bot = ChatBot('Robot')

#trainer = ListTrainer(bot)

#trainer.train(talk)

#respuesta_del_bot = str(bot.get_response(input_text))



col1, col2 = st.beta_columns([4,2])
col1.image('Bot.png', width=300)
col2.header('¿En qué te puedo ayudar?')
#col2.header('🤖 ' + respuesta_del_bot)
