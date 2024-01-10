import React, { useState } from "react";
import axios from "axios";
import NavBar from "../NavBar.jsx";
import "./Result.css";
import "../NavBar.css";

export default function Result() {
  const [imagePreview, setImagePreview] = useState(null);
  const [pred, setPred] = useState(null);
  const [conf, setConf] = useState(null);
  const [resultImage, setResultImage] = useState(null); // Add this line to define resultImage state

  const handleImageChange = async (e) => {
    console.log("Handling image change");

    const file = e.target.files[0];

    if (file) {
      const reader = new FileReader();

      reader.onloadend = () => {
        // Set the image preview using the FileReader result
        setImagePreview(reader.result);
      };

      // Read the content of the selected file as a data URL
      reader.readAsDataURL(file);

      const formData = new FormData();
      formData.append("image", file);

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/upload",
          formData
        );

        if (response.status === 200) {
          console.log("Image uploaded successfully");

          // Check the content type of the response
          const contentType = response.headers["content-type"];

          if (contentType.startsWith("image")) {
            // If the response is an image, convert it to a data URL and set it in the state
            const imageBlob = new Blob([response.data], { type: contentType });
            const imageUrl = URL.createObjectURL(imageBlob);
            console.log("Image Returned");
            setResultImage(imageUrl);
          } else {
            console.log("Received JSON response:", response.data);
            // setPred(response.data.pred);
            if(response.data.pred==1){
              setPred("Pneumonia");
            }
            else if(response.data.pred==0){
              setPred("Normal");
            }
            else{
              setPred("Eroor");
            }
            setResultImage(response.data.url);
            setConf(response.data.conf);
          }
        } else {
          console.error("Failed to upload image");
        }
      } catch (error) {
        console.error("Error uploading image", error);
      }
    }
  };

  return (
    <>
      <NavBar />
      <div className="VideoBackground">
        <video autoPlay loop muted>
          <source src="/BackVideo.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div className="Wrap">
        <div className="Inside">
          <div className="Input_side">
            <h3>UPLOAD IMAGE</h3>

            <label className="UpButtonLabel">
              Upload File
              <input
                type="file"
                className="UpButton"
                onChange={handleImageChange}
              />
            </label>

            {/* Display image preview if available */}
            {imagePreview ? (
              <div className="Holder">
                <h2>Image Preview:</h2>
                <img
                  src={imagePreview}
                  alt="Preview"
                  style={{ maxWidth: "100%", maxHeight: "80%",marginBottom: "5%" }}
                />
              </div>
            ) : (
              <div className="Holder">
                {/* Content of the empty box */}
                {/* You can customize the appearance of the empty box her */}
              </div>
            )}
          </div>

          <div className="Output_side">
            {/* Display result image if available */}
            {resultImage && (
              <div className="Holder">
                <h2>Result Image:</h2>
                <h4>Prediction = "{pred}", Confidence = {conf}%</h4>
                <img
                  src={`http://127.0.0.1:8080/${resultImage}`}
                  alt="Result"
                  style={{ maxWidth: "100%", maxHeight: "80%",marginBottom: "5%" }}
                />
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}


