import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  images: { unoptimized: true },
  basePath: "/basaamqpro.github.io", // <-- add this
};

export default nextConfig;