/**
 * Función que recibe el id del centro seleccionado y filtra los porgramas de acuerdo a ese id (centro),
 * ademas retorna la lista de programas para dicho centro.
 */


function filtraProgramas(id){
    console.log(id);
    let url = "http://127.0.0.1:8000/api/conall/Nombre/id_programa/programas/centro/"+id
    // let link = "http://127.0.0.1:8000/api/sumreg/programas/centros/5"
    // let api = link
    let link = "http://127.0.0.1:8000/api/conall/salon/id_salon/salon/centro/"+id
    

    fetch(url)
    .then(r => r.json())
    .then(data => {
        //console.log(data);
        // crear en el DOM apartir del id programa
        const createProgram = document.getElementById('programa');
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
    

    fetch(link)
    .then(result => result.json())
    .then( data => {
        // creamo en el DOM apartir del id salon
        const createSalon = document.getElementById('salona')
        createSalon.innerHTML  = ""; 

        //Crea una opción por defecto
        const option = document.createElement("option");
        option.value = "0";
        option.text = "Seleccione";
        createSalon.appendChild(option);

        // iterar sobre mi data para agregar los option
        data.forEach((item) => {
            console.log(item);
            
            const createOption = document.createElement('option');
            createOption.value = item[1];
            createOption.text = item[0];
            createSalon.appendChild(createOption);
        })

    })
    .catch(error => console.log(error))

}

function filtraFichas(id) {
    let url = "http://127.0.0.1:8000/api/conall/Nombre/id_ficha/ficha/programa/"+id
    // let link = "http://127.0.0.1:8000/api/sumreg/programas/centros/5"
    // let api = link
    

    fetch(url)
    .then(r => r.json())
    .then(data => {
        //console.log(data);
        // crear en el DOM apartir del id programa
        const createFichas = document.getElementById('fichas');
        createFichas.innerHTML  = "";        

        // Crea una opción por defecto
        const option = document.createElement("option");
        option.value = "0";
        option.text = "Seleccione";
        createFichas.appendChild(option);

        // iterar sobre mi data para agregar los option
        data.forEach((item) => {
            const createOption = document.createElement('option');
                createOption.value = item[1];
                createOption.text = item[0];
                createFichas.appendChild(createOption);
            
           
        })
        
        
    })
}
