import React, { useState } from 'react';
import './App.css';

const Appinfractsearch = () => {
  const [rut, setRut] = useState('');
  const [foundPerson, setFoundPerson] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/infractores/?rut=${rut}", {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const data = await response.json();
        if (data.length > 0) {
          // Se encontró a la persona
          const person = data[0]; // Suponiendo que solo se encuentra una persona con el RUT
          setFoundPerson(person);
        } else {
          // No se encontró a la persona
          setFoundPerson(null);
        }
      } else {
        console.error('Error al buscar la persona por RUT');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="create">
    <h2>Buscar Persona por RUT:</h2>
      <form onSubmit={handleSearch}>
        <div>
          <input
            type="text"
            name="rut"
            value={rut}
            onChange={(e) => setRut(e.target.value)}
          />
        </div>
        <button type="submit">Buscar</button>
      </form>

      {foundPerson && (
        <div className="result">
          <h2>Persona Encontrada:</h2>
          <table>
            <tr>
              <th>RUT</th>
              <th>Nombres</th>
              <th>Apellidos</th>
              <th>Fecha de Nacimiento</th>
            </tr>
            <tr>
              <td>{foundPerson.rut}</td>
              <td>{foundPerson.nombres}</td>
              <td>{foundPerson.apellidos}</td>
              <td>{foundPerson.fecha_de_nacimiento}</td>
              <td></td>
            </tr>
          </table>
        </div>
      )}

      {foundPerson === null && <p>No se encontró a la persona con el RUT proporcionado.</p>}
    </div>
  );
};

export default Appinfractsearch;
