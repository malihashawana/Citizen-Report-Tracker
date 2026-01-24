import React, { useEffect, useState } from "react";
import api from "../api/axiosConfig";

export default function ReportList() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    api.get("reports/").then(res => setReports(res.data));
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Community Reports</h2>

      {reports.map(r => (
        <div key={r.id} style={{ border: "1px solid #ccc", margin: "10px" }}>
          <h4>{r.title}</h4>
          <p>{r.description}</p>
          <small>{r.category}</small>
        </div>
      ))}
    </div>
  );
}
