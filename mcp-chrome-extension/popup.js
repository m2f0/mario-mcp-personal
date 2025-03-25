fetch("https://mcp.mariomayerle.com/resources/linkedin")
  .then(res => res.json())
  .then(data => {
    const profile = data.profile;
    const container = document.getElementById("profile");

    container.innerHTML = `
      <p><strong>${profile.name}</strong></p>
      <p>${profile.title}</p>
      <p>${profile.location}</p>
      <a href="https://www.linkedin.com/in/mariomayerlefilho/" target="_blank">Ver perfil</a>
    `;
  })
  .catch(err => {
    document.getElementById("profile").innerText = "Erro ao carregar dados.";
    console.error(err);
  });
