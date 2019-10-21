This is the 3rd Milestone Project for Code Institute - A database web application for Fishing Enthusiasts (Anglers).


# Rivers of County Kerry

This is a simple database web application, where users can visit and gather information on a particular river. River information can be added by users so that other users and be informed. The idea of this is that as the database grows, from users adding more and more info, it becomes a rich place for anglers to go and learn about particular rivers in Kerry.

## UX

This web application has been designed for local and visiting Fishing Enthusiasts (Anglers). The User should find this application educational, informative and easy to use. It has been designed with responsiveness in mind, as this application may be visited on a mobile device by a user who is "on the go". A user of this application who is already fully informed about the subject matter, can easily input additional information, thereby populating the existing database and making it more informative, rich and concise. The reviews option allows users to express their views on particular rivers, (rivers which must be referenced in the river database first), and providing additional information and knowledge on a particular river, that, perhaps, the database may not provide.

### User Stories:
As a new User to the web application, I want to:
* be able to understand how to navigate around the web application.
* be able to find information about a particular river in County Kerry.
* to be able to update a particular river's information if I believe it to be inaccurate, incorrect or outdated.
* leave a review about a particular river, which is both informative and allows me to broadcast my own opinion.

### Wireframes: 
* The Wireframes plan can be found in the Wireframes Folder in my github repository:
[My Wireframe](https://github.com/haydal810/Milestone-Project-3/blob/master/wireframes/Wireframes%20v1.0.jpg)


## Features

### Layout
This is a multi-page layout, but designed with simplicity in mind. The home page displays the main river database information, below the header text which allows the user to find information very quickly without the need to have to search for it.

### Buttons
Buttons on this application are of Bootstrap 4. Big, bright and easy to use. 

### Font
Two fonts used are a google fonts, called "Mansalvua" and "Amatic SC". They are visually appealing fonts, easy to read and give a nice indication that the application is based on local knowledge. Jumboton was also used from Bootstrap, and appears on the home page and the about page, and come with it's own fonts. 

### Existing Features
* Navigation Bar - This is on the top of all the pages on the site. The left hand side has the title of the page being "Rivers of County Kerry", and when clicked, will return the user to the home page. The rest of the navigation items are aligned on the right hand side of the Nav bar.   They are: "About us", "Add a new River", "Review a new river" and "Read Reviews". 

* Edit a river record - The Blue River Name Button (in the data table on home page). This button is in the first column of every river row in the database table in the home page. As the welcome text advises, when the user clicks on this particular button, the user is redirected to a pre-populated form, visually showing the user the already saved doucment details (the key:value pairs) of that particular river. The user is then able to alter any, all or none of the fields as the user see's fit, and can submit the form to the server, updating the document on the database. There is also an option at the bottom of the form for the user to delete the document entirely. This is in the form of a red delete button. After submit or delete, the user is redirected back to the home page, where they can visually the evidence of what they have added / deleted, appear/not appear on the river table.

* Add new river - The user is redirected to a seperate page, where they can populate a form and submit their info to the database. After submit, the user is redirected back to the home page, where they can visually the evidence of what they have added, appear on the river table.

* Review a river - The user is redirected to a seperate page, where they can populate a form and submit their review on a particular river to the database. The form has been setup in such a way, that the reviewer can only submit a review on a river that is in the river database. This ensures that relevant reviews are only left. The review is displayed on the Read reviews page and the review itself is saved in a seperate collection in the database. The river database (river_names) and the review database (river_reviews) share a foreign key: river_name.


### Features Left to Implement
* Authentication would be a nice feature to implement, as it would ensure data that is added is more authentic and less inclined to be spam.
* Add additional fields to the river_names database, such a location, additonal info regarding purchase of permits, and links to accomidations / fishing tackle shops, etc.
* A "fish caught" record, to display anglers achievements on particular rivers.
* A graphical representation of the most popular rivers, as voted by visitors to the application.
* A .sort() applied to the route functions in app.py, so that displayed results show the most recently added at the top of the table (rivers & reviews)

## Main Technologies Used

* This project uses Python, HTML, CSS and Javascript programming languages. -

### Tools used

* Visual Studio Code by Microsoft - This was used as the IDE for building the application. This was my first time using a local IDE. 
* GitHub to store the project code remotely.
* PIP for installation of tools needed in this project.
* Git to handle version control.

### Other technologies / libraries used:
* Jinja to simplify displaying data from the backend of this project smoothly and effectively in html.
* PyMongo - A Python distribution containing tools for working with MongoDB.
* Bootstrap 4.3.1 - The project uses Bootstrap 4 to simplify the structure of the website and make the website responsive easily. https://getbootstrap.com/
* Fontawesome - Used to provide icons from FontAwesome throughtout the site. https://fontawesome.com/
* Google Fonts - The project uses Google fonts to style the website fonts. https://fonts.google.com/
* AutoPrefixer - This project used AutoPrefixer to make sure the css code is valid for all browsers. https://autoprefixer.github.io/


## Testing

### User Testing

#### Manual User testing:
This was the primary method of testing the application. People were asked to visit the website on a variety of devices, and to enter information to the database. This feedback was very uselful to determine any bugs that may have been present. I also tested the app manually myself on a varietly of browsers. 


### Below are the list of Internet Browsers I used to test the display of the website:

1. Google Chrome (Version 77.0)
    * Chrome Lighthouse was used to audit the website.
2. Mozilla Firefox (Version 69.0)
3. Microsoft Edge (Version 44.1)
4. Internet Explorer 11 (Version 11.8)

Manual testing was carried out using the above browsers. No bugs or desplay issues could be identified. 

### Below are the list of websites I used to test the HTML, CSS and JS code:

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.
3. [CSS Lint](http://csslint.net/) CSS Lint is an open source CSS code quality tool I used.

#### Meeting the needs of the user stories (as described in the UX section of this README file)

#### As a new User to the web application, I want to be able to understand how to navigate around the web application.

Upon landing on the home page, the user is greeted with a jumbotron welcome text, imediately followed below by the subject of the application: The Data Table. The user doesn't have to go searching for it, as it's right there. Navigation comes from the Navigation Bar at the top of the page. The Logo, when clicked, will redirect the user back to the home page. The rest of the Nav Bar items are positioned on the right hand side. They visually tell the user exactly what they can do. Each item, when clicked, redirects the user to a seperate page where the desired action can occur.

#### As a new User to the web application, I want to be able to add additional information to the river database...

Under "Add a new River" on the Nav Bar, the user will be redirected to a new page where the user can add a new document to the collection in the database.


#### As a new User to the web application, I want to be able to update a particular river's information if I believe it to be inaccurate, incorrect or outdated.

On the data-table displayed on the home page, there is a blue button in the first row. As explained on the welcome message on the top of the home page, when this button is clicked for that particular river, the user is redirected to a new page, where a pre-polulated form is, and the user can edit and make changes to this river record. At this point, there is also an option to delete the document entirely from the collection, in the form of a red button at the bottom of the form.

#### As a new User to the web application, I want to leave a review about a particular river, which is both informative and allows me to broadcast my own opinion.

"Review a River" is an item on the Nav Bar. Once clicked, the user is brought to a new page, where, via a form, they can leave a review about a particular river in the database. Once the review is submitted, the user can view what they have posted to the database on the "Read Reviews" page. Other users can also view this page, providing insight and knowledge from other users.


## Deployment

### Local Deployment

This project was developed using the Visual Studio Code IDE, committed to git and pushed to GitHub using the built in function within Visual Studio Code.


The GitHub Repository is here: https://github.com/haydal810/Milestone-Project-3
The application is live here: https://kerry-rivers-ms3.herokuapp.com/

To deploy this project on your own IDE, folow the steps below:

 Firstly, ensure of the following:
    - You have an IDE, such as VS Code
    - The following must be installed locally on your computer:
            - git
            - PIP
            - Python 3
            - Flask
            - A MongoDB Atlas account

Instructions for Installation:

1.  Make your own folder and navigate to it on the terminal. Then enter the following in the terminal:

```
$ git clone https://github.com/haydal810/Milestone-Project-3.git
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
2.  To run the app locally:

```
$ python -m flask run
```

### Heroku Deployment

The code was also pushed from git to heroku for live deployment: https://www.heroku.com/ 

To Deploy using Heroku Git, use git in the command line:

1.  Install the Heroku CLI. If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

2.  Clone the repository. Use Git to clone the projects source code to your local machine.

```
$ heroku git:clone -a kerry-rivers-ms3
$ cd kerry-rivers-ms3
```
3.  create your requirements.txt file

```
$ pip freeze --local > requirements.txt

```
4.  create your procfile file

```
$ echo web: python app.py > Procfile

```

5.  Deploy your changes. Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "commit message"
$ git push heroku master
```
6.  In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7.  Set the following config vars:

```
IP : 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
```
To get your MONGO_URI read the MongoDB Atlas documentation: [HERE](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click on the button "Open App".

The app should open in a new tab.

## Credits

### Content
All text in this project was written by the developer.

### Media
- The background image was sourced from https://www.pexels.com/

### Acknowledgements

- I'd like to thank my mentor, [Antonija Šimić](https://github.com/tonkec), for her useful and constructive feedback throughout the Milestone Project


### The content of this website is for educational purposes only. 
### Thank you.