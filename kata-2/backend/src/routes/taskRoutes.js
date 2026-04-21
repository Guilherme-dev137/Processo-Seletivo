import { Router } from "express";
import {
  deleteTaskById,
  getTasks,
  patchTask,
  postTask
} from "../controllers/taskController.js";

const router = Router();

router.get("/tasks", getTasks);
router.post("/tasks", postTask);
router.patch("/tasks/:id", patchTask);
router.delete("/tasks/:id", deleteTaskById);

export default router;
