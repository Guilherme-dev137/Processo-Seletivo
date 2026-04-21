let nextId = 4;

let tasks = [
  {
    id: 1,
    title: "Revisar requisitos do cliente",
    status: "Pendente",
    description: "Validar o escopo antes de iniciar o desenvolvimento.",
    priority: "Alta"
  },
  {
    id: 2,
    title: "Criar endpoint de listagem",
    status: "Concluida",
    description: "Disponibilizar a rota para listar as tarefas cadastradas.",
    priority: "Media"
  },
  {
    id: 3,
    title: "Montar tela principal",
    status: "Pendente",
    description: "Organizar formulario, filtro e cards das tarefas.",
    priority: "Baixa"
  }
];

function cloneTask(task) {
  return { ...task };
}

export function listTasks(filter = "Todas") {
  if (filter === "Pendentes") {
    return tasks.filter((task) => task.status === "Pendente").map(cloneTask);
  }

  if (filter === "Concluidas") {
    return tasks.filter((task) => task.status === "Concluida").map(cloneTask);
  }

  return tasks.map(cloneTask);
}

export function createTask({
  title,
  description = "",
  status = "Pendente",
  priority = "Media"
}) {
  const task = {
    id: nextId++,
    title,
    status,
    description,
    priority
  };

  tasks.push(task);
  return cloneTask(task);
}

export function updateTask(id, updates) {
  const task = tasks.find((item) => item.id === id);

  if (!task) {
    return null;
  }

  if (updates.title !== undefined) {
    task.title = updates.title;
  }

  if (updates.status !== undefined) {
    task.status = updates.status;
  }

  if (updates.description !== undefined) {
    task.description = updates.description;
  }

  if (updates.priority !== undefined) {
    task.priority = updates.priority;
  }

  return cloneTask(task);
}

export function removeTask(id) {
  const index = tasks.findIndex((item) => item.id === id);

  if (index === -1) {
    return false;
  }

  tasks.splice(index, 1);
  return true;
}

export function resetTasks(newTasks = []) {
  tasks = newTasks.map((task) => cloneTask(task));
  nextId =
    tasks.reduce((highest, task) => Math.max(highest, task.id), 0) + 1;
}
