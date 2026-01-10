import shop from "shop.jsx";

const products = [
  {
    id: 1,
    name: "Wooden Keychains",
    price: 0,
    image: "keychains.png",
  },
  {
    id: 2,
    name: "Warli Hand Painted Panels",
    price: 0,
    image: "panels.png",
  },
  {
    id: 3,
    name: "Leather Handbags",
    price: 0,
    image: "handbags.png",
  },
  {
    id: 4,
    name: "Jute Bags",
    price: 0,
    image: "bags.png",
  },
  {
    id: 5,
    name: "Leather Wallets",
    price: 0,
    image: "wallets.JPG",
  },
  {
    id: 6,
    name: "Bamboo Photo Frame",
    price: 0,
    image: "bamboo-frame.png",
  },
  {
    id: 7,
    name: "File Holder by Jute",
    price: 0,
    image: "holder.JPG",
  },
   {
    id: 8,
    name: "Wall Hangings",
    price: 0,
    image: "hangings.JPG",
  },
  {
    id: 9,
    name: "Clay Pottery",
    price: 0,
    image: "pottery.JPG",
  },

];

function Shop({ addToCart }) {
  return (
    <div style={{ padding: "30px" }}>
      <h2>Shop Handmade Items</h2>

      <div style={{ display: "flex", gap: "20px" }}>
        {products.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid #ccc",
              padding: "15px",
              width: "200px",
              textAlign: "center",
            }}
          >
            <img
              src={item.image}
              alt={item.name}
              style={{ width: "100%", height: "150px" }}
            />
            <h4>{item.name}</h4>
            <p>${item.price}</p>
            <button onClick={() => addToCart(item)}>
              Add to Cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
