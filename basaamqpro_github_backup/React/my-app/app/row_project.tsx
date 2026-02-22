"use client";
import { useEffect } from "react";
import "./row_project.css";

type Project = {
  url: string;
  title: string;
  projectTitle: string;
};

export default function RowProject() {
  const projects: Project[] = [
    {
      url: "https://codepen.io/basaamqpro/pen/jErRdqp",
      title: "3D Car CSS/JS",
      projectTitle:
        "An 3D car visualization built with CSS and JavaScript, showcasing advanced CSS transforms and animations."
    },
    {
      url: "https://codepen.io/basaamqpro/pen/WbxBvxz",
      title: "3D GUN Interactive CSS/JS",
      projectTitle:
        "Requires mouse interaction and move with AWSD keys, and mouse click, built with CSS and JavaScript, showcasing advanced CSS transforms and animations"
    },
    {
      url: "https://codepen.io/basaamqpro/pen/yyJWNbG",
      title: "Mario Interactive",
      projectTitle:
        "Click on the link to see the full design..."
    },
    {
      url: "https://codepen.io/basaamqpro/pen/LEZoVoW",
      title: "HTML Design Editor",
      projectTitle:
        "An interactive HTML design editor built with CSS and JavaScript..."
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

function ProjectCard({ project }: { project: Project }) {
  const slug = project.url.split("/pen/")[1];

  return (
    <div className="project_container">
      <div className="project_description">
        <h1>{project.title}</h1>
        <p>{project.projectTitle}</p>
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