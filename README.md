# hello-world
The beginning of a coding adventure. It contains a journal of my progress. 
My name is Katpolice (Gilbert) and I'm offically starting my grind on becoming a developer today. 
I do have some past experience with programming like Scratch, Ev3 basic, RobotC and a bit of Python.
However, beyond that exposure and trial and error from years of experience with Robotics, I havn't formally taken any programming classes/courses. So as of today (July/2/19) I will begin my formal coding jounery with websites like Github, EdX, LeetCode, Khan Academy and Coursea. I have used resources like Lynda in the past. 
Thank you for listening to my Ted talk. 

--------------------------------------------------------------
June/04/20 - Today on Udemy, I created a phone and email scraper based on what you have on your clipboard. It'll be very handy whenever I need to mass copy and paste phone numbers or emails for whatever reason. I learned about filenames and absolute/relative file paths, reading and writing plaintext files and copying and moving files and folders. All within the python shell which was pretty neat. Normally, I would attempt a Leetcode problem but I have decided the jump was a bit too much for me as of right now so I decided to check a website called Interview Cake and a book called Cracking the Coding Interview. One day, I hope to sucessful obtain a junior dev or intern postition at a company or startup in the future. That's all for today, Katpolice (Gilbert) signing off. 

June/03/20 - Today on Udemy, I learned about Regex dot-star (.*), caret/dollar characters (^ and $), regex sub() method and verbose mode. 

I tried out the second challange of the June Leetcode Challenge and I finished it. Ther problem was "Two City Scheduling" so as always I started peudeo coding it. After many attempts, I gave up and searched up a couple of things that helped with my solution. That's all for today, Katpolice (Gilbert) signing off. 

June/02/20 - Today on Udemy, I learned about regex groups and the pipe character. It's very handy when your looking for specific values in a string. I looked into repetition in regex patterns and Greedy/Nongreedy matching which by default is greedy. Lastly, regex character classes and the findall() method taught me about handy shorthand classes like \d, \w, \s and to find the opposite have it in uppercase so \D. \W and \S.

I tried out the second challange of the June Leetcode Challenge and I completed it!!! The problem was "Delete Node in a Linked List" so I peudeocoded "Why don't I just skip the bad Node?" Well, I had the right idea but had troubles coding it. Eventually I ended up with the code below which got accepted. 

node.val = node.next.val

node.next = node.next.next

That's all for today, Katpolice (Gilbert) signing off.  

June/01/20 - Today I started with making my Raspberry Pi 1 B (which I got for free) functional. I found a brand new 16gb SanDisk Ultra SDHC card and formatted it with Raspberry Pi Imager and installed the newest verison of OS and copied a zip file of Minecraft Pi. Next, I found an old phone charger as the power source and a new HDMI cable. I inserted everything correctly and firmly into the Pi and plug it into a tv and a keyboard and mouse. My first problem was the charger was insuffient as it was a 5v 0.7amp compared to the 5v 1amp needed so I found a new charger. It worked! But everything is reallllly slow with 512mb of ram. Then, I decompressed the Minecraft Pi zip file and tried opening stackx and sadly it wouldn't work with a bunch of google searching and stackflow. Nonetheless, I have a (slow) computer now to do whatever and I'm planning to create a Minecraft Pi bot with python that automatically places blocks or builds structures. 

I decicded to try out the June Leetcode Challenge as my first ever experience on Leetcode. Yeah, that didn't go too well but I did learn alot. The problem was a Invert Binary Tree and sadly after an hour with Python and reviewing other sources I couldn't get it to work. :/ I kept getting "Line 17: SyntaxError: invalid syntax" which caused the rest of my program to not work. However, there were 500,898 accepted and 782,607 submissions so it was truly a learning experience being my first ever taste with a Invert Binary Tree.

On Udemy, I learned about launching python programs from outside IDLE with the window key + R. I started learning about the basics of regular expressions and I'm starting to get the hang of it. However, I keep getting the error "AttributeError: 'NoneType' object has no attribute 'groups'" which I'm currently looking into. 

That's all for today, Katpolice (Gilbert) signing off. 

May/31/20 - Today I learned about more about strings in particular about advanced string syntax, string methods and string formatting. Such as...

\n for creating more readable code with the print() function

variable.upper() to change the variable is in all caps

variable.lower() to change the variable is in all lowercase

variable.iupper() to check if the variable is in uppercase

variable.islower() to check if the variable is in lowercase

and others like .alpha(), .alnum(), .isdecimal(), isspace() & .istitle() which check if it contained said object in a string. 

Eg. 'hellomyfriend291'.isalpha() would display False because the string contains both letters and numbers while it's only checking for letters NOT numbers.
But it would display True for 'hellomyfriend291'.isalnum()

