dict = { "communities" : [ {"community" : "readonly" , "type" : "RO", "community" : "readwrite" , "type" : "RW"} ] 
}

print(dict["communities"][0]["community"])

for community in dict["communities"]:
  if community["type"] == "RO":
     print (community["community"])




