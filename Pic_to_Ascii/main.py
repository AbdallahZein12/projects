from flask import Flask, render_template, url_for, redirect, request
import os
from PIL import Image
import json



app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
@app.route("/home", methods=["GET","POST"])
def home():
    if request.method == "POST":
        file = request.files['file']
        dir = os.path.join("file_handling",file.filename)
        file.save(dir)
        with open("output.txt",'w') as output:
            with Image.open(dir) as im:
                im = im.convert('L')
                im = im.resize((80,60))
                chars = '.:-=+*#%@'
                for y in range(im.size[1]):
                    for x in range(im.size[0]):
                        gray = im.getpixel((x,y))
                        char = chars[gray * len(chars) // 355]
                        output.write(char)
                    output.write("\n")
        with open("output.txt",'r') as output:    
            final_output = output.read()
        os.remove(dir)
        with open("output.txt",'w') as output:
            output.truncate(0)
            
        return json.dumps({"output": final_output})
    
    
    return render_template("home.html",output="")

# @app.route('/upload',methods=['POST'])
# def upload_file():
#     file = request.files['file']
#     dir = os.path.join("file_handling",file.filename)
#     file.save(dir)
#     with open("output.txt",'w') as output:
#         with Image.open(dir) as im:
#             im = im.convert('L')
#             im = im.resize((80,60))
#             chars = '.:-=+*#%@'
#             for y in range(im.size[1]):
#                 for x in range(im.size[0]):
#                     gray = im.getpixel((x,y))
#                     char = chars[gray * len(chars) // 355]
#                     output.write(char)
#                 output.write("\n")
#     with open("output.txt",'r') as output:    
#         final_output = output.read()
#     os.remove(dir)
#     with open("output.txt",'w') as output:
#         output.truncate(0)
    
#     return render_template("home.html",output=final_output)

@app.route("/more")
def more():
    return render_template("more.html")


if __name__ == "__main__":
    app.run(debug=True)