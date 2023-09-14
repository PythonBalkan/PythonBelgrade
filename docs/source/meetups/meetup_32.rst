.. _meetup_32:

Python Belgrade #31
=================

- Location: `UK Stari Grad <https://goo.gl/maps/efU19kvACXS7XmdEA>`_
- Date: 2022-05-27 18:00

Talks:
-----

Python Microservices with gRPC
---

.. toctree::
  ../speakers/speaker_10

- Abstract:
Purpose for this study is to introduce the concept behind microservices, differences between microservices and monolithic applications, benefits and pitfalls of each and scaling. Inspiration for this came from the issues that I have encountered while working with large monolithic applications, mainly regarding scaling and speed of the service. Having all of the code in one place in early stages of development is better, lets you develop faster which is critical when starting, is less complicated to share between developers and allows for easier deployment in one go. But, as the codebase and complexity of the app grows, all of these pros that made it easier in the beginning, can gradually make a monolith harder to develop and maintain. Implementing microservices can be time consuming, but will allow for better scaling in the long run if applied at the right time - not too soon, not too late. Why microservices? Flexibility, scalability and robustness are main pros of implementing microservices. It will make a way to organize complex systems, breaking them down into smaller pieces that communicate with each other and deployed independently. They can also be written in different languages, giving the app even more flexibility. Why gRPC over REST? Well, we can use REST for microservices as well, but there are many pros in using protocol buffers. Performance, documentation and validation are the main ones. gRPC is built on top of HTTP/2 which can make multiple requests in parallel and is more efficient in this case, when using it for internal communication. Also, gRPC has interceptors that are used to monitor the communication between services, logging exceptions, requests and latencies. Generally, a go-to for our case and we will cover it in depth.

A step towards the fully automated Kubernetes infrastructure with Python
---

.. toctree::
  ../speakers/speaker_11

- Abstract:
In this talk, we'll walk down the rabbit hole of Kubernetes most mysterious components: Controllers, and Operators. We'll do a deep dive into the subject, and by the end of it, you will be either utterly amazed or utterly confused (as is the case with any Kubernetes topic).

