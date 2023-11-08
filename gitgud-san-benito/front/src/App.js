import * as React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import Sanbenito1 from './pages/Sanbenito1';
import Sanbenito2 from './pages/Sanbenito2';
import Sanbenito3 from './pages/Sanbenito3';
export default function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="sanbenito1" element={<Sanbenito1 />} />
        <Route path="sanbenito2" element={<Sanbenito2 />} />
        <Route path="sanbenito3" element={<Sanbenito3 />} />
      </Routes>
    </div>
  );
}