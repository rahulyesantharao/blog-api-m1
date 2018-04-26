[MIT Splash](https://esp.mit.edu/learn/Splash/index.html "MIT Splash") is a weekend program where MIT students teach classes on literally any topic for high schoolers. This past year (sorry for the late post!), I taught an intro class on ReactJS, and I was pretty happy with how it went, so I wanted to do a quick write up here (including a tutorial at the bottom).

### Preparing A Class
I was originally planning on creating an example application for the class and having the class follow along as we built the app up from the scratch. After thinking about the various basic topics that I wanted to teach and how to best demonstrate them, however, I realized that the [example tic-tac-toe app](https://reactjs.org/tutorial/tutorial.html "example tic-tac-toe app") that Facebook provides is perfectly suited to demonstrate all the foundational concepts that make React so exciting. So, I decided instead to prepare a good presentation that follows this tutorial and to explain each concept thoroughly as we came upon it in the example application. I figured this would still add value to independently following the tutorial as it would let me explain difficult concepts (e.g. unidirectional data flow) in greater detail and allow the students to ask questions. This turned out to be true, as my students asked me many questions that were not directly addressed in the tutorial (and indeed, which I hadn’t thought of myself).

In addition, I prepared a detailed explanation of how to set up the development environment because it is [extremely nontrivial](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f "extremely nontrivial") to get even a minimal setup to go from React code to a functioning website (that link was from 2 years ago, and believe it or not, it's only gotten worse!). I went with the create-react-app package as it would abstract away most of the specific tools and workflow (e.g. transpiling, packaging, linting, etc.) and allow us to focus on code. I did, however, plan out time to explain further time to explain these ideas and point the students to further resources to learn exactly how we go from code to product.

Overall, preparing the class turned out to be reasonably quick (~2 hours), as I just went with a PowerPoint that listed the key topics and made sure that I reviewed the topics so I could field questions about them the next day.

### Teaching A Class
The day of the event was a bit hectic as I had been planning on a Linux environment (and all my instructions were based on this assumption), but the lab I was put in had Windows machines; worse, they didn't have sufficient rights to install any software. This completely threw off my plan, as we couldn't install Node (there are ways to run Node as a local user, but I thought getting that set up for each student would completely sidetrack us from the main goal of learning React). Luckily, Facebook came to the rescue once again, and I just explained the idea of setting up an environment and then had the students work on the online CodePen that is set up to follow the React tutorial.

While teaching, I began suspecting that many of the students were getting lost, but also were too shy or embarrassed to ask for further clarification (although I did stop after each slide to check if the students had any questions). My suspicions were confirmed when one student finally began asking questions, and after that, the students began asking more frequently about confusing topics. One particularly confusing topic was unidirectional data flow, which I diagrammed on the blackboard to show how the UI is always a visual representation of the current state.

Overall, teaching was pretty fun after the few hiccups in setup because explaining topics that I find interesting and conveying the reason for their usefulness is exciting.

### A Class
As promised, here is the actual tutorial! Hopefully you found my ramblings above interesting, or at least short enough to skip over. One thing that becomes quickly evident when trying to teach/learn web development is that it's really useful (maybe even necessary) to have a pretty good grasp over basic JavaScript and (importantly) ES6. So, before going over this tutorial, it might be a good time to head over to [the MDN tutorials](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript "the MDN tutorials") and refresh your JavaScript.

Check out the PowerPoint [here](https://rahulyesantharao.com/blog-posts/assets/react-tutorial.pdf "here") and follow along at [the Facebook React Tutorial](https://reactjs.org/tutorial/tutorial.html "the Facebook React Tutorial").

Check back soon for a more detailed tutorial!