from ast import If


inaltime = 145
varsta = 23
greutate = 45
nume = "Alexa"

print(f"Numele este {nume}, am inaltimea {inaltime}, greutatea {greutate}")

imc = (varsta + inaltime) / greutate

print(imc)

if imc < 3:
    print ("da")
else:
    print("nu")