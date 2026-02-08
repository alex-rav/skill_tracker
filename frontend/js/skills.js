async function loadSkills() {
  try {
    const response = await fetch("/api/skills"); // относительный путь
    const skills = await response.json();

    const container = document.getElementById("skills-container");
    container.innerHTML = "";

    skills.forEach(skill => {
      const card = document.createElement("div");
      card.className = "card skill";

      card.innerHTML = `
        <span>${skill.name}</span>
        <progress value="${skill.level}" max="100"></progress>
        <span>${skill.level}%</span>
      `;

      container.appendChild(card);
    });
  } catch (err) {
    console.error("Ошибка загрузки навыков:", err);
  }
}

loadSkills();
