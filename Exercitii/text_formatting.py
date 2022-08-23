print(1, 2, 3, 4, sep = "<")
print ("What", "a", "beautiful", "day", ".", sep = "-", end = "! \ n")

error = 46372518
print ('Error number:% x'% error)

name = "Bob"
print("Hello, my name is {}". format (name))

title = "General"
name = "Kenobi"
print ("Hello there, {0} {1}". format (title, name))


def auto_detention(sentence, number_of_repetitions):
    for i in range(number_of_repetitions):
        current_sentence = sentence
        if i%4 == 0:
            current_sentence = current_sentence+'!'

        if i%3 == 0:
            current_sentence = current_sentence.upper()

        print(current_sentence)   

auto_detention ("Just don't tell lies", 5)