# slack-compile

* This project is no longer being maintained, and is defunct as the hackerrank api has now been depricated. *

A Python project with Flask for a /compile &lt;lang>  &lt;snippet-url> command. Also my first slack integration


This was a one day personal hackathon-like project where I attempted to create a slack /command that would take in a public snippet and language, then return the code after it had been run. It uses hackerrank's JSON api and slack's JSON api to acomplish this.

# Dependencies

This project uses beautiful soup 4 for html parsing, requests and urlib.request for scraping of the public slack snippet page, flask for webserver services and json for json parsing.


# Usage

To use this project, install python3 and flask with nginx or apache serving the flask page, either via wscgi or a redirect. This is because slack requires a valid SSL certificate.


Under Slack's custom integrations, locate "slash commands", and enter in <yoururl>/in


# TODO

Things that I should do at some stage to complete the project, or that you can help me out with

 - Implement stdout errors
 - Implement proper test cases
 - Clean and modularise code

Host permanently and deploy to slack's app store
