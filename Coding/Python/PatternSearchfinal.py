import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

regex='[^a-zA-Z0\d]' #placing a-z A-Z or 0-9 inside brackets signals to search for a sequence or range within the given parameters.
#^^ This creates a variable that assigns all of the occurrences of any characters other than the lower and uppercase
#alphabet and 0-9 or non-alpha numeric characters. 
#placing any string, string, variable, boolean, or integer inside “”,’’ makes it a literal sequence but using \d would be a #literal character and is very useful in condensing the code because it stands for more 
#in python the use of regex allows us to implement wild cards or special characters
#For example I could replace any single character of a word with ?. example col?r would return color
#the special character \d replaces the need to write out 0-9. it means the same thing. 
result= re.findall(regex, lorem_ipsum)
#This assigns a variable to the outcome of applying to regex to lorem_ipsum.
#This will findall of the occurences of non alphabet or integers in lorem_ipsum

print(len(result))#using len(result) will allow us to print how many times there 
#are non alpha numeric expressions in lorem_ipsum

regex="sit[-:]amet" 
#^^Here we are creating a variable that includes all the occurrences of sit dash or colon followed by amet.

occurrence_sit_amet= re.findall(regex,lorem_ipsum)
#here we assign the outcome of the variable the to the name occurrence_sit_amet. 
#we are using find all to search for this two word sequence in lorem_ipsum.

print(len(occurrence_sit_amet))# here we are printing out the number of occurances 
#of the above outcome by using the len() function

regularexpression='sit[:-]amet'
#here we are using the same variable expression as the previous regex.
#Here we are creating a variable that includes all the occurrences of sit dash or colon followed by amet.

replace_results=re.sub(regex,'sit amet',lorem_ipsum)# This outcome will replace all the occurrences
#of the regex 'sit[:-]amet' with 'sit amet' in lorem_ipsum.
#re.sub() completes this replacement for us

occurrence_sit_amet=re.findall(regex, lorem_ipsum)# here we are simply searching for all the occurrences
# of the 'sit amet' after subbing this with the findall() function

print(len(occurrence_sit_amet))
#here we will print the number of occurrences from the outcome of occurrcnce_sit_amet