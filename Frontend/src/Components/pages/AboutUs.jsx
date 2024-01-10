import React, { useState } from "react";
import "./AboutUs.css";
import { motion } from "framer-motion";
import HowHelp from "../HowHelp";
import WhatHelp from "../WhatHelp";

export default function AboutUs() {
  const [showModal, setShowModel] = useState(false);
  const [showModal2, setShowModel2] = useState(false);

  const closeModal = () => setShowModel(false);
  const closeModal2 = () => setShowModel2(false);

  return (
    <>
      <div className="VideoBackground">
        <video autoPlay loop muted>
          <source src="/BackVideo.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>

      <div className="Wrap">
        <div className="layout">
          {showModal && <WhatHelp closeModal={closeModal} />}
          {showModal2 && <HowHelp closeModal2={closeModal2} />}

          <div className="AboutUsOverall">
            <motion.div
              initial={{ x: -100 }}
              animate={{ x: 0 }}
              transition={{ duration: 1 }}
              className="Mid"
            >
              <p>About Us</p>
            </motion.div>

            <div className="Bottom">
              <motion.div
                initial={{ x: -200 }}
                animate={{ x: 0 }}
                transition={{ duration: 1 }}
                className="AboutUs1"
              >
                <h1>What We Do</h1>
                <div className="paragraph">
                  <p>
                    We leverage advanced technology to enhance respiratory
                    health. Our mission is to provide accurate and timely
                    detection of pneumonia infection through cutting-edge
                    technology. We prioritize the well-being of individuals by
                    providing accessible and reliable tools for lung health
                    assessment. Our services have a direct impact on patient
                    outcomes, enabling early intervention and improving the
                    overall prognosis for individuals with lung diseases.
                  </p>
                </div>
                <button
                  class="Viewmore "
                  id="ViewMore1"
                  onClick={() => setShowModel(true)}
                >
                  View More
                </button>
              </motion.div>
              <motion.div
                initial={{ x: -400 }}
                animate={{ x: 0 }}
                transition={{ duration: 1 }}
                className="AboutUs1"
              >
                <h1>How We Can Help</h1>
                <div className="paragraph">
                  <p>
                    <ul>
                      <li>
                        {" "}
                        The project incorporates machine learning techniques to
                        automatically analyze chest X-ray images for the
                        detection of lung infections.
                      </li>
                    </ul>
                    <ul>
                      <li>
                        {" "}
                        The project utilizes machine learning techniques for
                        accurate diagnosis, highlighting areas likely to be
                        affected by pneumonia in chest X-ray images.
                      </li>{" "}
                    </ul>
                  </p>
                </div>
                <button
                  class="Viewmore"
                  id="ViewMore2"
                  onClick={() => setShowModel2(true)}
                >
                  ViewMore
                </button>
              </motion.div>
            </div>
          </div>
        </div>{" "}
      </div>
    </>
  );
}
