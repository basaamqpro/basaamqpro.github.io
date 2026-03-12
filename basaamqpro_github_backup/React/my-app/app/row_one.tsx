"use client";

import React from "react";
import "./row_one.css";

export default function Row1() {
  return (
    <div className="rowOne">
      <LeftColumn />
      <RightColumn />
    </div>
  );
}

function LeftColumn() {
  const scrollToBottom = () => {
    window.scrollTo({
      top: document.body.scrollHeight,
      behavior: "smooth"
    });
  };

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
          <button onClick={scrollToBottom} className="Hire contactbutton">
            Hire Me!
          </button>

          <a href="/basaamq_cv.pdf">
            <button className="Resume contactbutton">My Resume</button>
          </a>
        </div>

      </div>
    </div>
  );
}

function RightColumn() {
  return (
    <div className="right-column">

     
    <div id="youtube_video_container">
      <iframe
        className="youtube_video"
        src="https://www.youtube.com/embed/IC0wcKV5NXk"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen
      ></iframe>
    </div>
    </div>
  );
}