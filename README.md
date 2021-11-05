# miniMDblog

A tool to automatically generate a minimal blog (html and css files) based on articles written in Markdown. 

## Usage
Download the base structure:
```
$ git clone git://github.com/danigarfe/miniMDblog.git miniMDblog
$ cd miniMDblog
```
Install dependencies:
```
pip install -r requirements.txt
```

Configure your blog's title and author:
```
$ python configure.py
```

Now you are ready to write your articles in the /articles folder. Three examples have been added. 

Building the website:
```
$ python run.py
```

You will now be able to find the assembled website in /output folder. You can change your blog's name and author anytime by running "configure.py" again. 

## Article writing
The first line of each article file must be its title. The second line must be the publication date. Next lines are the content of the article, writen in Markdown. Each time a new article is written, run.py must be executed in order to rebuild the page and add it. 
