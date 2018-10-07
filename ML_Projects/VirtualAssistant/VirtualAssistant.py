import speech_recognition as sr

class VirtualAssistant:
	def __init__(self):
		self.r = sr.Recognizer()

	def TranslateSpeech(self):
		with sr.Microphone() as source:
			print("Say something!")
			audio = self.r.listen(source)

		try:
			return self.r.recognize_google(audio)
		except sr.UnknownValueError:
			return "Google could not understand audio"
		except sr.RequestError as e:
			return "Sphinx error; {0}".format(e)

def main():
	va = VirtualAssistant()
	print(va.TranslateSpeech())

if __name__ == '__main__':
	main()