.startwith() & .endwith() will check if the string starts or ends with the argument. 

We can also use 'string'.join(['other strings']) to insert the value of the string into other strings.

Eg. ' '.join(['cats', 'rats', 'bats'])
Displays  'cats rats bats'

You can use the split() function to split a string into a bunch of smaller strings.
Eg. 'my name is Simpleton'.split()
Displays  ['my', 'name', 'is', 'Simpleton']

.rjust(), .ljust() & .center() places the agrument on the left, right or around the string alongside the quality. 
Eg. 'Hello'.center(20, 'T')
Displays  'TPHelloT'

Lastly, .strip(), .lstrip() & .rstrip() will remove the agrument from the string depending on how and which one you use. 
Eg. 'SpamSpamSpamBaconEggSpam'.strip('ampS')
Displays  'BaconEgg'

That's all for today, Katpolice (Gilbert) signing off. 
May/28/20 - Today I learned about try and except statements, creating a "Guess the Number" program, Lists and using loops with lists, multiple assignments and augmented operators. I'm also 25% completed of the course on Udemy so thats neat. That's all for today, Katpolice (Gilbert) signing off. 

May/30/20 - Today I learned about Dictionaries, data types and data strutures. I have also created a program that displays the number of each characters of what you paste. Likewise, it displays it with pprint.pprint (pretty print) as in a horziontal and more readable format rather than one really long string. That's all for today, Katpolice (Gilbert) signing off. 

May/29/20 - Today I learned about list methods and similarities between lists and stirngs. My favorites being variable.sort(key-str.lower), the ASCIIbetical order and variable.deepcopy() That's all for today, Katpolice (Gilbert) signing off. 

May/22-28/20 - I have decided to mess around with Minecraft's Nether Update beta on bedrock and I found some interesting bugs being a floating and sinking wither.

