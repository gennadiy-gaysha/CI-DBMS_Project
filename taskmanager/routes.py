from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    #     Whenever we call this function by clicking the navbar link for Categories, it will query
    # the database and retrieve all records from this table, then sort them by the category name.
    categories = list(Category.query.order_by(Category.category_name).all())
   #  Then pass this variable into our rendered template,
   #  so that we can use this data to display everything to our users.
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
