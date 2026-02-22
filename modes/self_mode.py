import streamlit as st
from database import add_order
from components.wallet_engine import deduct_wallet

# -------------------------
# Sample Restaurant Data
# -------------------------

restaurants = [
    {
        "name": "Pizza Palace",
        "rating": "4.5 ⭐",
        "delivery_time": "30 mins",
        "image": "https://images.unsplash.com/photo-1601924582975-7e7d3d4b2d02",
        "items": [
            {
                "name": "Cheese Pizza",
                "price": 250,
                "image": "https://images.unsplash.com/photo-1594007654729-407eedc4be65"
            },
            {
                "name": "Veg Supreme",
                "price": 300,
                "image": "https://images.unsplash.com/photo-1548365328-9f547fb0953a"
            }
        ]
    },
    {
        "name": "Biryani House",
        "rating": "4.3 ⭐",
        "delivery_time": "25 mins",
        "image": "https://images.unsplash.com/photo-1604908176997-431c3b6d38be",
        "items": [
            {
                "name": "Chicken Biryani",
                "price": 220,
                "image": "https://images.unsplash.com/photo-1633945274309-2c16c9682bce"
            },
            {
                "name": "Veg Biryani",
                "price": 180,
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
            }
        ]
    }
]

# -------------------------
# Self Mode UI
# -------------------------

def self_home():
    st.header("🍽 Explore Restaurants")

    # Initialize Cart
    if "cart" not in st.session_state:
        st.session_state.cart = []

    for restaurant in restaurants:

        st.markdown("---")
        st.subheader(restaurant["name"])
        st.write(f"{restaurant['rating']} • {restaurant['delivery_time']}")
        st.image(restaurant["image"], use_column_width=True)

        cols = st.columns(2)

        for i, item in enumerate(restaurant["items"]):

            with cols[i % 2]:

                st.image(item["image"], use_column_width=True)
                st.markdown(f"### {item['name']}")
                st.write(f"₹ {item['price']}")

                qty = st.number_input(
                    f"Quantity - {item['name']}",
                    min_value=1,
                    max_value=5,
                    value=1,
                    key=f"{restaurant['name']}_{item['name']}"
                )

                if st.button(f"Add to Cart - {item['name']}"):
                    st.session_state.cart.append({
                        "name": item["name"],
                        "price": item["price"],
                        "qty": qty
                    })
                    st.success(f"{item['name']} added to cart!")

    # -------------------------
    # Cart Section
    # -------------------------

    if st.session_state.cart:

        st.markdown("---")
        st.header("🛒 Your Cart")

        total = 0

        for order in st.session_state.cart:
            item_total = order["price"] * order["qty"]
            total += item_total
            st.write(f"{order['name']} x {order['qty']} = ₹ {item_total}")

        st.subheader(f"Total: ₹ {total}")

        if st.button("Proceed to Payment"):

            new_balance = deduct_wallet(st.session_state.wallet, total)

            if new_balance is not None:

                st.session_state.wallet = new_balance

                for order in st.session_state.cart:
                    add_order(
                        st.session_state.user,
                        order["name"],
                        order["price"] * order["qty"]
                    )

                st.success("🎉 Order Placed Successfully!")
                st.session_state.cart = []

            else:
                st.error("❌ Insufficient Wallet Balance")
