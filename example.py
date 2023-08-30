from flask import Flask, request

A = Flask(__name__)

@A.route('/')
def hW():
    return 'This is the main page. <a href="http://localhost:5000/F1">Click here to see the form.</a>'

@A.route('/F1')
def F1():
    return """ <form action="http://localhost:5000/rF1" method='GET'>
  <input type="checkbox" name="v1" value="Bike"> I have a bike<br>
  <input type="checkbox" name="v2" value="Car"> I have a car<br>
  <input type="checkbox" name="v3" value="Trolley"> I have a trolley
  <input type="submit" value="Submit">
</form>"""

@A.route('/rF1',methods=["GET"])
def rF1():
    if request.method == "GET":
        print(request.args)
        rs = ""
        for k in request.args:
            Rs += "{} - {}<br><br>".format(k, request.args.get(k,""))
        return Rs
    return "Nothing was selected this time!"

@A.route('/F2')
def F2():
    return """<form action="http://localhost:5000/lR" method='GET'>
    <input type="text" name="p"><br>
    <input type="submit" value="Submit">
    """

@A.route('/lR',methods=["GET"])
def lR():
    if request.method == "GET":
        P = request.args.get('p','')
        Tn = 0
        for ch in p:
            if ch == "e":
                Tn += 1
        return "There were {} occurrences of the letter e in the entered phrase".format(tn)
    return "Nothing was submitted yet... <a href='http://localhost:5000/F2'>Go submit something</a>"

if __name__ == "__main__":
    A.run(use_reloader=True, debug=True)
