from flask import Flask, render_template, request, redirect, session
from modelos.user import User
from controlador.product_controller import ProductController

# Inicializar Flask con carpetas personalizadas
app = Flask(
    __name__,
    template_folder="plantillas",   # HTML
    static_folder="estilos"         # CSS/JS
)
app.secret_key = "clave_secreta"

# ----------------------
# LOGIN
# ----------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.login(username, password)
        if user:
            session["user"] = username
            return redirect("/menu")
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    return render_template("login.html")

# ----------------------
# MENÚ PRINCIPAL
# ----------------------
@app.route("/menu")
def menu():
    if "user" in session:
        return render_template("menu.html")
    return redirect("/")

# ----------------------
# LISTAR PRODUCTOS (CRUD)
# ----------------------
@app.route("/products")
def products():
    if "user" not in session:
        return redirect("/")
    products = ProductController.get_products()
    return render_template("products.html", products=products, product=None)

# ----------------------
# CREAR O ACTUALIZAR PRODUCTO
# ----------------------
@app.route("/products/save", methods=["POST"])
def save_product():
    if "user" not in session:
        return redirect("/")
    product_id = request.form.get("id")
    name = request.form["name"]
    description = request.form["description"]
    price = float(request.form["price"])
    if product_id:
        ProductController.update_product(product_id, name, description, price)
    else:
        ProductController.create_product(name, description, price)
    return redirect("/products")

# ----------------------
# EDITAR PRODUCTO
# ----------------------
@app.route("/products/edit/<int:id>")
def edit_product(id):
    if "user" not in session:
        return redirect("/")
    products = ProductController.get_products()
    product = ProductController.get_product(id)
    class P: pass
    p = P()
    p.id = product[0]
    p.name = product[1]
    p.description = product[2]
    p.price = product[3]
    return render_template("products.html", products=products, product=p)

# ----------------------
# ELIMINAR PRODUCTO
# ----------------------
@app.route("/products/delete/<int:id>")
def delete_product(id):
    if "user" in session:
        ProductController.delete_product(id)
    return redirect("/products")

# ----------------------
# DESPLIEGUE DE PRODUCTOS (solo ver)
# ----------------------
@app.route("/products/view")
def view_products():
    if "user" not in session:
        return redirect("/")
    products = ProductController.get_products()
    return render_template("view_products.html", products=products)

# ----------------------
# CERRAR SESIÓN
# ----------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ----------------------
# EJECUTAR APP
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
