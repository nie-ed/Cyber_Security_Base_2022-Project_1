# Cyber Security Base – Project 1

In this project I used the OWASP Top ten 2021 list of Applicaion Security Risks, provided in thw webpage: https://owasp.org/www-project-top-ten/.
Also used the CSFR security risk, tho it is not specified in the OWASP Top ten 2021 list. The website is implemented using Pyhton and Django. The base was created using the instructions of the Django starter website: https://docs.djangoproject.com/en/3.1/intro/tutorial01/, however from there the website has been largely modified.

LINK: link to the repository



## FLAW 1 - Broken Access Control issue:

exact source link pinpointing flaw 1...

### Description:
Every users own website can be accessed by writing the correct url into the address bar. For example writing “http://localhost:8000/polls/3/”, while the local server is running, will take you to the users, whose id value is 3.

### How to fix:
Can be fixed by for example using Djangos ready made User objects, and checking that the logged in user is the one accessing the website. Checking who the current user is, can be done by using the request.user attribute, when using Djangos User objects as the method to make new users.

This method to fix the problem can be found as code in Fix can be found as code in 

Another way to fix this is when using the User object, one can use the @login_required decorator. This checks if the user is logged in and acts normally if they are, and if they are not logged in redirects the user to a predifined url (url defined in setting.py or in the @login_required() as a parameter). Another way, if not using Djangos User object, could be to add a logged_in value to users information in the database, so that if the user gives the correct username and password value, the logged_in value would turn True. Otherwise it would be False. Then letting the user access websited depending if the users logged_in value is True of False. This however could cause other issues, like what to do when another person is accessing the users website when the user them selves is accessing it and therefore the logged_in value is True.



## FLAW 2 - Cryptographic Failures issue:

exact source link pinpointing flaw 2…

### Description:
The users are created, saved and transmitted as clear text. There is no cryptographich methods in saving and transmitting for example the users password.

### How to fix:
Can be fixed for example by using Djangos User objects to create new users. Django stores users password only as a hash.

Fix can be found as code in  

Could also be attepted to create the Cryptographic protection manually by ones self, but this can be tricky and the ready made Djangos option might be the safer way to go.


## FLAW 3 - CSRF issue:

exact source link pinpointing flaw 5...

### Description:
When sending a POST request to the website, in the login page, there is no csrf protections placed. This means, in a malicious website, there can be a link that is intended to do something on my website, with logged in user that visit said malicious website.

### How to fix:
Can be fixed by setting csfr protection to places in the code, where a POST request is done. In this case, the login.html page, the views.py and adding csrf middleware to the settings.py. The csrf token to be placed in the html templates is a “{% csrf_token %}”. Also there is a need to import the csfr checking to the views.py file that handels the post request.
Fixes in code can be found in 


## FLAW 4 - Identification and Authentication Failures:

exact source link pinpointing flaw 5...

### Description:
The website allows weak, well-known passwords. There is no checking that the password chosen, when creating a new user, is safe. There is no checking that the password is atleast a specific length, that is has different types of letters and symbols or that it is not one off the most common password that people use, such as Password1. Currently in the application, one can create an empty password and username. 

### How to fix:
Can be fixed by for example utilizing Djangos pluggable password validation. This is done by adding to the setting.py file the validators wanted. When creating a new user, using User.objects.create_user() does not automatically validate the password provided to it. Because of this, you can validate the new created password by either creating your own password validators or integrating the Djangos password validation from setting.py. In this application, Djangos validators have been integrated to the code, and currently commented out, according to the example provided in “https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/password_validation/”.
One can also create there own validators, or add ones to the Djangos ready made validators.

These fixes to the validation problem can be found in the code from  


## FLAW 5 - Insecure Desing:

exact source link pinpointing flaw 5...

### Description:
No threat modeling used in the making of the application. This can lead to flaws in such things as the key flows and authentication of users of the application. Such ones as the one in the application, where it shows the texts of every user to every user. There is no checking whose texts are shown to whom. If the texts are meant to be private, this is a huge flaw in the design of the application.

### How to fix:
Can be fixed by checking that the logged in user is shown there own texts, and nobody elses. That can be implemented by filtering the shown texts not only by date but also by user.

These fixes to the validation problem can be found in the code from  
