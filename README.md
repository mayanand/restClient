Using Object Oriented Python, this script to a REST service to obtain a collection of JSON objects containing links to News Stories about a certain topic, saving any images from the news stories to a folder. This code accomplishes the following objectives:

1.	Calls the Guardian REST endpoint and retrieve the data 
2.	Iterates the objects 
3.	For each object call the contained url; 
		a.	Parse the contents of the returned object and attempt to extract the image hrefs 
		b.	Request the images directly and save to a folder 
4.	Completes the same task for the Google REST endpoint 

Design:
1. A base class that contains generic code for connecting to an API, capable of iterating through objects and storing the image files to the disk.
2. Derived classes can be used to extend the base class to customize the script. For instance customization for google news and guardian has been done here in the derived class.