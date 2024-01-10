import React from "react";
import "./NavBar.css";

export default function NavBar() {
  const handleLogoClick = () => {
    window.location.href = "/";
  };

  return (
    <div className="Navbar">
      <div className="logoContainer" onClick={handleLogoClick}>
        <img className="logo" src="/public/LogoLDD.png" alt="Logo" />
        <span className="logo-text">Lungs Disease Detection</span>
      </div>
      <div className="NavLinks">
        <a href="/">Home</a>
        <a href="AboutUs">About Us</a>
        <a href="ContactUs">Contact Us</a>
      </div>
    </div>
  );
}
