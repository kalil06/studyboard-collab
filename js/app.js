const STORAGE_KEY = "studyboard.tasks";

const initialTasks = [
  {
    id: crypto.randomUUID(),
    title: "Préparer la structure du rapport",
    owner: "Nadia",
    priority: "Haute",
    done: true
  },
  {
    id: crypto.randomUUID(),
    title: "Documenter les commandes Git",
    owner: "Youssef",
    priority: "Haute",
    done: false
  },
  {
    id: crypto.randomUUID(),
    title: "Vérifier l'interface responsive",
    owner: "Binôme",
    priority: "Moyenne",
    done: false
  }
];

const appState = {
  filter: "all",
  tasks: loadTasks()
};

const taskForm = document.querySelector("#taskForm");
const taskList = document.querySelector("#taskList");
const filterButtons = document.querySelectorAll(".filter-button");

function loadTasks() {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) {
    return initialTasks;
  }

  try {
    return JSON.parse(saved);
  } catch (error) {
    console.warn("Données locales invalides, réinitialisation.", error);
    return initialTasks;
  }
}

function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(appState.tasks));
}

function getVisibleTasks() {
  if (appState.filter === "done") {
    return appState.tasks.filter((task) => task.done);
  }
  if (appState.filter === "open") {
    return appState.tasks.filter((task) => !task.done);
  }
  return appState.tasks;
}

function renderMetrics() {
  const total = appState.tasks.length;
  const done = appState.tasks.filter((task) => task.done).length;
  const rate = total === 0 ? 0 : Math.round((done / total) * 100);

  document.querySelector("#totalTasks").textContent = total;
  document.querySelector("#doneTasks").textContent = done;
  document.querySelector("#progressRate").textContent = `${rate}%`;
}

function renderTasks() {
  const visibleTasks = getVisibleTasks();
  taskList.innerHTML = "";

  if (visibleTasks.length === 0) {
    const empty = document.createElement("li");
    empty.className = "empty-state";
    empty.textContent = "Aucune tâche ne correspond au filtre sélectionné.";
    taskList.append(empty);
    return;
  }

  visibleTasks.forEach((task) => {
    const item = document.createElement("li");
    item.className = `task-item ${task.done ? "is-done" : ""}`;
    item.innerHTML = `
      <input type="checkbox" ${task.done ? "checked" : ""} aria-label="Marquer ${task.title}" />
      <div>
        <strong class="task-title"></strong>
        <div class="task-meta">${task.owner}</div>
      </div>
      <span class="priority">${task.priority}</span>
    `;

    item.querySelector(".task-title").textContent = task.title;
    item.querySelector("input").addEventListener("change", () => toggleTask(task.id));
    taskList.append(item);
  });
}

function toggleTask(taskId) {
  appState.tasks = appState.tasks.map((task) =>
    task.id === taskId ? { ...task, done: !task.done } : task
  );
  saveTasks();
  render();
}

taskForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(taskForm);

  appState.tasks.unshift({
    id: crypto.randomUUID(),
    title: formData.get("taskTitle").trim(),
    owner: formData.get("taskOwner"),
    priority: formData.get("taskPriority"),
    done: false
  });

  taskForm.reset();
  saveTasks();
  render();
});

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((item) => item.classList.remove("is-active"));
    button.classList.add("is-active");
    appState.filter = button.dataset.filter;
    renderTasks();
  });
});

function render() {
  renderMetrics();
  renderTasks();
}

render();
