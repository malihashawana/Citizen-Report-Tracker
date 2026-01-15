import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import SubmitReport from "./pages/SubmitReport";
import ReportList from "./pages/ReportList";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/report" element={<SubmitReport />} />
        <Route path="/reports" element={<ReportList />} />
      </Routes>
    </Router>
  );
}

export default App;
