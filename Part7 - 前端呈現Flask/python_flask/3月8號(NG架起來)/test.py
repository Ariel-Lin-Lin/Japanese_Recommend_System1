from flask import Flask, render_template , session, redirect, url_for, escape, request
from werkzeug.utils import secure_filename



app = Flask(__name__)

@app.route('/')
def gender():
   return render_template('gender.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == "POST":
      sex = request.values.get("sex")
      return render_template('test.html')

@app.route('/picture_select', methods = ['GET', 'POST'])
def picture_select():
   if request.method == "POST":
      return render_template('picture_select.html')



# 存檔案
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

   
# run app
if __name__ == "__main__":
    app.run(debug=True)

