<h1>Bytes</h1>
Abir H., Parina K., Anam, W., Daniel W.

Summary: We are making a webapp that allows users to find the best deal on restaurants and/or hotels within a certain radius of a location, using the information given by the TripAdvisor API.

What defines a "good deal," is defined by the restaurants deviation from the linear regression analysis of the restaurant's rating vs. price level. If a restaurant is a good deal, it's actual rating will be above the estimated rating using this line. Using the deviations for the restaurants, we ranked in order which ones offered the best deals and displayed them to the user.
To run, download the entire project folder and run run.py using Python3.x. This will open a server on localhost:5000, which can be interfaced with through a browser.

<h2>Inspiration</h2>
"I never actually know if I'm getting a good deal anymore..."

While enjoying some free pizza, we began to discuss the struggles of being broke students in New York City.

"The food is good, but it's also really expensive."

"How much is too much for good food?"

"Bad food is cheap food and that's all that matters."

There are countless websites to check out food in your area, but they're all missing a critical element: <h4>a comparison with other local restaurants to determine if the food is a good value.</h4>

<h2>What it does</h2>
Bytes compares the ratings and cost of a restaurant to other restaurants around you to help you get the best food for your money. Bytes, taking into account cost/rating ratio of local restaurants, calculates a score and assigns a letter grade determining the quality of the deal. The higher the score, the better the deal!

<h2>How it works</h2>
Back-end dependencies: Requests, BeautifulSoup, NumPy, SciPy, GeoPy

Bytes is written in Python, using the Yelp API. GeoPy was used to get location; its ability to easily acquire latitude and longitude coordinates worked well with Yelp's API calls. From there, the API generates a list of restaurants within the specified distance, feeds their cost and rating into SciPy, calculates a linear regression based on this data. From there, the restaurants are rated based on their actual position either above or below the regression line; above meaning a better than average deal, and below meaning worse than average. NumPy is used to simplify some of the mathematical work behind this. The data is returned with the name of the restaurant, the score, and the letter grade. 

The front end was written using HTML and CSS to provide a web interface. JavaScript and Flask were used to integrate front end (mostly user input) with the back end. Bootstrap was used for a simple, sleek interface and compatibility with mobile devices.

<h2>Challenges we ran into</h2>
The greatest challenge by far has been using Flask to tie the front and back ends together, with the largest obstacle being getting user input into the back end, and then taking the results from the back end and outputting it to the front end. In the end, I used Python to return a dynamically generated HTML page containing all of the results. The true issue lied in returning info from Python to JS, so we opted to create the page in Python instead.

```for i in range(0, 20):
			...
			html_data += '''<div class="container">
			<a href="{}" target="_blank">
			<div class="jumbotron" id="result">
			<div class="block" style="background-image: url({}); background-size:cover;"></div>
	        <div class="row">
	            <div class="col-sm-8">
	                <h2>{}</h2>
	                <h4>{} miles</h4>
	                <h4>{}</h4>
	                <h4>{}</h4>
	            </div>
	            <div class="col-sm-2">
	                <h2>{}</h2>
	                <h4>{} reviews</h4>
	                <h2>{}</h2>
	            </div>
	            <div class="col-sm-1 col-sm-offset-1">
	                <h1>{}</h1>
	                <h3>{}</h3>
	            </div>
	        </div>
	        </div>
	    </div>\n
	    </a>'''.format(url, image_url, name, miles, add, phone, rating, reviews, price, data[i][1], data[i][0])

  ...
  with open(new_page, 'w') as new:
		new.write(page)
		new.write(html_data)
		new.write('</body>\n<html>')

	return render_template('results.html')
```

Bytes is a localhost:5000 only application, because hosting on AWS is frustratingly complicated.

<h2>What's next for Bytes</h2>
Bytes, in its current state, works very efficiently for finding local deals on food. However, this behavior could easily be extended to other areas such as hotels, attractions, and other things. Adding other features such as displaying menus, maps, having user accounts to allow users to save favorites and view eating history, share recommendations with friends, etc. Bytes could also (in a non-evil way) collect data about its users, using this information to improve user experience and perhaps even local food options. Most importantly, cleaning up the integration between the front and back ends using Flask would be great.
