=========
Domino App
=========

Domino Data Lab has the ability to host sharable web apps (e.g. Dash, Shiny, Flask); however, when iterating on those apps, you may want to open them directly in Jupyter. While note sharable, this is a nice way to debug and quickly iterate on your app before publishing in Domino later. 

https://docs.dominodatalab.com/en/4.1/reference/publish/apps/index.html

Usage
================

The process to publish an app is the same as you do regularly through Domino. In other words, you'll need to have an app.sh that starts your app on host 0.0.0.0 and port 8888 in addition to pointing ot you app files. 


