# Twilio_HowToSMS

## What is Twilio? 
Twilio is a customer engagement SaaS tool founded in 2008 that is used by companies like Doordash and Stripe, allowing them to make meaningful connections with their users. They put it best: 
> We’re known for democratizing channels like voice, text, chat, video, and email through APIs, making it easy for every organization to build meaningful interactions with customers on the channels they prefer.

Do you remember the transition from flip phones to iPhone, having to rewind a VCR tape to simply swiping the scroll bar on Netflix. Whether you do or not, it's clear that we have entered the digital-era and it's here to stay. **Either embrace the innovation, or lag behind** This new age has empowered indivuals to take advantage of technology to build businesses like we've never seen before. According to [Insider Intelligence](https://www.insiderintelligence.com/insights/ecommerce-industry-statistics/), amid the pandemic, US ecommerce sales will cross $1 trillion for the first time in 2022, this milestone was previously forecasted for 2024. 

There are many causes for this explosion of ecommerce including the rise in the use of mobile devices -- people are now able to buy and sell over the Internet more flexibly, quickly, and passively. In today's customer-centric world, businesses need to become more personalized and communicative through channels that are preferred by their consumers: mobile. 

Here are a few quick statistics from [Postscript's Text Messaging Statistics in 2020](https://postscript.io/blog/text-messaging-statistics): 
1. Over 77% of the entire population owns a smartphone. 
2. 68% of companies expect that mobile messaging will play a major role in consumer marketing soon. 
3. Customers are 134% more likely to respond to texts than email. 
4. The average person reads almost all of their texts, with nearly a 100% "read" rate. 

Given these stats and the growth along this horizon, there are still many opportunities for businesses to take advantage of SMS marketing and communication. It's personal, simple, outperforms other channels, and can be easily implemented with Twilio; let's get started :partying_face: 

## Users 
The users of Twilio can be segmeneted into two sections: 
1. Developers from any consumer-facing company 
2. Non-technical Marketing Teams at large companies 

## Prerequisites 
- Create a [Twilio Account](https://www.twilio.com/sms) to obtain your SMS-enabled Twilio phone number. We will need our account SID and auth token. 
- Create a Ngrox Account (*optional, but non-users can only use the service for 2 hrs* 
- Download [Python 3](https://www.python.org/downloads/) 
- Download [VS Code](https://code.visualstudio.com/download) (*optional; but I will be using this text-editor throughout the tutorial*)

## Subrequisites 
For this tutorial, we are going to be leveraging virtual environments. This will allow us to isolate and organize the dependencies for this Python project. 

If you've never worked with virtual environments, don't worries! I'll give you a brief introduction to this useful tool so you can follow along with this tutorial. I reccommend checking out the [official docs](https://docs.python.org/3/tutorial/venv.html) from Python to implement this principle for future projects. 

# Welcome to Drip2Duong Coffee 
Although Drip2Duong (would be an incredibly sick name for a :coffee: brand) this is a made-up example of a small ecommerce business (user persona #3) that would use Twilio SMS in attepts to not lagging behind. 

Drip2Duong Coffee is an ecommerce brand that sells coffee beans, creamers, and accessories. They want to excelerate their sales growth in the upcoming quarter, through building a more loyal customer base. We've just been offered a free bag of beans every month to help Drip2Duong coffee use Twilio SMS to build a foundation for communicating through SMS with their customers. 

## What We are Building 
To help Drip2Duong reach their quarter goals, we are using Twilio to: 
- :outbox_tray: Send an outbound message 
- :inbox_tray: Reply to an inbound message 

Watch [video](https://www.youtube.com/watch?v=tDb8ofsNpwI) for full tutorial, feel free to clone this repo to get building. You will need to create your own virtual environment first (steps in video).  

## Engagement 
- Star this repo -> we have a head count of how many people are getting involved! 
- Discord channel to be created to track engagement and success of tutorial. 

## What's Next? 
Drip2Duong is now able to send messages to their customers and have opened the feedback loop by accepting inbound messages. Using everything we have learned, if we choose, we can counter offer the :coffee:/month with :coffee: + :milk_glass:/ month in exchange for the implementation of a survey option. 

You can help Drip2Duong Coffee use Twilio to send an outbound message soliciting a survey response from users over SMS. This is your chance to build upon the logic we implemented for replying to an inbound message. 

Additionally, you can pipe the responses from the text messages out of the ngrox UI and into a Google Sheet (or Airtable) so Drip2Duong can more easily access extract meaning from their customer responses. 

## References
[Twilio Developer Docs](https://www.twilio.com/docs/sms/quickstart/python)
