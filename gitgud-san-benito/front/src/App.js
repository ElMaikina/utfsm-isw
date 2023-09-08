import logo from './logo.svg';
import './App.css';
import {useState} from 'react';

function App() {
  
  const [rut, setRut] = useState('');
  const [patent, setPatent] = useState('');
  const [desc, setDesc] = useState('');
  const [severidad, setSev] = useState('leve');
  const [model, setModel] = useState('nunoki');

  return (
    <div className="create">
      <h2>Reportar Infraccion</h2>
      <form>
        <label>RUT Infractor:</label>
        <input 
          type="text" 
          required 
          value={rut}
          onChange={(e) => setRut(e.target.value)}
        />
        <label>Patente del vehiculo:</label>
        <input 
          type="text" 
          required 
          value={patent}
          onChange={(e) => setPatent(e.target.value)}
        />
        <label>Modelo del vehiculo:</label>
        <input 
          type="text" 
          required 
          value={model}
          onChange={(e) => setModel(e.target.value)}
        />
        <label>Descripcion de la Infraccion:</label>
        <textarea
          required
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
        ></textarea>
        <label>severidad:</label>
        <select
          value={severidad}
          onChange={(e) => setSev(e.target.value)}
        >
          <option value="leve">Leve</option>
          <option value="moderada">Moderada</option>
          <option value="grave">Grave</option>
        </select>
        <button>Entregar</button>
      </form>
    </div>
  );
  
}

export default App;
