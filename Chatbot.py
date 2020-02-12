list = ["weather", "story"]
# output the first sentence
print("Welcome, i am a chatbot")
# asking the name and stored as a variable
name = input("how can i call you")
print("hi", name)
    
    

while True:   
    x = input("what can i help you with")
    x == x.split()    
    
    if x.split()in list:
        print("is good")
    else:
    # things the chatbot ablt to do
        a = """  you can ask me about the weather,
        you can ask me about a story"""
        print(a)    
    if x == "done":
        print("Thx, Bye")
        break


