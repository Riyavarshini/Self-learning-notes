<h1> 📚 ELEMENTS OF SUPERVISED LEARNING 📚 </h1>

Supervised machine learning is based on the following core concepts:

* Data
* Model
* Training
* Evaluating
* Inference

<h2> Data </h2>
Data is the driving force of ML. Data comes in the form of words and numbers stored in tables, or as the values of pixels and waveforms captured in images and audio files. We store related data in datasets. For example, we might have a dataset of the following:

* Images of cats
* Housing prices
* Weather information

Datasets are made up of individual examples that contain features and a label.
You could think of an example as analogous to a single row in a spreadsheet. Features are the values that a supervised model uses to predict the label. The label is the "answer," or the value we want the model to predict. In a weather model that predicts rainfall, the features could be latitude, longitude, temperature, humidity, cloud coverage, wind direction, and atmospheric pressure. The label would be rainfall amount.
Examples that contain both features and a label are called labeled examples.

<h3> Dataset characteristics</h3>
A dataset is characterized by its size and diversity. Size indicates the number of examples. Diversity indicates the range those examples cover. Good datasets are both large and highly diverse.


☠️ For instance, a dataset might contain 100 years worth of data, but only for the month of July. Using this dataset to predict rainfall in January would produce poor predictions. Conversely, a dataset might cover only a few years but contain every month. This dataset might produce poor predictions because it doesn't contain enough years to account for variability. ☠️

Thus,
A large number of examples that cover a variety of use cases is essential for a machine learning system to understand the underlying patterns in the data. A model trained on this type of dataset is more likely to make good predictions on new data.

A dataset can also be characterized by the number of its features. For example, some weather datasets might contain hundreds of features, ranging from satellite imagery to cloud coverage values. Other datasets might contain only three or four features, like humidity, atmospheric pressure, and temperature. Datasets with more features can help a model discover additional patterns and make better predictions.

<h2> MODEL </h2>

In supervised learning, a model is the complex collection of numbers that define the mathematical relationship from specific input feature patterns to specific output label values. The model discovers these patterns through training.

<h2> Training </h2>

Before a supervised model can make predictions, it must be trained. To train a model, we give the model a dataset with labeled examples. The model's goal is to work out the best solution for predicting the labels from the features. The model finds the best solution by comparing its predicted value to the label's actual value.
Based on the difference between the predicted and actual values—defined as the loss—the model gradually updates its solution. In other words, the model learns the mathematical relationship between the features and the label so that it can make the best predictions on unseen data.

During training, ML practitioners can make subtle adjustments to the configurations and features the model uses to make predictions. For example, certain features have more predictive power than others. Therefore, ML practitioners can select which features the model uses during training. For example, suppose a weather dataset containstime_of_day as a feature. In this case, an ML practitioner can add or remove time_of_day during training to see whether the model makes better predictions with or without it.

<h2> Evaluating </h2>

We evaluate a trained model to determine how well it learned. When we evaluate a model, we use a labeled dataset, but we only give the model the dataset's features. We then compare the model's predictions to the label's true values.
Depending on the model's predictions, we might do more training and evaluating before deploying the model in a real-world application.

<h2> Inference </h2>

Once we're satisfied with the results from evaluating the model, we can use the model to make predictions, called inferences, on unlabeled examples. In the weather app example, we would give the model the current weather conditions—like temperature, atmospheric pressure, and relative humidity—and it would predict the amount of rainfall.

<h2> Predictive power </h2>
Supervised ML models are trained using datasets with labeled examples. The model learns how to predict the label from the features. However, not every feature in a dataset has predictive power. In some instances, only a few features act as predictors of the label. In the dataset below, use price as the label and the remaining columns as the features.

---
<H1> 🌟 NOTES 🌟 </H1>

1. **example** : 
  The values of one row of features and possibly a label. Examples in supervised learning fall into two general categories:
    * `A labeled example` consists of one or more features and a label. Labeled examples are used during training.
    * `An unlabeled example` consists of one or more features but no label. Unlabeled examples are used during inference.

2. **Features** :
  An input variable to a machine learning model.

3. **Label** :
   In supervised machine learning, the "answer" or "result" portion of an example.

   <img width="885" alt="Example, feature, label illustration" src="https://github.com/Riyavarshini/Self-learning-notes/assets/117080445/d442fc31-f1e0-442e-bedb-bcddecc818de">

4. **loss** :
  During the training of a supervised model, a measure of how far a model's prediction is from its label.
  A loss function calculates the loss.


---
<H1> 🟢 UNDERSTANDINGS 🟢 </H1>

1. <img width="829" alt="Screenshot 2024-01-31 at 8 38 17 PM" src="https://github.com/Riyavarshini/Self-learning-notes/assets/117080445/4761e8d4-aca7-45f2-80b1-edde93ac9bd3">

   Which three features do you think are likely the greatest predictors for a car's price?
    - A car's make/model, year, and miles are likely to be among the strongest predictors for its price.

2. If you wanted to understand the types of users that visit the site, would you use supervised or unsupervised learning?
    - Because we want the model to cluster groups of related customers, we'd use unsupervised learning. After the model clustered the users, we'd create our own names for each cluster, for example, "discount seekers," "deal hunters," "surfers," "loyal," and "wanderers."
  
3. What type of ML would you use to predict the kilowatt hours used per year for a newly constructed house?
    - Supervised learning trains on labeled examples. In this dataset "kilowatt hours used per year” would be the label because this is the value you want the model to predict. The features would be "square footage,” "location,” and "year built.”

4. If you wanted to predict the cost of a coach ticket, would you use regression or classification?
    - A regression model's output is a numeric value.
  
5. Based on the dataset, could you train a classification model to classify the cost of a coach ticket as "high," "average," or "low"?
    - It's possible to create a classification model from the dataset. You would do something like the following:
        - Find the average cost of a ticket from the departure airport to the destination airport.
        - Determine the thresholds that would constitute "high," "average," and "low".
        - Compare the predicted cost to the thresholds and output the category the value falls within.

6. If the model's predictions are far off, what might you do to make them better?
    - Retraining the model with fewer features, but that have more predictive power, can produce a model that makes better predictions.
    - Models trained on datasets with more examples and a wider range of values can produce better predictions because the model has a better generalized solution for the relationship between the features and the label.

---

