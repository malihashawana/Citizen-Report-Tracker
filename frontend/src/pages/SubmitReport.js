import React, { useState } from "react";
import api from "../api/axiosConfig";
import SeverityBadge from "../components/SeverityBadge";

export default function SubmitReport() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    category: "traffic",
  });

  const [riskScore, setRiskScore] = useState(null);

  const handleChange = async (e) => {
    const updated = { ...form, [e.target.name]: e.target.value };
    setForm(updated);

    if (e.target.name === "description" && e.target.value.length > 5) {
      const res = await api.post("ai/analyze/", {
        text: e.target.value,
      });
      setRiskScore(res.data.risk_score);
    }
  };

  const handleSubmit = async () => {
    await api.post("reports/", {
      ...form,
      risk_score: riskScore ?? 0,
    });
    alert("Report submitted successfully!");
  };

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Submit a Report</h2>

      <input
        name="title"
        placeholder="Title"
        onChange={handleChange}
      /><br /><br />

      <textarea
        name="description"
        placeholder="Describe the issue"
        onChange={handleChange}
      /><br /><br />

      {riskScore !== null && <SeverityBadge score={riskScore} />}
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
