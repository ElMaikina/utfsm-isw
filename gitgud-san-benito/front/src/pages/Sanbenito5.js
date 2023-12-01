import React, { useState } from 'react';
import './Sanbenito.css';

const MyComponent = () => {
  const [formData, setFormData] = useState({
    fecha_emision: '',
    gravedad: '',
    acusado: '',
    acusante: '',
    patente_auto: '',
    multa: '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/infracciones/", {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Infraccion pagada:', data);
      } else {
        console.error('Error al borrar la infraccion');
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
      <h2>Pagar Infraccion</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Fecha de Emision: </label>
            <input
              type="date"
              name="fecha_emision"
              value={formData.fecha_emision}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Gravedad: </label>
            <input
              type="range"
              name="gravedad"
              min="1"
              max="11"
              value={formData.gravedad}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Acusado: </label>
            <input
              type="text"
              name="acusado"
              value={formData.acusado}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Acusante: </label>
            <input
              type="text"
              name="acusante"
              value={formData.acusante}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Patente del Auto: </label>
            <input
              type="text"
              name="patente_auto"
              value={formData.patente_auto}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Multa: </label>
            <input
              type="number"
              name="multa"
              value={formData.multa}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Pagar</button>
        </form>
      </div>
  );
};

export default MyComponent;
