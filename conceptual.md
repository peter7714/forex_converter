### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  javascript is more for handling the code with the user and python is for serving the code to the user

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  dict = ``{'a': 1, 'b': 2}``
  dict.get('c', "doesn't exist")

- What is a unit test?

  a unit test is when you test a singular function within your application 

- What is an integration test?

  an integration test is when you test how functions interact with each other 


- What is the role of web application framework, like Flask?

  to handle the heavy lifting for the back end of a web app

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  query string would be useful to look for content related to the inputs the directory way would be usful if the page is dedicated to the content at hand

- How do you collect data from a URL placeholder parameter using Flask?

  using the "<placeholder>" syntax within the app.route declaration 

- How do you collect data from the query string using Flask?

  request.form

- How do you collect data from the body of the request using Flask?
  
  request.args 

- What is a cookie and what kinds of things are they commonly used for?

  to store session date to provide a better experience like adding items to a cart and keeping them there the next time a user visits the page.

- What is the session object in Flask?

  it stores data that you declare, mostly to keep track of a users habbits 

- What does Flask's `jsonify()` do?
  transforms a string into json
