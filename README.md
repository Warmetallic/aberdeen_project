# Alpha-2021

The project link: http://51.250.35.2:8000/

## Team members:

**_Qi Liu_**

**_Haixun Xin_**

**_Gleb Kharlamov_**

**_Yanghaochen Xu_**

**_Christopher McKeagney_**

# The Greig-Duncan Folk Song Collection

The main purpose of this web application is to store and display The Greig-Duncan Folk Song Collection. All data was provided by Dr. McKean in 8 volumes with hundreds of musical notations. The link to the data: https://www.dropbox.com/sh/k4qcsdi19vu8thl/AACJB0q9AKmo6k-rYiYGDevwa?dl=0 

Since the dataset is huge and requires a storage of several terabytes, only a few songs from the volumes are presented on the website, which is enough to demonstrate the functionality and all features of the project.

The website is deployed on Heroku and should be accessed through this web hosting service. If needed, the project can be launched locally. To do so, prepare own virtual environment and install everything from the requirements.txt file. The app was developed and tested on Windows machines in Sublime Text and Codio.


# The core features

The tools to add new songs with static files (images) and to edit already existings ones. Any song can have a detailed description and multiple images, whose images display music notations.

In order to use these tools, a user needs to login as an admin and with the Django admin form add a new song. The Django dashboard can be accessed through the navigation bar by clicking on the Admin link or through the direct link http://51.250.35.2:8000/admin

A new song will be added to the main page and displayed in a catalog with other songs. It is possible to click on the song and see all information about it. Images are placed in a carousel from Bootstrap and can be switched by sliders.

The site has a multi-search function with different filters. All filters can be applied to search separately or all together to create a more precise query. The search field is placed on the right side of the navigation bar.



# The app development

*Paired and mob programming*

The project was developed by a group of five students. Teams of two and three students were working on different activities based on Sprint tasks. On a weekly basis we had mob programming sessions to solve any problems and explain new solutions/decisions to each other.


*Testing*

Unit testing was used to test all functions and the functionality


*Git*  

The version control system was used to create this project. It allowed our team to collaborate and use back-ups if required. Every team member was working on their branch and after a review meeting we merged all the work. The gitlog.txt is providing all history of the development.


*Yandex Cloud* 

The project is deployed on Yandex Cloud


*Data and storage*

The provided data is in TIFF format and every single file is around 70 Mbs, which is too heavy to store and to upload/display on the website. We reformatted files to the PNG format and dramatically decreased the size of images. This way it is more efficient to work with the files. To store all our static files, we used an Amazon S3 bucket, since Heroku cannot keep large files.


*Security*

All security keys for Django and Amazon S3 Bucket are placed in the .env file. This file is added to .gitignore, so no one can obtain the data. For a new team of developers it is a need to create own env file with new keys by using Decouple(python library).

# User creation

First of all, it is required to create an admin user to access the Django dashboard. In order to do so, type |py manage.py createsuperuser|. Enter details (username, password and email). After that, it is possible to login into the dashboard and use the admin tools (create/edit/delete songs,images and users). In the dashboard Admin can create new users by click “ADD” button under the “AUTHENTICATION AND AUTHORIZATION’’. This will work only in the local environment. If needed to create Admin for Heroku, use this command instead |heroku run --app stark-mesa-89039 python manage.py makemigrations|.

![Снимок экрана (872)](https://user-images.githubusercontent.com/35700332/128427702-a70193b4-4b70-493a-bb1a-c45daebadcaa.png)


# Song creation

New songs can be added or edited only by the admin user through the dashboard. In the dashboard click on Songs and choose ADD. Fill all fields and press SAVE.
After that, the song will be displayed on the website.

![Снимок экрана (875)](https://user-images.githubusercontent.com/35700332/128428425-1f9a37f2-5c28-4b64-8c37-f7f0183ad7ea.png)


# Additional programs

To prepare data from songs' files we are using Tesseract. This library converts images to text and stores all data into the separate file. After that, it is easy to store text data into the Django admin form. 

Tesseract instructions:

- Prepare tiff files from Dropbox

- Make a screenshot of every tiff file (this way an image will be in a png format, which is much lighter than tiff)

- Crop new images

- Store images into a separate folder

- Open the program (Alpha-2021\folksongs\management\commands\songtxt.py)

- Set a path to the folder with images

- Run the program (py songtext.py)


# Commands for the local development: 

- git clone https://github.com/UoA-CS5942/Alpha-2021.git

- cd Alpha-2021

- python/pip -V (checks a version)

- pip install virtualenv (install the virtual environment)

- virtualenv . (download everything here)

- . ./Scripts/activate (to turn off - deactivate)

- pip install django (install everything from the requirements list provided below)

- py manage.py createsuperuser (create the admin user)

- py manage.py makemigrations (packaging models into a database)

- py manage.py migrate (apply all migrations)

- py manage.py runserver (runs the project)


