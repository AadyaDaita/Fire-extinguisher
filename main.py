# For Backend Code
# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() !=0:
            if name == "athena":  # input field has content
                return render_template("athena.html", name=name)
            if name == "Athena":  # input field has content
                return render_template("athena.html", name=name)
            if name == "allison":  # input field has content
                return render_template("allison.html", name=name)
            if name == "Allison":  # input field has content
                return render_template("allison.html", name=name)
            if name == "gaurish":  # input field has content
                return render_template("gaurish.html", name=name)
            if name == "Gaurish":  # input field has content
                return render_template("gaurish.html", name=name)
            if name == "aadya":  # input field has content
                return render_template("aadya.html", name=name)
            if name == "Aadya":  # input field has content
                return render_template("aadya.html", name=name)
            else:
                return render_template("minilab.html", name=name)
        else:
            # starting and empty input default
            return render_template("minilab.html", name="World")
    else:
        return render_template("minilab.html")


@app.route('/greet_commentforum', methods=['GET', 'POST'])
def greet_commentforum():
    # submit button has been pushed
    if request.form:
        comment = request.form.get("comment")
        if comment.__len__() != 0:  # input field has content
            return render_template("commentforum.html", comment=comment)
        else:
            # starting and empty input default
            return render_template("commentforum.html", comment="World")
    else:
        return render_template("commentforum.html")


@app.route('/greet_commentforum1', methods=['GET', 'POST'])
def greet_commentforum1():
    # submit button has been pushed
    if request.form:
        comment1 = request.form.get("comment1")
        if comment1.__len__() != 0:  # input field has content
            return render_template("commentforum.html", comment1=comment1)
        else:
            # starting and empty input default
            return render_template("commentforum.html", comment1="World")
    else:
        return render_template("commentforum.html")

@app.route('/greet_commentforum3', methods=['GET', 'POST'])
def greet_commentforum3():
    # submit button has been pushed
    if request.form:
        comment3 = request.form.get("comment3")
        if comment3.__len__() != 0:  # input field has content
            return render_template("classrecommendations.html", comment3=comment3)
        else:
            # starting and empty input default
            return render_template("classrecommendations.html", comment3="World")
    else:
        return render_template("classrecommendations.html")


@app.route('/greet_commentforum4', methods=['GET', 'POST'])
def greet_commentforum4():
    # submit button has been pushed
    if request.form:
        comment4 = request.form.get("comment4")
        if comment4.__len__() != 0:  # input field has content
            return render_template("classrecommendations.html", comment4=comment4)
        else:
            # starting and empty input default
            return render_template("classrecommendations.html", comment4="World")
    else:
        return render_template("classrecommendations.html")


@app.route('/greet_athena', methods=['GET', 'POST'])
def greet_athena():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("athena.html", name=name)
        else:
            # starting and empty input default
            return render_template("athena.html", name="World")
    else:
        return render_template("athena.html")


@app.route('/greet_gaurish', methods=['GET', 'POST'])
def greet_gaurish():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("gaurish.html", name=name)
        else:
            # starting and empty input default
            return render_template("gaurish.html", name="World")
    else:
        return render_template("gaurish.html")


@app.route('/greet_allison', methods=['GET', 'POST'])
def greet_allison():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("allison.html", name=name)
        else:
            # starting and empty input default
            return render_template("allison.html", name="World")
    else:
        return render_template("allison.html")


@app.route('/greet_aadya', methods=['GET', 'POST'])
def greet_aadya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("aadya.html", name=name)
        else:
            # starting and empty input default
            return render_template("aadya.html", name="World")
    else:
        return render_template("aadya.html")


# hi
# connects default URL to render index.html
# @app.route('/')
# def index():
#   return render_template("greet.html")


# for input on binary
@app.route('/bits', methods=['GET', 'POST'])
def bits():
    BITS=8
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("binary.html", BITS=BITS)


# binary inputs end

# @app.route('/input_binary', methods=['GET', 'POST'])
# def input_binary():
# submit button has been pushed
#    if request.form:
#       bitnumber = request.form.get("number")
#      if len(bitnumber) != 0:  # input field has content
#        return render_template("binary.html", BITS=int(bitnumber))
# return render_template("binary.html", BITS=8)

# binary input ends


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


@app.route('/athena')
def athena():
    return render_template("athena.html")


@app.route('/allison')
def allison():
    return render_template("allison.html")


@app.route('/gaurish')
def gaurish():
    return render_template("gaurish.html")


@app.route('/aadya')
def aadya():
    return render_template("aadya.html")


@app.route('/binary')
def binary():
    BITS=8
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("binary.html", BITS=BITS)


@app.route('/ratingsystem')
def ratingsystem():
    return render_template("ratingsystem.html")


@app.route('/classrecommendations')
def classrecommendations():
    return render_template("classrecommendations.html")


@app.route('/commentforum')
def commentforum():
    return render_template("commentforum.html")


@app.route('/videos')
def videos():
    return render_template("videos.html")


@app.route('/team/')
def team():
    return render_template("team.html")


@app.route('/binarywithinput')
def binarywithinput():
    return render_template("binarywithinput.html")


# to display variable


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)