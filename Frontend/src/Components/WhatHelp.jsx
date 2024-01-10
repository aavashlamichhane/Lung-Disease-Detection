import "./pages/AboutUs.css";

const WhatHelp = ({ closeModal }) => {
  return (
    <>
      <div className="MainWrapper" onClick={() => closeModal()}>
        <div className="ModelContent">
          <h1>What We Do</h1>
          <p>We leverage advanced technology to enhance respiratory health. Our mission is to provide accurate and timely detection of pneumonia infection through cutting-edge technology. We prioritize the well-being of individuals by providing accessible and reliable tools for lung health assessment. Our services have a direct impact on patient outcomes, enabling early intervention and improving the overall prognosis for individuals with lung diseases.</p>
          <button id="ViewMore" onClick={() => closeModal()}>
            ViewMore
          </button>
        </div>
      </div>
    </>
  );
};

export default WhatHelp;
