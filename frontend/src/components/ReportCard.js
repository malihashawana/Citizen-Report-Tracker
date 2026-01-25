import React from "react";
import SeverityBadge from "./SeverityBadge";

export default function ReportCard({ report }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      padding: "1rem",
      marginBottom: "1rem",
      borderRadius: "8px"
    }}>
      <h3>{report.title}</h3>
      <SeverityBadge score={report.risk_score} />
      <p>{report.description}</p>
      <small>
        Category: {report.category} | Status: {report.status}
      </small>
    </div>
  );
}
