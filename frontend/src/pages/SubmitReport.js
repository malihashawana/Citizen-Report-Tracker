import React, { useState } from "react";
import api from "../api/axiosConfig";

export default function SubmitReport() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    category: "traffic"
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    await api.post("reports/", form);
    alert("Report submitted!");
  };

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Submit a Report</h2>

      <input name="title" placeholder="Title" onChange={handleChange} />
      <br /><br />

      <textarea name="description" placeholder="Description" onChange={handleChange} />
      <br /><br />

      <select name="category" onChange={handleChange}>
        <option value="traffic">Traffic</option>
        <option value="road">Road Damage</option>
        <option value="crime">Crime</option>
      </select>

      <br /><br />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}
