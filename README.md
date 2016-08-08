# Home Intranet
A simple web app featuring a Food Planner written in Flask.

## Background
This project was a way for me to learn [Flask](http://flask.pocoo.org/). I am not a web front-end developer so the views are
adaptations of [Shay Howe's HTML and CSS tutorial](http://learn.shayhowe.com/) that I did to get familiar with HTML and CSS.

## What does it do?
The idea was to create an automatic shopping list generator based on our weekly food plan at home. The app is a web page only
available to people in your home internet network. You can put some general info there to share with the family.
The main feature is the Food Manger. You can add your favorite recipes to the database. Then you go make a weekly plan for
what you want to eat during the week. The app then generates a shopping list based on the recipes and their ingredients.
You can add or remove stuff from the shopping list.

## How to use it?
After getting the repo, and making sure you have installed the requirements, run:
```
python home_intranet.py
```
On the same device, you will be able to access the app by opennig the browser and heading to http://127.0.0.1:5000/.
The web server is accessible to any device on the same network, including other computers, tablets, and smartphones on:
```
http://<your.ip.adress>:5000/
```
where `<your.ip.adress>` is the IP adress of the device running the app. So it will be something like:
```
http://192.168.1.3:5000/
```
My solution was to run the app on a Raspberry Pi connected to our home's router. That was good enough for me :)


