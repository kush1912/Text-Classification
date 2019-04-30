# Text-Classification

This is one of the Projects which was done in interest to learn the difference between the different classification algorithm and derive a solid conclusion from that. It scrap sthe data from youtube and related to six different classes and then by using different classification algorithm it classifies them.

**Language :** Python <br>
**Tools & Technolgies :**  Spyder,  Jupyter Notebook, Chrome driver, google collab

**SCRAPING:** <br>
-Website Scraped :  Youtube</br>
-Libraries used : Beautiful Soup, Selenium, Requests  <br>
-Data Fields: Video ID, Title,  Description, Class <br>
-Dataset contains 500 entries per class on an average. <br>

![image](https://user-images.githubusercontent.com/36148381/56984817-8fa0cf00-6ba4-11e9-8ea8-4c19ff78471f.png)

Beautiful soup library of python was used to pull the information of html page from youtube. Youtube does not gives the full video length when you normally search a topic in its first page when you scroll down it shows the list of other videos. Hence it was a challenging to get the list of videos in that big amount.
 
To overcome this challenge [chromeweb driver](http://chromedriver.chromium.org/downloads) with selenium was used. A function was built in the scraping code which firstly loads the page by scrolling it 150 times after a period of one sec.  And then it receives the list of all the videos. You can get video ID, Title, from there but to get the full description you have to go to the link of that video and then scrap description from there. 
