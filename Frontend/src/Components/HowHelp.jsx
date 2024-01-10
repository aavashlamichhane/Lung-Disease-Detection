import "./pages/AboutUs.css";

const HowHelp = ({ closeModal2 }) => {
  return (
    <>
      <div className="MainWrapper" onClick={() => closeModal2()}>
        <div className="ModelContent">
          <h1>How Can We Help You ?</h1>
          <p> <ul><li> The project incorporates machine learning techniques to automatically analyze chest X-ray images for the detection of lung infections.
</li></ul>
<ul><li> The project utilizes machine learning techniques for accurate diagnosis, highlighting areas likely to be affected by pneumonia in chest X-ray images.</li> </ul>
                    
                </p>
          <button id="ViewMore" onClick={() => closeModal2()}>
            ViewMore
          </button>
        </div>
      </div>
    </>
  );
};

export default HowHelp;
