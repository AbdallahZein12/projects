I started by creating a bask flask web server and then moved on to cr.eating the HTML templates.

I am using sockets because they provide a live real-time way of communicating rather than refreshing the page or saving stuff to the data base to transmit messages between different chat rooms and different clients.


we are gonna have a socket server which is going to be running on our flask web server and we are going to have different clients which are really just the web browsers that connect to that server they are going to send a message to our server. our server is going to look at what chatroom they are inside of, and then it is going to transmit that message to all of the people in that chat room. They are going to be listening for that message in the front end so in java script. and then they are gonna be displaying that on the screen.

I passed variables directly to the HTML code from the flask server and used the jenga templating engine in myy HTML code to render content served from server
