"use client";

import React from "react";
import Row1 from "./row_one";
import Row2Menu from "./row_two_menu";
import RowThreeAbout from "./row_three_about";
import RowProjects from "./row_project";
import Footer from "./row_footer";

// Optional: If you want a small counter demo
function Counter() {
  const [count, setCount] = React.useState(0);

  return (
    <div className="flex flex-col items-center">
      <p className="text-xl mb-2 text-black dark:text-white">Count: {count}</p>
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        onClick={() => setCount(count + 1)}
      >
        Increment
      </button>
    </div>
  );
}

export default function Home() {
  return (
    <main>
      <Row1 />
      <Row2Menu />
      <RowThreeAbout />
      <RowProjects />
      <Footer />
      <Counter /> {/* Optional demo */}
    </main>
  );
}