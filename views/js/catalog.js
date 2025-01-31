
document.querySelector('.dashboard').addEventListener('change', (event) => {
  const catalogContainer = document.querySelector('.catalog-container');
  const file = event.target.files[0];

  if (file) {
    const newItem = document.createElement('div');
    newItem.className = 'catalog-item';
    newItem.textContent = `Manual: ${file.name}`;
    newItem.dataset.file = file.name; // Asignar el nombre del archivo al atributo data-file

    catalogContainer.appendChild(newItem);
  }
});

document.querySelector('.catalog-container').addEventListener('click', (event) => {
  if (event.target.classList.contains('catalog-item')) {
      const file = event.target.dataset.file; // Obtener la URL del archivo
      if (file) {
          // Redirigir al visor, pasando la URL del archivo
          window.location.href = `pdfViewer.html?file=${file}`;
      }
  }
});
const logout = async () => {
  try{
    const data = {
      user: "logout"
    }
    const response = await fetch("https://mechanical-workshop-g3up.onrender.com/auth/signout", {
      method: "POST",
      headers: {
        "Content-Type": "application/json" 
        },
      body: JSON.stringify(data)
    });

    if (response.ok){
      window.location.replace("index.html");
    }

  }catch(error){
    console.log(error);
  }
}

