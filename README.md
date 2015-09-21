Uses Scrapy to crawl and parse all articles by [The Daily Clog](http://www.dailycal.org/section/blogs/clog/), a blog by The Daily Californian, for sentences with the word "You", to have a Fortune Cookie like list of quotes. Eg: "In tough times like these, what have you got to lose?" or "You've had your ups and downs with that bird, and now it's time to let go."

Requires Python and Scrapy. To run, go to the root directory and enter,

`scrapy crawl clog` 

To store the results as a JSON file, enter,

`scrapy crawl clog -o items.json`