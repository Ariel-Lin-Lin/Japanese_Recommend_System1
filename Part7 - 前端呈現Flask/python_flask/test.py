from flask import Flask, render_template , session, redirect, url_for, escape, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)

@app.route('/')
def gender():
   return render_template('gender.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == "POST":
      result_a = request.form
      result_aa = result_a.to_dict(flat=False)
      result = result_aa['sex'][0]
      print(result)
      print(type(result))
      # sex = request.values.get("sex")
      if result == 'W':
         return render_template('test_W.html', result=result)
      else:
         return render_template('test_M.html', result=result)
#傳送門
#女生
@app.route('/testW', methods = ['GET', 'POST'])
def testW():
   if request.method == "POST":
      return render_template('test_W.html')

@app.route('/completeW', methods = ['GET', 'POST'])
def completeW():
   if request.method == "POST":
      return render_template('completeW.html')

@app.route('/resultW', methods = ['GET', 'POST'])
def resultW():
   if request.method == "POST":
      return render_template('resultW.html')

@app.route('/selectW', methods = ['GET', 'POST'])
def selectW():
   if request.method == "POST":
      return render_template('selectW.html')

@app.route('/selectW1', methods = ['GET', 'POST'])
def selectW1():
   if request.method == "POST":
      return render_template('selectW1.html')

@app.route('/selectW2', methods = ['GET', 'POST'])
def selectW2():
   if request.method == "POST":
      return render_template('selectW2.html')

@app.route('/resultALS_W', methods = ['GET', 'POST'])
def resultALS_W():
   if request.method == "POST":
      return render_template('/resultALS_W.html')

@app.route('/chartW', methods = ['GET', 'POST'])
def chart_W():
   if request.method == "POST":
      return render_template('chartW.html')

#男生
@app.route('/testM', methods = ['GET', 'POST'])
def testM():
   if request.method == "POST":
      return render_template('test_M.html')

@app.route('/completeM', methods = ['GET', 'POST'])
def completeM():
   if request.method == "POST":
      return render_template('completeM.html')

@app.route('/resultM', methods = ['GET', 'POST'])
def resultM():
   if request.method == "POST":
      return render_template('resultM.html')

@app.route('/selectM', methods = ['GET', 'POST'])
def selectM():
   if request.method == "POST":
      return render_template('selectM.html')

@app.route('/selectM1', methods = ['GET', 'POST'])
def selectM1():
   if request.method == "POST":
      return render_template('selectM1.html')

@app.route('/selectM2', methods = ['GET', 'POST'])
def selectM2():
   if request.method == "POST":
      return render_template('selectM2.html')

@app.route('/resultALS_M', methods = ['GET', 'POST'])
def resultALS_M():
   if request.method == "POST":
      return render_template('/resultALS_M.html')

@app.route('/chartM', methods = ['GET', 'POST'])
def chart_M():
   if request.method == "POST":
      return render_template('chartM.html')

#全部圖表
@app.route('/chartALL', methods = ['GET', 'POST'])
def chart_ALL():
   return render_template('chartALL.html')
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

