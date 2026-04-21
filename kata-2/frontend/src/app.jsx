import { useEffect, useState } from "react";
import {
  getTasks,
  createTask,
  deleteTask,
  updateTask
} from "./services/api";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState("Media");
  const [filter, setFilter] = useState("Todas");
  const [isLoading, setIsLoading] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [error, setError] = useState("");

  function resetForm() {
    setTitle("");
    setDescription("");
    setPriority("Media");
  }

  function openModal() {
    setError("");
    setIsModalOpen(true);
  }

  function closeModal() {
    if (isSubmitting) {
      return;
    }

    resetForm();
    setIsModalOpen(false);
  }

  async function loadTasks() {
    setIsLoading(true);
    setError("");

    try {
      const data = await getTasks(filter);
      setTasks(data);
    } catch (loadError) {
      setError(loadError.message);
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    loadTasks();
  }, [filter]);

  async function handleAdd() {
    const trimmedTitle = title.trim();

    if (!trimmedTitle) {
      setError("Digite um titulo para criar a tarefa.");
      return;
    }

    setIsSubmitting(true);
    setError("");

    try {
      await createTask({
        title: trimmedTitle,
        description: description.trim(),
        priority,
        status: "Pendente"
      });
      resetForm();
      setIsModalOpen(false);
      await loadTasks();
    } catch (createError) {
      setError(createError.message);
    } finally {
      setIsSubmitting(false);
    }
  }

  async function handleDelete(id) {
    setError("");

    try {
      await deleteTask(id);
      await loadTasks();
    } catch (deleteError) {
      setError(deleteError.message);
    }
  }

  async function handleTaskUpdate(id, updates) {
    setError("");

    try {
      await updateTask(id, updates);
      await loadTasks();
    } catch (updateError) {
      setError(updateError.message);
    }
  }

  return (
    <main className="bg-body-tertiary min-vh-100 py-5">
      <section className="container">
        <div className="card shadow-sm border-0">
          <div className="card-body p-4 p-lg-5">
            <div className="mb-4">
              <span className="badge text-bg-primary mb-3">Kata 2</span>
              <h1 className="h2 mb-2">Gerenciador de tarefas</h1>
              <p className="text-body-secondary mb-0">
                Cadastre, filtre, conclua e exclua tarefas em uma unica tela.
              </p>
            </div>

            <div className="d-flex justify-content-center mb-4">
              <div className="col-12 col-md-6 col-lg-4 d-grid">
                <button
                  className="btn btn-primary"
                  onClick={openModal}
                  type="button"
                >
                  Adicionar tarefa
                </button>
              </div>
            </div>

            <div className="mb-4">
              <p className="fw-semibold mb-2">Filtro</p>
              <div className="btn-group flex-wrap" role="group" aria-label="Filtro de tarefas">
                {["Todas", "Pendentes", "Concluidas"].map((option) => (
                  <button
                    key={option}
                    className={`btn ${
                      filter === option ? "btn-primary" : "btn-outline-primary"
                    }`}
                    onClick={() => setFilter(option)}
                    type="button"
                  >
                    {option}
                  </button>
                ))}
              </div>
            </div>

            {error ? <div className="alert alert-danger">{error}</div> : null}

            {isLoading ? (
              <div className="alert alert-secondary mb-0">Carregando tarefas...</div>
            ) : tasks.length === 0 ? (
              <div className="alert alert-secondary mb-0">
                Nenhuma tarefa encontrada para o filtro selecionado.
              </div>
            ) : (
              <div className="row g-3">
                {tasks.map((task) => (
                  <div className="col-12 col-md-6 col-xl-4" key={task.id}>
                    <article className="card h-100 shadow-sm task-card">
                      <div className="card-body d-flex flex-column task-card__body">
                        <div className="task-card__content">
                          <div className="d-flex justify-content-between align-items-start gap-2 mb-3">
                            <h2 className="h5 mb-0 task-card__title">{task.title}</h2>
                            <span
                              className={`badge flex-shrink-0 ${
                                task.status === "Concluida"
                                  ? "text-bg-success"
                                  : "text-bg-warning"
                              }`}
                            >
                              {task.status}
                            </span>
                          </div>

                          <p className="text-body-secondary mb-3 task-card__description">
                            {task.description || "Sem descricao informada."}
                          </p>

                          <p className="mb-0">
                            Prioridade: <strong>{task.priority || "Media"}</strong>
                          </p>
                        </div>

                        <div className="task-card__controls mt-auto">
                          <div className="mb-3">
                            <label className="form-label">Situacao</label>
                            <select
                              className="form-select"
                              value={task.status}
                              onChange={(event) =>
                                handleTaskUpdate(task.id, {
                                  status: event.target.value
                                })
                              }
                            >
                              <option value="Pendente">Pendente</option>
                              <option value="Concluida">Concluida</option>
                            </select>
                          </div>

                          <div className="mb-3">
                            <label className="form-label">Prioridade</label>
                            <select
                              className="form-select"
                              value={task.priority || "Media"}
                              onChange={(event) =>
                                handleTaskUpdate(task.id, {
                                  priority: event.target.value
                                })
                              }
                            >
                              <option value="Baixa">Baixa</option>
                              <option value="Media">Media</option>
                              <option value="Alta">Alta</option>
                            </select>
                          </div>

                          <button
                            className="btn btn-outline-danger w-100"
                            onClick={() => handleDelete(task.id)}
                            type="button"
                          >
                            Excluir
                          </button>
                        </div>
                      </div>
                    </article>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </section>

      {isModalOpen ? (
        <>
          <div className="modal fade show d-block" tabIndex="-1" role="dialog" aria-modal="true">
            <div className="modal-dialog modal-dialog-centered">
              <div className="modal-content">
                <div className="modal-header">
                  <h2 className="modal-title fs-5">Adicionar tarefa</h2>
                  <button
                    className="btn-close"
                    onClick={closeModal}
                    type="button"
                    aria-label="Fechar"
                  />
                </div>

                <div className="modal-body">
                  <div className="mb-3">
                    <label className="form-label">Nova tarefa</label>
                    <input
                      className="form-control"
                      value={title}
                      onChange={(event) => setTitle(event.target.value)}
                      placeholder="Ex.: Revisar documentacao"
                      maxLength={120}
                    />
                  </div>

                  <div className="mb-3">
                    <label className="form-label">Descricao da tarefa</label>
                    <textarea
                      className="form-control"
                      rows="3"
                      value={description}
                      onChange={(event) => setDescription(event.target.value)}
                      placeholder="Descreva os detalhes da tarefa"
                      maxLength={280}
                    />
                  </div>

                  <div>
                    <label className="form-label">Prioridade da tarefa</label>
                    <select
                      className="form-select"
                      value={priority}
                      onChange={(event) => setPriority(event.target.value)}
                    >
                      <option value="Baixa">Baixa</option>
                      <option value="Media">Media</option>
                      <option value="Alta">Alta</option>
                    </select>
                  </div>
                </div>

                <div className="modal-footer">
                  <button
                    className="btn btn-outline-secondary"
                    onClick={closeModal}
                    disabled={isSubmitting}
                    type="button"
                  >
                    Cancelar
                  </button>
                  <button
                    className="btn btn-primary"
                    onClick={handleAdd}
                    disabled={isSubmitting}
                    type="button"
                  >
                    {isSubmitting ? "Salvando..." : "Adicionar tarefa"}
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show" />
        </>
      ) : null}
    </main>
  );
}

export default App;
