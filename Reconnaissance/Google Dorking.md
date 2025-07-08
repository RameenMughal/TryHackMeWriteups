# Google Dorking

## Let’s Learn About Crawlers
These crawlers discover content through various means. One being by pure discovery, where a URL is visited by the crawler and information regarding the content type of the website is returned to the search engine. In fact, there are lots of information modern crawlers scrape.

Another method crawlers use to discover content is by following any and all URLs found from previously crawled websites. Much like a virus in the sense that it will want to traverse/spread to everything it can.

The diagram below is a high-level abstraction of how these web crawlers work. Once a web crawler discovers a domain such as mywebsite.com, it will index the entire contents of the domain, looking for keywords and other miscellaneous information

![image](https://github.com/user-attachments/assets/0c664b70-3c0f-401c-b7ca-f7188f48b97b)

In the diagram above, "mywebsite.com" has been scraped as having the keywords as “Apple” “Banana" and “Pear”. These keywords are stored in a dictionary by the crawler, who then returns these to the search engine i.e. Google. 

Because of this persistence, Google now knows that the domain “mywebsite.com” has the keywords “Apple", “Banana” and “Pear”. 

As only one website has been crawled, if a user was to search for “Apple”...“mywebsite.com” would appear. This would result in the same behaviour if the user was to search for “Banana”. As the indexed contents from the crawler report the domain as having “Banana”, it will be displayed to the user.

A user submits a query to the search engine of “Pears". Because the search engine only has the contents of one website that has been crawled with the keyword of “Pears” it will be the only domain that is presented to the user. 

However, as we previously mentioned, crawlers attempt to traverse, termed as crawling, every URL and file that they can find! Say if “mywebsite.com” had the same keywords as before (“Apple", “Banana” and “Pear”), but also had a URL to another website “anotherwebsite.com”, the crawler will then attempt to traverse everything on that URL (anotherwebsite.com) and retrieve the contents of everything within that domain respectively.

The crawler initially finds “mywebsite.com”, where it crawls the contents of the website - finding the same keywords (“Apple", “Banana” and “Pear”) as before, but it has additionally found an external URL. Once the crawler is complete on “mywebsite.com”, it'll proceed to crawl the contents of the website “anotherwebsite.com”, where the keywords ("Tomatoes", “Strawberries” and “Pineapples”) are found on it. The crawler's dictionary now contains the contents of both “mywebsite.com” and “anotherwebsite.com”, which is then stored and saved within the search engine.

“anotherwebsite.com” was only crawled because it was referenced by the first domain “mywebsite.com”. 

### Answer the questions below
1. Name the key term of what a "Crawler" is used to do. This is known as a collection of resources and their locations. 

Index

2. What is the name of the technique that "Search Engines" use to retrieve this information about websites?

Crawling

3. What is an example of the type of contents that could be gathered from a website?

Keywords

## Enter: Search Engine Optimisation

Search Engine Optimisation or SEO is a prevalent and lucrative topic in modern-day search engines.

At an abstract view, search engines will “prioritise” those domains that are easier to index. There are many factors in how “optimal” a domain is - resulting in something similar to a point-scoring system.

To highlight a few influences on how these points are scored, factors such as:
- How responsive your website is to the different browser types I.e. Google Chrome, Firefox and Internet Explorer - this includes Mobile phones!
- How easy it is to crawl your website (or if crawling is even allowed) through the use of "Sitemaps"
- What kind of keywords your website has 

There are various online tools such as Google Site Analyzer.

## Beepboop – Robots.txt

Similar to "Sitemaps", this file is the first thing indexed by "Crawlers" when visiting a website.

This file must be served at the root directory - specified by the webserver itself. Looking at this files extension of .txt, its fairly safe to assume that it is a text file.

The text file defines the permissions the "Crawler" has to the website. 

For example, what type of "Crawler" is allowed (I.e. You only want Google's "Crawler" to index your site and not MSN's). 

Moreover, Robots.txt can specify what files and directories that we do or don't want to be indexed by the "Crawler".

Here we have a few keywords
- User-agent: Specify the type of "Crawler" that can index your site (the asterisk being a wildcard, allowing all "User-agents"
- Allow: Specify the directories or file(s) that the "Crawler" can index
- Disallow: Specify the directories or file(s) that the "Crawler" cannot index
- Sitemap: Provide a reference to where the sitemap is located

### Answer the questions 

1. Where would "robots.txt" be located on the domain "ablog.com"

ablog.com/robots.txt

2. If a website was to have a sitemap, where would that be located?

/sitemap.xml

3. How would we only allow "Bingbot" to index the website?

User-agent:Bingbot

4. How would we prevent a "Crawler" from indexing the directory "/dont-index-me/"?

Disallow: /don’t-index-me/

5. What is the extension of a Unix/Linux system configuration file that we might want to hide from "Crawlers"?

.conf

## Sitemaps

Comparable to geographical maps in real life, “Sitemaps” are just that - but for websites!

“Sitemaps” are indicative resources that are helpful for crawlers, as they specify the necessary routes to find content on the domain. 

![image](https://github.com/user-attachments/assets/2f383dc1-a518-4904-873a-4f9c1cf37aac)

The blue rectangles represent the route to nested-content, similar to a directory I.e. “Products” for a store. Whereas, the green rounded-rectangles represent an actual page. However, this is for illustration purposes only - “Sitemaps” don't look like this in the real world.

“Sitemaps” are XML formatted

Search engines have a lot of data to process. The efficiency of how this data is collected is paramount. Resources like "Sitemaps" are extremely helpful for "Crawlers" as the necessary routes to content are already provided! All the crawler has to do is scrape this content - rather than going through the process of manually finding and scraping. 

### Answer the questions below

1. What is the typical file structure of a "Sitemap"?

XML

2. What real life example can "Sitemaps" be compared to?
  
Map

3. Name the keyword for the path taken for content on a website.

Route

## What is Google Dorking?

We can add operators such as that from programming languages to either increase or decrease our search results - or perform actions such as arithmetic!

If we wanted to narrow down our search query, we can use quotation marks. Google will interpret everything in between these quotation marks as exact and only return the results of the exact phrase provided.

Example: “American pscho poster”

We can use terms such as “site” (such as bbc.co.uk) and a query (such as "gchq news") to search the specified site for the keyword we have provided to filter out content that may be harder to find otherwise.

Example: site: bbc.co.uk gchq news

A few common terms we can search and combine include:
- filetype: Search for a file by its extension (e.g. PDF)
- cache: View Google's Cached version of a specified URL
- intitle: The specified phrase MUST appear in the title of the page

For example, let's say we wanted to use Google to search for all PDFs on bbc.co.uk:

site:bbc.co.uk filetype:pdf

### Answer the questions below

1. What would be the format used to query the site bbc.co.uk about flood defences

site: bbc.co.uk flood defences

2. What term would you use to search by file type?

filetype:

3. What term can we use to look for login pages?

intitle: login
