from sodapy import Socrata
from flask import Flask, render_template, request
import annoying
app= Flask(__name__)

@app.route('/')
def annoyingo():
    return render_template('frontend.html')

@app.route('/', methods=['POST'])
def getzip():
    zip=request.form['zipcode']
    dat=annoying.searchLocation(zip)
    return render_template('annoyingy01.html',zipcode=dat[0])

if __name__=='__main__':
    app.run()


def searchLocation(zipcode):
    """
    returns a list of the data with state given
    """
    client= Socrata("data.cdc.gov",None)
    results=client.get("5jp2-pgaw", loc_admin_zip=request.form['zipcode'])
    result=getstate(results)
    return result


def getstate(lst):
    """
    returns the necessary information from json
    """
    outerlist=[]
    for x in lst:
        innerlist=[]
        for key in x:
                innerlist.append(x[key])
        outerlist.append(innerlist)
    return outerlist
