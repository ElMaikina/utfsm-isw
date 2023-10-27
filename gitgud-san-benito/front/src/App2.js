import {useState} from 'react';




function Appinfractsearch() {
  const handleClick = () => {
    console.log('serpell se la come?');
  };
  const [rut, setRut] = useState('');
  

  return (
    <div className="create">
      <h2>Buscar infracción por RUT</h2>
      <form>
        <label>RUT Infractor:</label>
        <input 
          type="text" 
          required 
          value={rut}
          onChange={(e) => setRut(e.target.value)}
        />
        
        <button onClick={handleClick}>Entregar</button>
      </form>
    </div>
  );
  
}

export default Appinfractsearch;
