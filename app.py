from flask import Flask, render_template
import urllib.request, json
# import os

app = Flask(__name__)

# @app.route("/")
# def get_countries():
#     url = "https://restcountries.com/v3.1/all"
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     dict = json.loads(data)
#     # print(dict)
#     print(dict[0])
#     # return render_template ("countries.html", countries=dict["results"])
#     # return render_template ("countries.html")
#     return(dict)


@app.route("/countries")
def get_countries_list():
    url = "https://restcountries.com/v3.1/all"
    response = urllib.request.urlopen(url)
    countries = response.read()
    dict = json.loads(countries)

    # countries = []

    # for movie in dict["results"]:
    #     movie = {
    #         "title": movie["title"],
    #         "overview": movie["overview"],
    #     }
    #     movies.append(movie)
    # return {"results": movies}
    countries=[]
    for i in range(len(dict)):
        country={
            "altSpellings":dict[i]["altSpellings"],
            "area":dict[i]["area"],
            # "capital":dict[i]["capital"],  
            "name":dict[i]["name"],
        }
        countries.append(country)
    return{"results":countries}


if __name__ == '__main__':
    app.run(debug=True,port=8081)