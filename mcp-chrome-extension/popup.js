fetch("https://mcp.mariomayerle.com/resources/linkedin")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("profile");
    container.innerHTML = `
      <p><strong>${data.name}</strong></p>
      <p>${data.title}</p>
      <p>${data.location}</p>
      <a href="${data.url}" target="_blank">Ver perfil</a>
    `;
  })
  .catch(err => {
    document.getElementById("profile").innerText = "Erro ao carregar dados.";
    console.error(err);
  });
