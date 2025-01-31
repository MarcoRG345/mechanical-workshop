document.getElementById('signup-form').addEventListener('submit', async (event) =>{
    event.preventDefault()
    const data = {
        username: document.querySelector('[name="username"]').value, // Selecciona por el atributo name
        password: document.querySelector('[name="password"]').value,
        mail: document.querySelector('[name="mail"]').value
    }
    try{
        const response = await fetch("http://192.168.100.50:5001/auth/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json" 
            },
            body: JSON.stringify(data)
        });
        dataResult = response.json();
        if (response.ok){
            window.location.href = "dashboard.html";
        }else {
            switch(dataResult["message"]){
                case "Missing username or password":
                    showMessage("Falta usuario y contraseña", "orange");
                    break;
                case "User already exists":
                    showMessage("El usuario ingresado ya existe", "red");
                    break;
            }
        }
    } catch(error){
        console.log("error", error);
    }
});

const showMessage = (message, color) => {
    elementMessage = document.getElementById('text-status');
    elementMessage.innerText = message;
    elementMessage.style.color = color;
    setTimeout(() => {elementMessage.style.display ="block"}, 2000);
}