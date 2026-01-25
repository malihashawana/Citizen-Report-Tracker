import React from "react";

export default function SeverityBadge({ score }) {
  let label = "Low";
  let color = "green";

  if (score === 1) {
    label = "High";
    color = "red";
  }

  return (
    <span style={{
      background: color,
      color: "white",
      padding: "4px 8px",
      borderRadius: "6px",
      fontSize: "12px"
    }}>
      {label} Risk
    </span>
  );
}
