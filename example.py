from flask import Flask, request

a = Flask(__name__)

@a.route('/')
def hW():
    return 'This is the main page. <a href="http://localhost:5000/f1">Click here to see the form.</a>'

@a.route('/f1')
def f1():
    return """ <form action="http://localhost:5000/rF1" method='GET'>
  <input type="checkbox" name="v1" value="Bike"> I have a bike<br>
  <input type="checkbox" name="v2" value="Car"> I have a car<br>
  <input type="checkbox" name="v3" value="Trolley"> I have a trolley
  <input type="submit" value="Submit">
</form>"""

@a.route('/rF1',methods=["GET"])
def rF1():
    if request.method == "GET":
        print(request.args)
        rs = ""
        for k in request.args:
            rs += "{} - {}<br><br>".format(k, request.args.get(k,""))
        return rs
    return "Nothing was selected this time!"

@a.route('/f2')
def f2():
    return """<form action="http://localhost:5000/lR" method='GET'>
    <input type="text" name="p"><br>
    <input type="submit" value="Submit">
    """

@a.route('/lR',methods=["GET"])
def lR():
    if request.method == "GET":
        p = request.args.get('p','')
        tn = 0
        for ch in p:
            if ch == "e":
                tn += 1
        return "There were {} occurrences of the letter e in the entered phrase".format(tn)
    return "Nothing was submitted yet... <a href='http://localhost:5000/f2'>Go submit something</a>"

if __name__ == "__main__":
    a.run(use_reloader=True, debug=True)
