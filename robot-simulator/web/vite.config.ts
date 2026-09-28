import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, ".", "ROBOT_");
  return {
    plugins: [react()],
    server: {
      port: 5173,
      proxy: { "/api": env.ROBOT_API_URL ?? "http://127.0.0.1:8000" },
    },
    build: { chunkSizeWarningLimit: 800 },
  };
});
