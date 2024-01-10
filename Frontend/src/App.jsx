import React from "react";
import Home from "./Components/pages/Home";
import Result from "./Components/pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import AboutUs from "./Components/pages/AboutUs";
import ContactUs from "./Components/pages/ContactUs";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/result" element={<Result />} />
          <Route path="/" element={<Home />} />
          <Route path="AboutUs" element={<AboutUs />} />
          <Route path="Contactus" element={<ContactUs />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}
