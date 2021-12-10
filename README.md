# CS181 Final Project Proposal

Wilson Le & Phong Hoang

For the final project, we will be doing a movie recommendation system. User will be able to input their favorite movies (or previously watched movies) and our application will be able to produce a list of recommend movie for them.

The main question we want to answer is that what is the main factor that goes into a movie recommendation algorithm. We assume that the algorithm is a form of machine learning algorithm, so finding out the main factor (i.e genre, actors, director, etc.) trying different factor and see which one has the best recommendation.

Our dataset will be obtained by repeated hitting an API: http://omdbapi.com. This API will return data of the queried movie in JSON format. This API also requires an API key, which we have obtained. We will then proceed with writing a script that repeated hit this API with different queries for different movies. After each iteration, from the JSON formatted data the API response, we will parse it into a huge JSON file where the movie name will map to its respective data.

