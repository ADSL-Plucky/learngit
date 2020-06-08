'''
@File    :   1.py
@Time    :   2020/05/15 09:46:18
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
from flask import Flask,request,render_template,redirect

app = Flask(__name__)

from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
    username = TextField("username",[validators.Required()])
    password = PasswordField("password",[validators.Required()])

@app.route("/user",methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method =='POST':
        if myForm.username.data =="user" and myForm.password.data=="password" and myForm.validate():
            return redirect("http://www.baidu.com")
        else:
            message = "Failed Login"
            return render_template('login1.html',message=message,form=myForm)
    return render_template('login1.html',form=myForm)

if __name__ == '__main__':
    app.run(debug=True)