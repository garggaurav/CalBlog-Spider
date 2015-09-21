Uses Scrapy to crawl and parse all articles by [The Daily Clog](http://www.dailycal.org/section/blogs/clog/), a blog by The Daily Californian, for sentences with the word "You".

Requires Python and Scrapy. To run, go to the root directory and enter,

`scrapy crawl clog` 

To store the results as a JSON file, enter,

`scrapy crawl clog -o items.json`