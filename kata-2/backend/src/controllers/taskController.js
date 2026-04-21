import {
  createTask,
  listTasks,
  removeTask,
  updateTask
} from "../models/taskModel.js";

const VALID_FILTERS = new Set(["Todas", "Pendentes", "Concluidas"]);
const VALID_STATUS = new Set(["Pendente", "Concluida"]);
const VALID_PRIORITIES = new Set(["Baixa", "Media", "Alta"]);

function normalizeText(value) {
  return typeof value === "string" ? value.trim() : "";
}

export function getTasks(req, res) {
  const filter = req.query.filter || "Todas";

  if (!VALID_FILTERS.has(filter)) {
    return res.status(400).json({
      message: "Filtro invalido. Use Todas, Pendentes ou Concluidas."
    });
  }

  return res.json(listTasks(filter));
}

export function postTask(req, res) {
  const title = normalizeText(req.body.title);
  const description = normalizeText(req.body.description);
  const priority = req.body.priority || "Media";

  if (!title) {
    return res.status(400).json({
      message: "O titulo da tarefa e obrigatorio."
    });
  }

  if (!VALID_PRIORITIES.has(priority)) {
    return res.status(400).json({
      message: "Prioridade invalida. Use Baixa, Media ou Alta."
    });
  }

  const task = createTask({
    title,
    status: "Pendente",
    description,
    priority
  });

  return res.status(201).json(task);
}

export function patchTask(req, res) {
  const id = Number(req.params.id);
  const title =
    req.body.title === undefined ? undefined : normalizeText(req.body.title);
  const description =
    req.body.description === undefined
      ? undefined
      : normalizeText(req.body.description);
  const { status } = req.body;
  const { priority } = req.body;

  if (Number.isNaN(id)) {
    return res.status(400).json({
      message: "Identificador de tarefa invalido."
    });
  }

  if (title !== undefined && !title) {
    return res.status(400).json({
      message: "O titulo da tarefa nao pode ficar vazio."
    });
  }

  if (status !== undefined && !VALID_STATUS.has(status)) {
    return res.status(400).json({
      message: "Status invalido. Use Pendente ou Concluida."
    });
  }

  if (priority !== undefined && !VALID_PRIORITIES.has(priority)) {
    return res.status(400).json({
      message: "Prioridade invalida. Use Baixa, Media ou Alta."
    });
  }

  const task = updateTask(id, { title, description, status, priority });

  if (!task) {
    return res.status(404).json({
      message: "Tarefa nao encontrada."
    });
  }

  return res.json(task);
}

export function deleteTaskById(req, res) {
  const id = Number(req.params.id);

  if (Number.isNaN(id)) {
    return res.status(400).json({
      message: "Identificador de tarefa invalido."
    });
  }

  const deleted = removeTask(id);

  if (!deleted) {
    return res.status(404).json({
      message: "Tarefa nao encontrada."
    });
  }

  return res.status(204).send();
}
