from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

# =======================
# Inventory Service
# =======================
inventory_bp = Blueprint('inventory', __name__)

# Sample in-memory inventory data
inventory_data = [
    {"sku": "A123", "name": "Widget", "quantity": 100},
    {"sku": "B456", "name": "Gadget", "quantity": 250},
]

@inventory_bp.route("/inventory", methods=["GET"])
def list_inventory():
    return jsonify(inventory_data)

@inventory_bp.route("/inventory/<sku>", methods=["GET"])
def get_inventory_item(sku):
    item = next((i for i in inventory_data if i["sku"] == sku), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@inventory_bp.route("/inventory/<sku>", methods=["PUT"])
def update_inventory_item(sku):
    payload = request.json
    for item in inventory_data:
        if item["sku"] == sku:
            item["quantity"] = payload.get("quantity", item["quantity"])
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# =======================
# Order Service
# =======================
order_bp = Blueprint('order', __name__)

# Sample in-memory orders
orders_data = [
    {"order_id": 1, "items": [{"sku": "A123", "quantity": 2}], "status": "pending"},
]

@order_bp.route("/orders", methods=["GET"])
def list_orders():
    return jsonify(orders_data)

@order_bp.route("/orders", methods=["POST"])
def create_order():
    payload = request.json
    new_order = {
        "order_id": len(orders_data) + 1,
        "items": payload["items"],
        "status": "pending",
    }
    orders_data.append(new_order)
    return jsonify(new_order), 201

@order_bp.route("/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    payload = request.json
    for order in orders_data:
        if order["order_id"] == order_id:
            order["status"] = payload.get("status", order["status"])
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

# =======================
# User Service
# =======================
user_bp = Blueprint('user', __name__)

# Sample in-memory users
users_data = [
    {"user_id": 1, "name": "Alice", "role": "admin"},
    {"user_id": 2, "name": "Bob", "role": "picker"},
]

@user_bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(users_data)

@user_bp.route("/users", methods=["POST"])
def create_user():
    payload = request.json
    new_user = {
        "user_id": len(users_data) + 1,
        "name": payload["name"],
        "role": payload.get("role", "picker"),
    }
    users_data.append(new_user)
    return jsonify(new_user), 201

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users_data if u["user_id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# =======================
# Health Endpoint
# =======================
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

# =======================
# Register Blueprints
# =======================
app.register_blueprint(inventory_bp)
app.register_blueprint(order_bp)
app.register_blueprint(user_bp)

# =======================
# Run
# =======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
