import edge_tts
import asyncio

#Esta es la función que se encarga de descargar los audios de las palabras
#Se descargan en ingles, con la voz de Guy Neuronal

async def descar_sonidos(texto, i):
    voice = "en-US-GuyNeural"
    communicate = edge_tts.Communicate(texto, voice)
    #ruta en el que se van a guardar los audios
    #al final de la ruta hay una B_ y un i, esa B se cambia dependiendo de la categoría que se esté procesando(A o B)
    #y el i es el número de la palabra en la lista
    await communicate.save(f"C:/Users/ASUS/Documents/MISALES PASTRANA BORRERO/1102 2025/GORETTI/spelling_bee_page/assets/audios/B_{i}.mp3")

# Lista de palabras (se debe cambiar categoryB por la lista a procesar, es decir, categoryA o categoryB)
#las palabras deben estar entre comillas y separadas por comas: ("example", "words")
categoryB = [
    "AGREEMENT", "DYNAMITE", "JUPITER", "PROSPECTOR", "ANGULAR", "EMOTION",
    "KNOWLEDGE", "PROSPEROUS", "ANNOUNCE", "ENGAGEMENT", "LATENCY", "PSYCHIC",
    "APOCALYPSE", "ENTERTAINMENT", "LUCRATIVE", "PURIFICATION", "ARCHERY",
    "EQUILIBRIUM", "MICROORGANISM", "QUESTIONNAIRE", "ATMOSPHERE",
    "ESTABLISHMENT", "MULTITUDE", "RECRUIT", "AUDITORIUM", "EXHIBITION",
    "MUSCLE", "RELUCTANT", "AWARENESS", "EXPOSURE", "MYSTERIOUS", "SAUCE",
    "BISCUIT", "EXTERMINATE", "NUMEROLOGY", "SCULPTURE", "BUDGET", "EXTINGUISH",
    "OPPORTUNITY", "SEATBELT", "CAFFEINE", "FANTASY", "OVERWEIGHT",
    "SKATEBOARDING", "CALORIES", "FLIGHT", "OYSTER", "SOLITAIRE", "CHILDHOOD",
    "FLUENCY", "PASSAGE", "SOUNDTRACK", "CITIZENSHIP", "FORECAST", "PASSWORD",
    "SUFFICIENCY", "COARSE", "FORGIVENESS", "POSSESSION", "SUPREMACY",
    "CONFESS", "GEESE", "PUNISHMENT", "SWALLOW", "CORPULENT", "GEOGRAPHY",
    "SKYSCRAPER", "SWIMMER", "COURAGE", "GLASSES", "PEACEKEEPER", "SYLLABUS",
    "CREATURE", "GLOVES", "PERCEPTIBLE", "SYMPATHY", "CRIMINAL", "GRAVITY",
    "PITCH", "TERRITORY", "CROCODILE", "GUILTY", "PLAGIARISM", "THUNDERSTORM",
    "CRYSTAL", "HERITAGE", "PRELIMINARY", "UNFORGETTABLE", "CYBERSPACE",
    "HESITATE", "PROCEDURE", "VEGETARIAN", "DEFENSE", "ILLEGAL", "PRODIGIOUS",
    "VENUE", "DISPOSITION", "INDOLENT", "PROFILE", "WARRIOR"
]

# Procesar todas las palabras
# Se debe cambiar categoryB por la lista a procesar, es decir, categoryA o categoryB
#si es categoryA, se debe cambiar categoryB por categoryA, o viceversa
for word in categoryB:
    asyncio.run(descar_sonidos(word, categoryB.index(word) + 1))
    
