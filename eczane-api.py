from flask import Flask, render_template
import http.client
import json

# your code will be in here

# template of the conversion method from response to data
def convertToJson(data):
    stringData = data.decode("utf-8")
    # print(stringData)
    jsonObj = json.loads(stringData)
    print(jsonObj)
    return render_template('template.html', data=jsonObj)


if __name__ == "__main__":
    print("start")
    #app.run(host="0.0.0.0", port=5005, debug=True)  