import React, { useState } from 'react';
import './Sanbenito.css';

const MyComponent = () => {
  const [formData, setFormData] = useState({
    rut: '',
    nombres: '',
    apellidos: '',
    fecha_de_nacimiento: '',
    numero_de_infracciones: 0,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/infractores/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Persona creada:', data);
      } else {
        console.error('Error al crear la persona');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

  };

  return (
    <div className="create">
    <div class="menu">
    <a href='Sanbenito1' class='button'>Ingresar Infractor</a> 
    <a href='Sanbenito4' class='button'>Ingresar Evidencia</a>
    <a href='Sanbenito2' class='button'>Buscar Infractor</a>
    <a href='Sanbenito3' class='button'>Mostrar Infractores</a>
    <a href='Sanbenito5' class='button'>Pagar Infraccion</a>
    </div>
      <h1>Municipalidad de San Benito</h1>
      <h2>Ingresar Infractor</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>RUT: </label>
            <input
              type="text"
              name="rut"
              value={formData.rut}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Nombres: </label>
            <input
              type="text"
              name="nombres"
              value={formData.nombres}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Apellidos: </label>
            <input
              type="text"
              name="apellidos"
              value={formData.apellidos}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Fecha de Nacimiento: </label>
            <input
              type="date"
              name="fecha_de_nacimiento"
              value={formData.fecha_de_nacimiento}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Número de Infracciones: </label>
            <input
              type="number"
              name="numero_de_infracciones"
              value={formData.numero_de_infracciones}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Ingresar</button>
        </form>
      </div>
  );
};

export default MyComponent;
