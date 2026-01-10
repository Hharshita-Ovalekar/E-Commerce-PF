import Cart from "cart.jsx";

function Cart({ cart, removeFromCart }) {
  const total = cart.reduce(
    (sum, item) => sum + item.price * item.qty,
    0
  );

  return (
    <div style={{ padding: "30px" }}>
      <h2>Cart</h2>

      {cart.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <>
          {cart.map((item) => (
            <div
              key={item.id}
              style={{
                display: "flex",
                alignItems: "center",
                marginBottom: "10px",
                borderBottom: "1px solid #ddd",
                paddingBottom: "10px",
              }}
            >
              <img
                src={item.image}
                alt={item.name}
                style={{ width: "60px", marginRight: "10px" }}
              />
              <div>
                <p>{item.name}</p>
                <p>
                  ${item.price} × {item.qty}
                </p>
              </div>
              <button
                onClick={() => removeFromCart(item.id)}
                style={{ marginLeft: "auto" }}
              >
                Remove
              </button>
            </div>
          ))}

          <h3>Total: ${total}</h3>
          <button>Checkout</button>
        </>
      )}
    </div>
  );
}


