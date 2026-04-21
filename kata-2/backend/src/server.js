import express from "express";
import cors from "cors";
import taskRoutes from "./routes/taskRoutes.js";

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.use("/api", taskRoutes);

app.get("/health", (_req, res) => {
  res.json({ status: "ok" });
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
