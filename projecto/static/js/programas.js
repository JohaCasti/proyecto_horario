/* FUNCION PARA CREAR SEDES POR HERENCIA DE CENTROS */

function filtraDatos(id,s,n,i,t,d) {
    let url = `http://127.0.0.1:8000/api/conall/${n}/${i}/${t}/${d}/${id}`
    
    fetch(url)
    .then(r => r.json())
    .then(data => {
        console.log(data)
        // crear en el DOM apartir del id programa
        const createProgram = document.getElementById(s);
        createProgram.innerHTML  = "";    


        // Crea una opción por defecto
        const option = document.createElement("option");
        option.value = "0";
        option.text = "Seleccione";
        createProgram.appendChild(option);

        // iterar sobre mi data para agregar los option
        data.forEach((item) => {
            const createOption = document.createElement('option');
                createOption.value = item[1];
                createOption.text = item[0];
                createProgram.appendChild(createOption);
            
           // recibo la informacion debe guardarla e imprimirla en el select con id programa
        })
    })
    .catch(error => console.log(error))
}