Floating wither (https://youtu.be/OPqhnoF-nJk) - I spawned 5 withers at the same time and one acted normally while the other 4 just floated upwards endlessly. I suspect that it has something to do with the spawn damage created when a (or 5) withers are spawned. 

Sinking wither (https://youtu.be/lqHZ9PnIfJc\) - I spawned a wither in the end and I was stuck with it in the end platform being underground end stone. So, I tapped the wither forcing it to show a explosion until it broke free at the edge of the island. It moved around for a bit before sinking to the void and later dying. I think it has something to do with the wither not having something to attack in sight causing it to gitch and sink. That's all for today, Katpolice (Gilbert) signing off. 

April/5/20 - Today I learned about how to use and create functions in a global and local environment. Likewise, with handling errors with try/except statements. That's all for today, Katpolice (Gilbert) signing off. 

April/3/20 - Well alot of things happened since my last update. A three week long summer vacation, summer job making bubble tea, qualifying for vex provinicals and senior year of high school. Also, a few bad things like a concussion, COVID-19 and school being closed indefinite. Regardless, I'm going to champion the way and get back to my coding adventures. OHhyeah, I got a free 12 year old laptop so that's neat. Sadly, I can't install Microsoft Visual Studio on it but Notepad++ will do. My resource of choose right now is University of Watrloo OpenCS because honestly I need a structured to help me get back into the groove. That's all for today, Katpolice (Gilbert) signing off. 

July/11-16/19 - Well these sores translated into infections and let's just say that wasn't fun at all. Anyways, I'm currently getting better to the point where I can actually sit for once. Currently on Khan Academy, I somewhat managed a computer science video everyday. Currently for edx and Lynda, I wasn't able to watch and learn, let alone program for the duration of time sadly. In other news, Ikea is closing down it's only US production site and moving it to Europe. That's all for today, Katpolice (Gilbert) signing off. 

July/10/19 - I got some sores which are mainly from not taking enough breaks inbetween coding, I'll keep that in mind for the future. Currently in Lynda, I learned about modular code. Topics like why you should be breaking your code apart, how to create and call functions, setting parameters and agruments, understanding variable scope and splitiing ocde into different files. Currently on Khan Academy, I learned more about computer science and digged even deeper in algorithms. Currently on edx, I learned about how to create and use dictionaries in python. In other news, the classic political blame game is happening in regards to the layoffs with Bombardier. I don't like the outcome of this. That's all for today, Katpolice (Gilbert) signing off. 

July/6-9/19 - I did manage to do a little bit of programming on each of the day, but I didn't do enough to prompt a daily add-on for each date due to other commitments. Also, I switched from Atom to Visual Studio Code because it's "meta". Currently on Lynda, I learned about variables and data types. I got an introduciton to variables and data types, how to use duck-typed languages, the ins and outs with numbers, characters and strings, working with operators, properly using white space and adding comments to code for human understanding. Likewise, I learned about writing conditional code. In terms of using if statements, complex conditions, comparison operator and switch statements. Currently on Khan Academy, I learned more about computer science and algorithms. Currently on edx, I did some lab questions about sets. In other news, Bombardier are cutting half of there staff (550 of 1100) at their Thunder Bay, Ontario, Canada plant. Which is kind of odd because they still own the TTC well overdued streetcars. That's all for today, Katpolice (Gilbert) signing off. 

July/5/19 - Today I found out that you can create your own website on Github. I sucessfully created a website and I'm planning to transfer my journal entries as blog posts on my website in the near future. In the mean time, I also played around with Wix and Wordpress and found out that GitHub and WordPress would be my go to. I actually found out about the whole concept of hosting from Github from the learning labs. I downloaded atom-beautify and oh boy my code does look colorful and codelike. So, I started to do some html and I honestly forgot what did what. I did learn a little bit of html before forgetting about it. So, I tried a format that I got from the web and I didn't like it. So, i chose to write my own code from scratch. I learned about subpages thank to StackOverflow and boy the amount of help/coding advice on that site is on par with Github. (And Google) Currently on Lynda, I learned about why JavaScript is so important, how to create your first program in JavaScript and requesting inputs. Currently on Khan Academy, I learned about how it's possible to generate "English looking" text using Markov chains. In other words, English is filled with randoness and statistics. Also, this Markov theory can be used to explain "communication." Currently on EdX, I learned about sets and how you can visually represent them with a Venn diagram. In other news, Appearly Nathan Phillips Square can fit about 100,000 people during the Raptor's parade. Also, a one stop subway extentison cost 4 billions for poltical and zoning reasons. So, that's interesting and the back and forth debate about the general area Scarborough about a "subway extension" for at least 30+ years? Honestly, that's an oof. That's all for today, Katpolice (Gilbert) signing off. 

July/4/19 - 
Well it's offical. I broke the Community starter kit by the looks of it, I could restart the whole process which I'm considering. However it seems like I was a little bit ambiguous so I started working on "Reviewing pull requests" by The GitHub Training Team. I completed all 8 steps and I learned about pull requests and all of the possibilities and neat features about them. The biggest takeaway would be effective communicating about a change. For example, "This looks like it’ll be helpful to our users, but I’m not sure about the flow. I also have some concerns about the efficiency of these queries." or "Although this feature might be useful, do we have any data that identifies that our users need it?" both are which were directly taken from the "Reviewing pull requests" program. Although, I had a minor problem when I accidently progressed a few steps ahead. But, I managed to fix that by going back and working on those prior steps. It gave a bigger insight on what could have went wrong with my Community starter kit. It's possible that I committted the pull request with the master so that I was unable to work on any of the steps in between #2 and the final product. I will look into this further tomorrow. I downloaded Atom eariler today so I could start typing out and messing around with code. Appearly, there's a fit with the "best text editor" and I think it ultimately depends on your own preferneces. Currently on EdX, I decided to resume my progress on Python Basics for Data Science by IBM. I honestly forgot about it, until today. Currently on Khan Academy, I started watching 1 Organic Chemistry video a day starting from about 2 weeks ago. But recently I got interested in the Computer Science section instead. Currently on Lynda, I finished my first chapter and it was on "Programming Basics". I eager to learn about the next chapter which is about "Core Programming Syntax". In other news, there was a 6.4 magnitude earthquake west of Las Vegas and north of Los Angeles. I hope that everyone that was affected is safe. That's all for today, Katpolice (Gilbert) signing off. 

July/3/19 - 
I started working on the Community starter kit which is offered by The GitHub Training Team. I completed the first course step "Add a repository description". However, it seems like I messed up with the "EDIT the README" section and I'm trying to troubleshoot it. By the looks of it, it seems like I accidently messed up one of the steps and which off track. Resulting in a unfixable loop that I can't seem to fix and/or undo. Therefore it seems like I have to restart the whole Community starter kit. Currently on Lynda, I'm watching a playlist called "Programming Foundations: Fundamentals" inorder to get a strong foundation in programming. So far I learned about "machine languages" and appearly C+ is closer to it then somelike like Python. 
In other news, Whatsapp, Facebook, Instagram are having troubles with sending photos to other users on there platform. All 3 companies are owned by Facebook. Likewise, Twitter is having troubles with there private message system. I suspect a DDoS by some company or organization because it's literally the day before July 4th. Or it could be some shady plot to extract specific images and/or private messages from certain individuals/groups. Honestly, who knows at this point until there's a formal news conference. 
That's all for today, Katpolice (Gilbert) signing off. 
