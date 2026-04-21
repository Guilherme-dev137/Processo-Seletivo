const API = "http://localhost:3000/api/tasks";

async function request(url, options = {}) {
  const response = await fetch(url, options);

  if (!response.ok) {
    let message = "Nao foi possivel concluir a requisicao.";

    try {
      const data = await response.json();
      message = data.message || message;
    } catch {
      message = response.statusText || message;
    }

    throw new Error(message);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

export async function getTasks(filter = "Todas") {
  const params = new URLSearchParams();

  if (filter && filter !== "Todas") {
    params.set("filter", filter);
  }

  const url = params.toString() ? `${API}?${params.toString()}` : API;
  return request(url);
}

export async function createTask(task) {
  return request(API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(task)
  });
}

export async function deleteTask(id) {
  return request(`${API}/${id}`, {
    method: "DELETE"
  });
}

export async function updateTask(id, updates) {
  return request(`${API}/${id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(updates)
  });
}
