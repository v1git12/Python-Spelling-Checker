from textblob import TextBlob
#incorrected Spelling
a =input("Enter any word of English: ")
print("Original Text: "+str(a))

b= TextBlob(a)

print("Corrected Text:" +str(b.correct()))

