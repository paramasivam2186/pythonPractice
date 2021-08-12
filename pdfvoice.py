import pyttsx3
import PyPDF2
file = open('C:\\Users\\Sivakumar\\Desktop\\siva.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(file)
num_pages = pdf_reader.numPages
play = pyttsx3.init()
print('Playing PDF File')
for num in range(0,num_pages):
	page = pdf_reader.getPage(num)
data= page.extractText()
play.say(data)
play.runAndWait()


# Required Libraries
# First, we need to install the necessary libraries. We require two libraries to build this.
# 1. PyPDF2
# A Pure-Python library built as a PDF toolkit. It is capable of extracting document information splitting documents page by page merging documents page by page cropping pages merging multiple pages into a single page encrypting and decrypting PDF files and more!
# So, open your terminal and run the following command.
# pip install PyPDF2
# 2. pyttsx3
# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3.
# So, open your terminal and run the following command.
# pip install pyttsx3
# Steps to be followed
# STEP 1
# As we have installed the packages, we can import them into our program.
# import pyttsx3
# import PyPDF2
# import win32api
# STEP 2
# Now, we need to open our file in reading format and store it in a book. The name of the pdf file is demo.pdf. rb stands for reading mode.
# file = open(‘demo.pdf’,’rb’)
# STEP 3
# Now, we will call PyPDF2’s PdfFileReader method on file and store it into pdf_reader
# pdf_reader = PyPDF2.PdfFileReader(book)
# STEP 4
# Now let’s calculate the number of pages in our pdf by using the numPages method on pdf_reader and store in num_pages.
# num_pages = pdf_reader.numPages
# STEP 5
# Now let’s initialize pyttsx3 using the init method and let’s print playing PDF File
# play = pyttsx3.init()
# print(‘Playing PDF File’)
# STEP 6
# Now, let’s run a loop for the number of pages in our pdf file. A page will get retrieved at each iteration.
# for num in range(0,num_pages):
# page = pdf_reader.getPage(num)
# data= page.extractText()
# play.say(data)
# play.runAndWait()
# Moving forward, let’s extract the text from our page using the extractText method on our page and store it into data.
# Next, we will call say method on data, and finally, we can call runAndWait method at the end.
Run the python script and your PDF File content will play.