import ngrok

myVar = ngrok.forward(5000, authtoken_from_env =True)  
print(myVar.url())

