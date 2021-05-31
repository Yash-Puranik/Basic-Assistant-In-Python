import webbrowser
import pyttsx3

# Query #
while True:
    command = input("Please Enter Your Query: ")
    pyttsx3.speak(command)

# Open Google #
    if command == 'Open Google':
        pyttsx3.speak("Opening Google")
        webbrowser.open('www.google.com')

# Open Youtube #
    elif command == 'Open YouTube':
        pyttsx3.speak("Opening Youtube")
        webbrowser.open('www.youtube.com')

# Open Github #
    elif command == 'Open GitHub':
        pyttsx3.speak("Opening Github")
        webbrowser.open('www.github.com')

# Play Music #
    elif command == 'Play Music':
        pyttsx3.speak("Opening Spotify")
        webbrowser.open('www.spotify.com')

# Normal Movies #
    elif command == 'Play Movie':
        pyttsx3.speak("Opening Youtube")
        webbrowser.open('https://www.youtube.com/channel/UClgRkhTL3_hImCAmdLfDE4g')

# Anime Movies #
    elif command == 'Play Anime Movie':
        pyttsx3.speak("Opening GoGoAnime")
        webbrowser.open('www.gogoanime1.com')

# Information #

    elif command == 'Open Wikipedia':
        pyttsx3.speak("Opening Wikipedia")
        webbrowser.open('www.wikipedia.com')

# Open Whatsapp #

    elif command == 'Open WhatsApp':
        pyttsx3.speak("Opening WhatsApp")
        webbrowser.open('web.whatsapp.com')

# Open Telegram #

    elif command == 'Open Telegram':
        pyttsx3.speak("Opening Telegram")
        webbrowser.open('web.telegram.org')

# Open Twitter

    elif command == 'Open Twitter':
        pyttsx3.speak("Opening Twitter")
        webbrowser.open('www.twitter.com')

# Open Instagram #

    elif command == 'Open Instagram':
        pyttsx3.speak("Opening Instagram")
        webbrowser.open('web.instagram.com')

# Rename System's Name #

    elif command == 'Rename System':
        pyttsx3.speak("What will be my new name?")
        sysName = input("What Will Be My New Name?: ")
        pyttsx3.speak("My new name is " + sysName)

# Invalid Command #
    else:
        pyttsx3.speak("Invalid Command!")
