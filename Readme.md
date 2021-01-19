# MoodifyPlayer
Hack the North 2020++ project. A cool app that converts a song to images that match the mood of the song and its lyrics. Built with JavaScript and Flask.

# What it does
Moodify start by connecting the user to their Spotify account and allow them to request a song. 
The song is then passed to a Tensorflow machine learning model that will predict the mood of the piece between Happy, Sad, and Energetic. 
Then, we also utilize the lyricsgenius python library to pull the lyrics of the song that we process, before sending them off to 
IBM Cloud's Natural Language Understanding service that returns the keywords of the song. Using the mood and the keywords, 
we construct a few search terms that we send to the Bing Image Search API which in turn gives back URLs to relevant pictures.
Finally, we serve the audio of the song as well as the images simultaneously on the front-end for the user to enjoy.

Example: The song Welcome to New York by Taylor Swift has a mood of "Happy", and one of the keywords from its lyrics is "New York". Hence we get images of "Happy New York City" 
<br>
![Welcome_to_New_York](/Demo/Welcome_to_New_York.png)

# How we built it
The backend we used is Flask and we used the Tensorflow library to load the model. We also connected our application to a variety of APIs 
such as the Spotify API, Bing Image Search API, Genius API (through lyricsgenius), and IBM NLU API. Furthermore we used SQLite3 to store 
our user data and SocketIO to continuously serve images from the backend to the front-end.
