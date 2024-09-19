contents = ["All carrots are to be sliced longitudinally. And this first string is unbelievably long so I am going to" 
            " split it right here",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()