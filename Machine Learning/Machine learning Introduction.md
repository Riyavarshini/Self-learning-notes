<h1> 🌟 Introducation to Machine learning 🌟 </h1>

**Machine learning** (ML) powers some of the most important technologies we use, from translation apps to autonomous vehicles. This course explains the core concepts behind ML.
In basic terms, ML is the process of training a piece of software, called a model, to make useful predictions or generate content from data.
Using an ML approach, we would give an ML model enormous amounts of weather data until the ML model eventually learned the mathematical relationship between weather patterns that produce differing amounts of rain.
We would then give the model the current weather data, and it would predict the amount of rain.

## Types of ML Systems
ML systems fall into one or more of the following categories based on how they learn to make predictions or generate content:

* Supervised learning
* Unsupervised learning
* Reinforcement learning
* Generative AI

### 🌟 SUPERVISED LEARNING:
Supervised learning models can make predictions after seeing lots of data with the correct answers and then discovering the connections between the elements in the data that produce the correct answers.
This is like a student learning new material by studying old exams that contain both questions and answers.
Once the student has trained on enough old exams, the student is well prepared to take a new exam.
These ML systems are "supervised" in the sense that a human gives the ML system data with the known correct results.

Two of the most common use cases for supervised learning are regression and classification.

* Regression
  
  A regression model predicts a numeric value. For example, a weather model that predicts the amount of rain, in inches or millimeters, is a regression model.

  See the table below for more examples of regression models:
  
  | Scenario | 	Possible input data	| Numeric prediction |
  | :-- | :--- | :--- | 
  |Future house price|	Square footage, zip code, number of bedrooms and bathrooms, lot size, mortgage interest rate, property tax rate, construction costs, and number of homes for sale in the area.|	The price of the home.|
  |Future ride time |	Historical traffic conditions (gathered from smartphones, traffic sensors, ride-hailing and other navigation applications), distance from destination, and weather conditions. |	The time in minutes and seconds to arrive at a destination.|

  Two common types of regression models are:

  - Linear regression, which finds the line that best fits label values to features.  
  - Logistic regression, which generates a probability between 0.0 and 1.0 that a system typically then maps to a class prediction.  
  
* Classification

  Classification models predict the likelihood that something belongs to a category.  
  Unlike regression models, whose output is a number, classification models output a value that states whether or not something belongs to a particular category.  
  For example, classification models are used to predict if an email is spam or if a photo contains a cat.

  Classification models are divided into two groups:
  1. binary classification
  2. multiclass classification.
  
  - **Binary classification models** output a value from a class that contains only two values, for example, a model that outputs either rain or no rain.</br>
  - **Multiclass classification models** output a value from a class that contains more than two values, for example, a model that can output either rain, hail, snow, or sleet.

    1. **binary classification**
    A type of classification task that predicts one of two mutually exclusive classes:

    - the positive class
    - the negative class
    For example, the following two machine learning models each perform binary classification:

    A model that determines whether email messages are spam (the positive class) or not spam (the negative class).
    A model that evaluates medical symptoms to determine whether a person has a particular disease (the positive class) or doesn't have that disease (the negative class).

    2. In supervised learning,
        a classification problem in which the dataset contains more than two classes of labels.
        For example, the labels in the Iris dataset must be one of the following three classes:

        * Iris setosa
        * Iris virginica
        * Iris versicolor
        A model trained on the Iris dataset that predicts Iris type on new examples is performing multi-class classification.

        In contrast, classification problems that distinguish between exactly two classes are binary classification models.
       
> A classification model predicts a class. In contrast, a regression model predicts a number rather than a class.

## 🌟 Unsupervised learning 🌟
Unsupervised learning models make predictions by being given data that does not contain any correct answers.
An unsupervised learning model's goal is to identify meaningful patterns among the data. In other words, the model has no hints on how to categorize each piece of data, but instead it must infer its own rules.

A commonly used unsupervised learning model employs a technique called `**clustering**`. The model finds data points that demarcate natural groupings.
Clustering differs from classification because the categories aren't defined by you. For example, an unsupervised model might cluster a weather dataset based on temperature, revealing segmentations that define the seasons. You might then attempt to name those clusters based on your understanding of the dataset.

* clustering
  #clustering
  Grouping related examples, particularly during unsupervised learning. Once all the examples are grouped, a human can optionally supply meaning to each cluster.
  Many clustering algorithms exist. For example, the k-means algorithm clusters examples based on their proximity to a centroid.

  <img width="404" alt="Screenshot 2024-01-30 at 7 59 36 PM" src="https://github.com/Riyavarshini/Self-learning-notes/assets/117080445/c1748665-585d-41e3-827e-9cdff3ab61ab">

  A human researcher could then review the clusters and, for example, label cluster 1 as "dwarf trees" and cluster 2 as "full-size trees."

## 🌟 Reinforcement learning 🌟
Reinforcement learning models make predictions by getting rewards or penalties based on actions performed within an environment. A reinforcement learning system generates a policy that defines the best strategy for getting the most rewards.

Reinforcement learning is used to train robots to perform tasks, like walking around a room, and software programs like AlphaGo to play the game of Go.
Using feedback from human raters to improve the quality of a model's responses. For example, an RLHF mechanism can ask users to rate the quality of a model's response with a 👍 or 👎 emoji. The system can then adjust its future responses based on that feedback.

## 🌟 Generative AI 🌟
Generative AI is a class of models that creates content from user input. For example, generative AI can create novel images, music compositions, and jokes; it can summarize articles, explain how to perform a task, or edit a photo.

Generative AI can take a variety of inputs and create a variety of outputs, like text, images, audio, and video. It can also take and create combinations of these. For example, a model can take an image as input and create an image and text as output, or take an image and text as input and create a video as output.
How does generative AI work? At a high-level, generative models learn patterns in data with the goal to produce new but similar data.

To produce unique and creative outputs, generative models are initially trained using an unsupervised approach, where the model learns to mimic the data it's trained on. The model is sometimes trained further using supervised or reinforcement learning on specific data related to tasks the model might be asked to perform, for example, summarize an article or edit a photo.

Generative AI is a quickly evolving technology with new use cases constantly being discovered. For example, generative models are helping businesses refine their ecommerce product images by automatically removing distracting backgrounds or improving the quality of low-resolution images.
