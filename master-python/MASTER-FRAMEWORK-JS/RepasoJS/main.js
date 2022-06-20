let altura = 189;
let nombre = "aaron";
/*
// document.write(nombre)
// document.write(altura)

let concatenacion = nombre + " " + altura;
// document.write(concatenacion);

let datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>soy la caja de datos</h1>
    <h2>mi nombre es: ${nombre}</h2>
    <h3>mi altura es: ${altura}</h3>
`;

if (altura>=190) {
    datos.innerHTML += `<h1/>
        Eres una persona alta</h1>
    `
}else{
    datos.innerHTML += `<h1/>
        Eres una persona bajita</h1>`
}

for(let i=0; i<=2020; i++){
    //bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año:"+i;
}
*/

function MuestraMiNombre(nombre, altura){    
    let misDatos = `
        <h1>soy la caja de datos</h1>
        <h2>mi nombre es: ${nombre}</h2>
        <h3>mi altura es: ${altura}</h3>
    `;
    return misDatos;
}

function imprimir(){
    let datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Victor Robles",190);
}

imprimir();



document.write('<h1>Lista de nombres</h1>');
let nombres = ['aaron','paco','nathi'];
// let mostrar;
// for(let i=0;i<nombres.length;i++){
//     let mostrar = document.getElementById("datos");
//     mostrar.innerHTML += `Nombre: ${nombres[i]}<br>`;

// }
nombres.forEach((nombre)=> {
    document.write(nombre + '<br>');
});




