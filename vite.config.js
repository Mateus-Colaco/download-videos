import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "node:path";
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: path.join("./dist/"),
    manifest: "manifest.json",
    assetsDir: "bundled",
    emptyOutDir: true,
    copyPublicDir: false,
  },
})
