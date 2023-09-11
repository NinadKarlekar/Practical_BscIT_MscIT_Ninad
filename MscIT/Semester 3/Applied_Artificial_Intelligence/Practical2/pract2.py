#pip install aiml
#pip install python-aiml

import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">Bot: "+response)
	
