import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

##This excerise used the findall funcation to output the number of non-alphanumeric charaters. This is an example of
#sequences and ranges because the code is looking in the lorem_ipsum range, to find the sequence of code I called out.
#The code that was called out is "[ -:.,]"

pattern = "[ -:.,]"
results = re.findall(pattern, lorem_ipsum)
print(len(results))

#This code I used the findall funcation again to find all occurances of sit amet meeting the directions. 
#The line pattern = 'sit[-:]amet' is an example of literal characters. 

pattern = 'sit[-:]amet'
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

#This code is used to find occurrances of the condidiotnd and then subsitute the conditions with what the system is wanting
#to have replaced. This is an example of finding speical charaters within the code, but is also an exmple of using the sub 
#funcation too.

pattern = 'sit[-:]amet'
replace_results = 'sit amet'
new_string = re.sub(pattern, replace_results, lorem_ipsum)

pattern = 'sit[-:]amet'
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

