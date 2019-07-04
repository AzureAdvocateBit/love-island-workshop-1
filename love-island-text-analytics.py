#!/usr/bin/env python
# coding: utf-8

# # Love Island Tweet Analysis Workbook

# First run a pip install command to get a package that will help us query the Azure Text Analytics API

# In[ ]:


get_ipython().system(u'pip install --upgrade azure-cognitiveservices-language-textanalytics')


# In[ ]:


# import packages needed
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials


# In[ ]:


# enter your subscription key below
subscription_key = "<ENTER KEY>"
credentials = CognitiveServicesCredentials(subscription_key)


# In[ ]:


# Enter datacenter location
text_analytics_url = "https://<ENTER LOCATION>.api.cognitive.microsoft.com/"
text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)


# In[ ]:


# After running the sample use the love-island-tweetdata.csv file to input different tweet text to test
documents = [
    {
      "id": "1", 
      "language": "en", 
      "text": "I like lucie n all but I love Amy she is just new to everything people need to stop judging #loveisland"
    },
    {
      "id": "2", 
      "language": "en", 
      "text": "But Amy doesn't deserve Curtis #loveisland"
    },  
    {
      "id": "3", 
      "language": "es", 
      "text": "Really hope Arrabella gets a new bit in casa amor just purely for my own entertainment and the look on Danny's face #Loveisland"
    },  
    {
      "id": "4", 
      "language": "it", 
      "text": "can we just vote out Danny and Arrabella already pls????? nobody is interested in seeing snakes in the villa @LoveIsland #LoveIsland"
    }
  ]


# In[ ]:


# Call the web API and loop through each document returned in the JSON response to get the results and the sentiment score
# Sentiment: Positive = closer to 1, Negative = closer to 0
response = text_analytics.sentiment(documents=documents)
for document in response.documents:
     print("Document Id: ", document.id, ", Sentiment Score: ", "{:.2f}".format(document.score))


# In[ ]:


# Call the web API and loop through each document returned in the JSON response to get the results and the sentiment score
# Kay Phrase: return key words in the sentence
response = text_analytics.key_phrases(documents=documents)

for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Phrases:")
    for phrase in document.key_phrases:
        print("\t\t",phrase)

