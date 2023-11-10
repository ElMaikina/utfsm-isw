import React, { useState, useEffect } from 'react';
import './Sanbenito.css';

const ListPeople = () => {
  const [people, setPeople] = useState([]);
  const [filteredPeople, setFilteredPeople] = useState([]);
  const [rutFilter, setRutFilter] = useState('');

  useEffect(() => {
    // Realizar una solicitud GET inicial para obtener la lista completa de personas
    fetch('http://127.0.0.1:8000/infractores/')
      .then((response) => response.json())
      .then((data) => {
        setPeople(data);
        setFilteredPeople(data);
      })
      .catch((error) => console.error('Error:', error));
  }, []);

  const handleRutFilterChange = (e) => {
    const value = e.target.value;
    setRutFilter(value);

    // Filtrar la lista de personas por "rut" cuando el usuario ingrese un valor en el campo de filtro
    const filtered = people.filter((person) =>
      person.rut.toLowerCase().includes(value.toLowerCase())
    );
    setFilteredPeople(filtered);
  };

  return (
    <div className="list-people-container">
      <div class="menu">
      <a href='Sanbenito1' class='button'>Ingresar Infractor</a> 
      <a href='Sanbenito4' class='button'>Ingresar Evidencia</a>
      <a href='Sanbenito2' class='button'>Buscar Infractor</a>
      <a href='Sanbenito3' class='button'>Mostrar Infractores</a>
      </div>
      <h1>Municipalidad de San Benito</h1>
      <h2>Mostrar Infractores</h2>
      <table>
        <thead>
          <tr>
            <th>RUT</th>
            <th>Nombres</th>
            <th>Apellidos</th>
            <th>Fecha de Nacimiento</th>
            <th>Número de Infracciones</th>
          </tr>
        </thead>
        <tbody>
          {filteredPeople.map((person) => (
            <tr key={person.id}>
              <td>{person.rut}</td>
              <td>{person.nombres}</td>
              <td>{person.apellidos}</td>
              <td>{person.fecha_de_nacimiento}</td>
              <td>{person.numero_de_infracciones}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ListPeople;
