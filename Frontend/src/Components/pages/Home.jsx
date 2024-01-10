import React from "react";
import "./Home.css";

export default function Home() {
  return (
    <div className="HomePage">
      <div className="VideoBackground">
        <video autoPlay loop muted>
          <source src="/BackVideo.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div className="Overall">
        <div className="Container">
          <div className="textbox">
            <h1>
              Empowering Respiratory Resilience: Detecting Lung Infections,
              Defining Tomorrow's Health.
            </h1>
            <p className="Paragraph">Precise Way Of Finding The Infection.</p>
         
          <a className="Button" href="/result">
            Let's Begin
            
          </a>
          </div>
        </div>
      </div>
    </div>
  );
}
