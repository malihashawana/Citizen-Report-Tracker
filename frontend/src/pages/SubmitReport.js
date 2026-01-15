import React, { useState } from "react";

export default function SubmitReport() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    category: ""
  });

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Submit a Report</h2>

      <input placeholder="Title" />
      <br /><br />

      <textarea placeholder="Description"></textarea>
      <br /><br />

      <select>
        <option>Traffic</option>
        <option>Road Damage</option>
        <option>Crime</option>
      </select>

      <br /><br />
      <button>Submit</button>
    </div>
  );
}
