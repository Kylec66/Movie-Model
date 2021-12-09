# Project-4:https://moviemodel.herokuapp.com/

![image](https://user-images.githubusercontent.com/83102597/145463544-72a5838a-6fb2-4bdc-ab9b-d787ceebc3d4.png)

Have you ever wanted to make a movie but weren't sure about how it would perform? We develeopled a machine learning model that would do just that based on a few different variables that can be adjusted or changed based on your movie preference. The model we created allows the user to pick between multiple Writers, Stars, Genres and budget amounts to determine the gross revenue of their movie. 

This was achieved using a Kaggle dataset of movies from the past forty years, which was originally extracted from the IMDB API. We took the original CSV and then cleaned it into two different versions, one for information charts to be made on Tableau, and the other to run a machine learning predictor based on specific columns. For the charts to be made through Tableau, we removed all movie rows that had blank columns, thus making the data streamlined with movies that had data in all columns. Although it deleted over two thousand titles, it still left over five thousand to work off of. As for the machine model, we removed almost half of the original set’s columns, and left off with the ones that would serve the best levels of accuracy in predicting outcomes from the user’s request. Lastly, we exported separate CSVs for both sets, and then connected them to a SQLite database for further use 
