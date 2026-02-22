"use client";

import "./row_footer_css.css";

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  };

  return (
    <footer className="footer">
      <div id="contact"className="footer-content">

        <div className="footer-left">
          <h2>Basaam Qasem</h2>
          <p>Frontend Developer • Creative Engineer</p>
        </div>

        <div className="footer-center">
          <a
            href="mailto:basaamqpro@gmail.com"
            className="footer-btn"
          >
            📩 Email Me
          </a>

          <p className="phone">📱 07497467360</p>

          <button onClick={scrollToTop} className="footer-btn secondary">
            ↑ About
          </button>
        </div>

        <div className="footer-right">
          <a
            href="https://github.com/basaamqpro"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
              alt="GitHub"
              className="icon"
            />
          </a>

          <a
            href="https://github.com/kiteqio?tab=overview&from=2024-12-01&to=2024-12-31"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg"
              alt="Old GitHub"
              className="icon"
            />
          </a>
        </div>

      </div>
    </footer>
  );
}