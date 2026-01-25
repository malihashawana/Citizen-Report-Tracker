import React, { useEffect, useState } from "react";
import api from "../api/axiosConfig";
import ReportCard from "../components/ReportCard";

export default function ReportList() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    api.get("reports/").then((res) => setReports(res.data));
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Community Reports</h2>

      {reports.map((report) => (
        <ReportCard key={report.id} report={report} />
      ))}
    </div>
  );
}
