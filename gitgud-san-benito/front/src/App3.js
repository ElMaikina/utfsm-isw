import {useState} from 'react';




function Appinfractshow() {
  const handleClick = () => {
    console.log('serpell se la come!');
  };
  const [rut, setRut] = useState('');
  

  return (
    <div className="create">
      <h2>Desplegar infractores</h2>
        
      <button onClick={handleClick}>Mostrar</button>
    </div>
  );
  
}

export default Appinfractshow;