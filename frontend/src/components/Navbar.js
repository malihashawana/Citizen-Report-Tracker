import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{
      background: "#222",
      color: "white",
      padding: "1rem",
      display: "flex",
      gap: "20px"
    }}>
      <h3>Citizen Report Tracker</h3>
      <Link to="/" style={{ color: "white" }}>Home</Link>
      <Link to="/report" style={{ color: "white" }}>Submit</Link>
      <Link to="/reports" style={{ color: "white" }}>Reports</Link>
    </nav>
  );
}
