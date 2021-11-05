import os
from markdown import markdown
import minify_html

arts = []

#REMOVE PREVIOUS OUTPUT
files_art = next(os.walk("./output/art"), (None, None, []))[2]
for i in files_art:
    os.remove("./output/art/" + i)
files_out = next(os.walk("./output"), (None, None, []))[2]
for i in files_out:
    os.remove("./output/" + i)

#GET ARTICLES AND MODELS 
filenames = next(os.walk("./articles"), (None, None, []))[2]
art_model_file = open("./models/article.html") 
index_model_file = open("./models/index.html") 
art_model = art_model_file.read()
index_model = index_model_file.read()
index_model_file.close()
art_model_file.close()

#DETECT WETHER FILES ARE .MD (MARKDOWN)
for i in filenames:
    a = i[-3]+i[-2]+i[-1]
    if a!=".md":
        filenames.remove(i)

#FOR EACH ARTICLE
for name in filenames:
    f = open("./articles/" + name) 
    #GET TITLE, DATE AND TEXT 
    title = f.readline()
    date = f.readline()
    text = markdown(f.read())
    f.close()
    newfile_text = art_model

    #SET THEM IN PLACE IN THE MODEL
    newfile_text = newfile_text.replace("$$$0", title)
    newfile_text = newfile_text.replace("$$$1", date)
    newfile_text = newfile_text.replace("$$$2", text)

    #MINIFY
    newfile_text = minify_html.minify(newfile_text, minify_css=True, remove_processing_instructions=True)

    newfile_name = "./output/art/" + date.replace('/', '') + "_" + title.replace(' ', '_') + ".html"
    try:
        os.mkdir("./output/art/")
    except:
        pass

    #SAVE NEW ARTICLE
    newfile = open(newfile_name, 'w')
    newfile.write(newfile_text)
    newfile.close()
    arts.append([title,date])

#NEW ARTICLE MODEL FOR INDEX PAGE
index_entry = "<a href='$$$enlace'> <div class='article'> <div class='title'> <p>$$$titulo</p></div><div class='date'> <p>$$$fecha</p></div></div></a>"

#GETTING HTML PIECE OF CODE FOR EACH ARTICLE, ACCUMULATING ALL THEM
accum = ""
for article in arts:
    titulo = article[0]
    fecha = article[1]
    enlace = "./art/" + fecha.replace('/', '') +"%0A" + "_" + titulo.replace(' ', '_') +"%0A" + ".html"
    html = index_entry.replace("$$$enlace", enlace)
    html = html.replace("$$$titulo", titulo)
    html = html.replace("$$$fecha", fecha)
    accum +=html

#SETTING THE ACCUMULATED HTML IN PLACE INTO INDEX MODEL
index_html = index_model.replace("$$$0", accum)

#MINIFY
index_html = minify_html.minify(index_html, minify_css=True, remove_processing_instructions=True)

#SAVE INDEX
newindex = open("./output/index.html", 'w')
newindex.write(index_html)
newindex.close()
