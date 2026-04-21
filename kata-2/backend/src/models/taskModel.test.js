import test from "node:test";
import assert from "node:assert/strict";
import {
  createTask,
  listTasks,
  removeTask,
  resetTasks,
  updateTask
} from "./taskModel.js";

test("createTask adds a new task with incremental id", () => {
  resetTasks([
    {
      id: 1,
      title: "Inicial",
      description: "Descricao inicial",
      status: "Pendente",
      priority: "Media"
    }
  ]);

  const created = createTask({
    title: "Nova tarefa",
    description: "Nova descricao",
    priority: "Alta"
  });

  assert.equal(created.id, 2);
  assert.equal(created.status, "Pendente");
  assert.equal(created.description, "Nova descricao");
  assert.equal(created.priority, "Alta");
  assert.equal(listTasks().length, 2);
});

test("listTasks filters pending and completed tasks", () => {
  resetTasks([
    {
      id: 1,
      title: "A",
      description: "Descricao A",
      status: "Pendente",
      priority: "Baixa"
    },
    {
      id: 2,
      title: "B",
      description: "Descricao B",
      status: "Concluida",
      priority: "Alta"
    }
  ]);

  assert.equal(listTasks("Pendentes").length, 1);
  assert.equal(listTasks("Concluidas").length, 1);
});

test("updateTask changes an existing task", () => {
  resetTasks([
    {
      id: 1,
      title: "Original",
      description: "Descricao original",
      status: "Pendente",
      priority: "Baixa"
    }
  ]);

  const updated = updateTask(1, {
    status: "Concluida",
    description: "Descricao atualizada",
    priority: "Alta"
  });

  assert.equal(updated.status, "Concluida");
  assert.equal(updated.description, "Descricao atualizada");
  assert.equal(updated.priority, "Alta");
});

test("removeTask deletes an existing task", () => {
  resetTasks([
    {
      id: 1,
      title: "Original",
      description: "Descricao original",
      status: "Pendente",
      priority: "Media"
    }
  ]);

  assert.equal(removeTask(1), true);
  assert.equal(listTasks().length, 0);
});
