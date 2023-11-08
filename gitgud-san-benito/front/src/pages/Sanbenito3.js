import {useState} from 'react';
import './Sanbenito.css';




function Appinfractshow() {
  const handleClick = () => {
    //console.log('serpell se la come!');
    fetch("http://127.0.0.1:8000/infractores/")
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json(); // or response.json() for JSON data
    })  
    .then(data => {
      console.log(data);
      //var infractores = JSON.stringify(data, null, 2);;
      //document.getElementById("listaDeInfractores").innerHTML = infractores;

      // Reference to the tableOfContents element
      var tableOfContents = document.getElementById("listaDeInfractores");

      // Create an HTML table
      var table = document.createElement("table");

      // Create the table header
      var headerRow = table.insertRow(0);
      var rutHeader = headerRow.insertCell(0);
      rutHeader.textContent = "RUT";
      var nombresHeader = headerRow.insertCell(1);
      nombresHeader.textContent = "Nombres";
      var apellidosHeader = headerRow.insertCell(2);
      apellidosHeader.textContent = "Apellidos";
      var fechaDeNacimientoHeader = headerRow.insertCell(3);
      fechaDeNacimientoHeader.textContent = "Fecha de Nacimiento";
      var numeroDeInfraccionesHeader = headerRow.insertCell(4);
      numeroDeInfraccionesHeader.textContent = "Número de Infracciones";

      // Create table rows for each object
      data.forEach(function (item, index) {
        var row = table.insertRow(index + 1);
        var rutCell = row.insertCell(0);
        rutCell.textContent = item.rut;
        var nombresCell = row.insertCell(1);
        nombresCell.textContent = item.nombres;
        var apellidosCell = row.insertCell(2);
        apellidosCell.textContent = item.apellidos;
        var fechaDeNacimientoCell = row.insertCell(3);
        fechaDeNacimientoCell.textContent = item.fecha_de_nacimiento;
        var numeroDeInfraccionesCell = row.insertCell(4);
        numeroDeInfraccionesCell.textContent = item.numero_de_infracciones;
      });

      // Append the table to the tableOfContents element
      tableOfContents.appendChild(table);
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    })

  };
  const [rut, setRut] = useState('');
    
  return (
    <div className="create">
      <h2>Desplegar infractores</h2>
      <button onClick={handleClick}>Mostrar</button>
      <p id="listaDeInfractores"></p>
    </div>
  );
  
}

export default Appinfractshow;