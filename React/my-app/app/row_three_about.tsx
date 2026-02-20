"use client"; // <-- Add this line at the very top

import React from "react";  
import './row_three_about.css';

export default function Row_three_about() {
  return (
    <div className="rowthree">
        <LeftColumn />
        <RightColumn />
    </div>
  );
}


function LeftColumn() {
    return (
        <div className="about_icons_section"> 
        <div >
          <div className="vertical_column_section">
            <div className="border_left"></div>
            <div className="border_bullet"></div>
            <div className="border_left"></div>
            <div className="border_bullet"></div>
            <div className="border_left"></div>
          </div>
       </div>


       <div className="skills">
        <div className="icon_skills">
            <img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png" alt="html5 icon" className="skill_icon" />
            <h1>Website Development</h1>
        </div>
        <div className="icon_skills">
            <img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png" alt="html5 icon" className="skill_icon" />
            <h1>App Development</h1>
        </div>
        <div className="icon_skills">
            <img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png" alt="html5 icon" className="skill_icon" />
            <h1>Website Hosting</h1>
        </div>
       </div>

       </div>

    );
}

function RightColumn() {
    return (
         <div className="About_">
        <h1>About Me</h1>
        <p>I started my coding journey with a passion for creating beautiful and functional websites.
          I have experience in HTML, CSS, JavaScript, and React. I'm always looking to learn new technologies and improve my skills.
        </p>


       <div className="data_row">


        <div className="data_column">
          <div id="row_number">
          <h1>20</h1>
          <p>+</p>
        </div>
        <div className="smallerText">
          Completed Projects
        </div>
        </div>

         <div className="data_column">
          <div id="row_number">
          <h1>2</h1>
          <p>+</p>
        </div>
        <div className="smallerText">
          Satisfied Clients
        </div>
        </div>


         <div className="data_column">
          <div id="row_number">
          <h1>4</h1>
          <p>+</p>
        </div>
        <div className="smallerText">
          Years of Coding
        </div>
        </div>
     </div>
       </div>
    );
}