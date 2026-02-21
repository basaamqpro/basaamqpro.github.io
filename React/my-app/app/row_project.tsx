"use client";
import { useEffect } from "react";

export default function RowProject() {
  const projects = [
    {
      url: "https://codepen.io/basaamqpro/pen/jErRdqp",
      title: "Untitled"
    },
    {
      url: "https://codepen.io/basaamqpro/pen/WbxBvxz",
      title: "3D GUN CSS/JS"
    },
    {
      url: "https://codepen.io/basaamqpro/pen/yyJWNbG",
      title: "Mario Interactive"
    },
    {
      url: "https://codepen.io/basaamqpro/pen/LEZoVoW",
      title: "Untitled"
    }
  ];

  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://public.codepenassets.com/embed/index.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);

  return (
    <div className="rowProjects">
      {projects.map((project, index) => (
        <ProjectCard key={index} project={project} />
      ))}
    </div>
  );
}

function ProjectCard({ project }) {
  const slug = project.url.split("/pen/")[1];

  return (
    <div className="project_container">
      <div className="project_description">
        <h1>Projects</h1>
        <p>
          Here are some of my recent projects. Click on the links to see more details.
        </p>
      </div>

      <div className="project_element">
        <p
          className="codepen"
          data-height="300"
          data-theme-id="dark"
          data-default-tab="js,result"
          data-slug-hash={slug}
          data-pen-title={project.title}
          data-user="basaamqpro"
          style={{ height: "300px" }}
        />
      </div>
    </div>
  );
}