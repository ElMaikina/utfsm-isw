import React, { useState } from 'react';
import './Sanbenito.css';

const MyComponent = () => {
  const [formData, setFormData] = useState({
    acusado: '',
    descripcion: '',
    foto: '',
    video: '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/evidencia/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Evidencia creada:', data);
      } else {
        console.error('Error al crear la evidencia');
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
      </div>
      <h1>Municipalidad de San Benito</h1>
      <h2>Ingresar Evidencia</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>RUT del Acusado: </label>
            <input
              type="text"
              name="acusado"
              value={formData.acusado}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Descripcion: </label>
            <input
              type="text"
              name="descripcion"
              value={formData.descripcion}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Foto: </label>
            <input
              type="file"
              name="foto"
              accept="image/*"
              value={formData.foto}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Video: </label>
            <input
              type="file"
              name="video"
              accept="video/*"
              value={formData.video}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Ingresar</button>
        </form>
      </div>
  );
};

export default MyComponent;
