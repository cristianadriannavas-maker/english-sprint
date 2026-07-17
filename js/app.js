const biblioteca = [

{

titulo:"Imagine Dragons - Believer",

canal:"Imagine Dragons",

frases:32

},

{

titulo:"Coldplay - Yellow",

canal:"Coldplay",

frases:45

},

{

titulo:"Benson Boone - Beautiful Things",

canal:"Benson Boone",

frases:37

}

];

function mostrarBiblioteca(){

const contenido=document.getElementById("contenido");

contenido.innerHTML="";

biblioteca.forEach(video=>{

contenido.innerHTML+=`

<div class="card">

<h2>${video.titulo}</h2>

<p>Canal: ${video.canal}</p>

<p>${video.frases} frases</p>

<button onclick="abrirLeccion('${video.titulo}')">

Abrir

</button>

</div>

`;

});

}

function abrirLeccion(nombre){

alert("Abriremos la lección:\n\n"+nombre);

}