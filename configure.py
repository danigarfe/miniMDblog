
art_model_file = open("./models/article_config.html") 
art_model_text = art_model_file.read()
index_model_file = open("./models/index_config.html") 
index_model_text = index_model_file.read()

name = input("Introduce a name for your blog: ")
art_model_text = art_model_text.replace("$$$blogname", name)
index_model_text = index_model_text.replace("$$$blogname", name)

author = input("Introduce the author's name: ")
art_model_text = art_model_text.replace("$$$author", author)
index_model_text = index_model_text.replace("$$$author", author)

art = open("./models/article.html", 'w')
art.write(art_model_text)
art.close()

index = open("./models/index.html", 'w')
index.write(index_model_text)
index.close()




