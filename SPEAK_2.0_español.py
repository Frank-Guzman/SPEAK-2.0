#Decidi meterle mano al codigo original debido a que el programa fallaba mucho
# y a varios cuates les daba quebradero de cabeza!!
#Ademas que estaba en ingles y no reconocia las palabras en español
#espero que pueda ayudarles en sus proyectitos sin que se la compliquen tanto
#Un gran saludo a todos y todas desde Honduras (Franklin 'AR' Guzman) :3


from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import pyfiglet
#importo la libreria pyttsx3 debido a que re y gtts me estaban dando muchos problemas.
import pyttsx3

#se llama la funcion i se ingresan los parametros de idioma mas el rate o velocidad de voz.
engine = pyttsx3.init()
voice_id = 'spanish-latin-am'
engine.setProperty('voice', voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

#esto solo define la funcion y despliega el banner las opciones :v

print('\n#Uso:\n#Diga"ABRE -- site.com" para abrir cualquier pagina.\n#diga "SALIR" para salir del programa.\n')

def banner():
    ascii_banner = pyfiglet.figlet_format("SPEAK 2.0")
    print(ascii_banner)


#Saludo inicial y la hora!!
def Saludo():
    
    engine.say('hola')
    engine.runAndWait()
    currentTime = datetime.datetime.now()
    print(currentTime,'\n')
    if currentTime.hour < 12:
        engine.say('buenos dias')
        engine.runAndWait()
        print('Hola Buenos dias \n')
    elif 12 <= currentTime.hour < 18:
        engine.say('buenas tardes')
        engine.runAndWait()
        print('Hola Buenas Tardes \n')
    else:
        engine.say('Buenas noches')
        engine.runAndWait()
        print('Hola Buenas Noches \n\n')

#el audio se pasara a esta funcion
def speak(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("dice " + audio)
        

#escucha lo que dices!!
def ownerCommand():
        
        r = sr.Recognizer() # lo que dices se guarda en la variable
        with sr.Microphone() as source:
            print('\n En que le puedo servir? \n')
        
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1) #sirve para reducir el ruido hambiente ;)
            audio = r.listen(source)

        try:
            
            storeCommand = r.recognize_google(audio, language='es-MX').lower() # mete los parametros
    # del reconocimiento de voz ahora es en español ;)

            print('usted me pidio este sitio : ' + storeCommand + '\n')
            engine.say('ejecutando' + storeCommand + '\n')
            engine.runAndWait()
            #bueno ya sabemos para que es el except XD
        except sr.UnknownValueError: 
            print('Lo siento , no\'escuche lo que dijiste!!')
            storeCommand = ownerCommand();

        return storeCommand

#esta funcion ejecutara las ordenes que le demos al programa :3
def virtualAssist(storeCommand):
    if 'abre' in storeCommand:
        reg = re.search('abre (.+)', storeCommand)
        if reg:
            domain = reg.group(1) #groupo(1) es usado para capturar el string 
            url = ('https://www.' + domain)
            webbrowser.open(url)
            print('Vamo a Darle Con todo!!!........\n')
        else:
            pass

    elif 'salir' in storeCommand:
        engine.say('Hasta luego')
        engine.runAndWait()
        print('Hasta luego....')
        exit()
        

banner()
Saludo()
while True:
    virtualAssist(ownerCommand())

# Animo Banda!!!! :v
