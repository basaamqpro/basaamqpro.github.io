"use client"; // <-- Add this line at the very top

import React from "react";  
import './row_one.css';

export default function Row1() {
  return (
    <div className="rowOne">
        <LeftColumn />
        <RightColumn />
    </div>
  );
}


function LeftColumn() {
    return (
        <div className="left-column">
            <div className="container">
            <div className="row0 row">
                <h1 className="hello">Hello</h1>
                <div className="dot"></div>
            </div>
            <div className="row1 row">
                <div className="line"></div>
                <h1 className="name">I'm Basaam Q</h1>
            </div>
            <div className="row2">
                <h1 className="Entry">Entry Web Developer</h1>
            </div>
            <div className="row3 row">
                <button className="Hire contactbutton">Hire Me!</button>
                <button className="Resume contactbutton">My Resume</button>
            </div>
            </div>
        </div>
    );
}

function RightColumn() {
    return (
        <div className="right-column">
           <img src="/basaam.png" alt="Profile Picture" className="profile_image" />
        </div>
    );
}