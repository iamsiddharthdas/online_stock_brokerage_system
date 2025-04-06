import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const initialStocks = {
  TCS: { name: "Tata Consultancy Services", price: 3500 },
  INFY: { name: "Infosys", price: 1400 },
  RELIANCE: { name: "Reliance Industries", price: 2600 },
  HDFC: { name: "HDFC Bank", price: 1650 },
};

export default function StockBrokerageApp() {
  const [users, setUsers] = useState({});
  const [username, setUsername] = useState("");
  const [currentUser, setCurrentUser] = useState(null);
  const [stocks, setStocks] = useState(initialStocks);

  const createUser = () => {
    if (users[username]) return alert("User already exists");
    const newUser = { balance: 10000, portfolio: {} };
    setUsers({ ...users, [username]: newUser });
    setCurrentUser(username);
  };

  const buyStock = (symbol, quantity) => {
    const stock = stocks[symbol];
    const cost = stock.price * quantity;
    if (users[currentUser].balance < cost) return alert("Not enough balance");
    const updatedUser = { ...users[currentUser] };
    updatedUser.balance -= cost;
    updatedUser.portfolio[symbol] = (updatedUser.portfolio[symbol] || 0) + quantity;
    setUsers({ ...users, [currentUser]: updatedUser });
  };

  const sellStock = (symbol, quantity) => {
    const updatedUser = { ...users[currentUser] };
    if ((updatedUser.portfolio[symbol] || 0) < quantity) return alert("Not enough shares");
    updatedUser.portfolio[symbol] -= quantity;
    updatedUser.balance += stocks[symbol].price * quantity;
    setUsers({ ...users, [currentUser]: updatedUser });
  };

  const updatePrices = () => {
    const updated = {};
    for (const symbol in stocks) {
      const change = 1 + (Math.random() * 0.1 - 0.05);
      updated[symbol] = {
        ...stocks[symbol],
        price: parseFloat((stocks[symbol].price * change).toFixed(2)),
      };
    }
    setStocks(updated);
  };

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📈 Online Stock Brokerage System</h1>

      {!currentUser && (
        <div className="flex gap-2 mb-4">
          <Input
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Button onClick={createUser}>Create Account</Button>
        </div>
      )}

      {currentUser && (
        <div>
          <h2 className="text-xl font-semibold mb-2">Welcome, {currentUser}!</h2>
          <p className="mb-4">💰 Balance: ₹{users[currentUser].balance.toFixed(2)}</p>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            {Object.entries(stocks).map(([symbol, stock]) => (
              <Card key={symbol}>
                <CardContent className="p-4">
                  <h3 className="text-lg font-semibold">{symbol}</h3>
                  <p>{stock.name}</p>
                  <p>₹{stock.price}</p>
                  <div className="flex gap-2 mt-2">
                    <Button size="sm" onClick={() => buyStock(symbol, 1)}>Buy</Button>
                    <Button size="sm" onClick={() => sellStock(symbol, 1)}>Sell</Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          <h3 className="text-lg font-semibold mb-2">📊 Portfolio</h3>
          <div className="bg-gray-100 rounded-lg p-4 mb-4">
            {Object.entries(users[currentUser].portfolio).length === 0 ? (
              <p>No stocks yet.</p>
            ) : (
              <ul>
                {Object.entries(users[currentUser].portfolio).map(([symbol, qty]) => (
                  <li key={symbol}>{symbol}: {qty} shares</li>
                ))}
              </ul>
            )}
          </div>

          <Button onClick={updatePrices}>🔄 Update Stock Prices</Button>
        </div>
      )}
    </div>
  );
}
