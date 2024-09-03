import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faDownload  } from '@fortawesome/free-solid-svg-icons';
import './DynamicTable.css';
const DynamicTable = () => {
  const [rows, setRows] = useState([{ tempoInicial: '', tempoFinal: '', filename: '' }]);

  const handleAddRow = () => {
    setRows([...rows, { tempoInicial: '', tempoFinal: '', filename: '' }]);
  };

  const handleInputChange = (index, name, value) => {
    const newRows = [...rows];
    newRows[index][name] = value;
    setRows(newRows);
  };

  return (
    <div className="dynamic-table-container">
      <table className="dynamic-table">
        <thead>
          <tr>
            <th>Tempo Inicial</th>
            <th>Tempo Final</th>
            <th>Filename</th>
            <th>Download</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              <td>
                <input
                  type="text"
                  name="tempo inicial"
                  value={row.tempoInicial}
                  onChange={(event) => handleInputChange(index, "tempoInicial", event.target.value)}
                />
              </td>
              <td>
                <input
                  type="text"
                  name="tempo final"
                  value={row.tempoFinal}
                  onChange={(event) => handleInputChange(index, "tempoFinal", event.target.value)}
                />
              </td>
              <td>
                <input
                  type="text"
                  name="Arquivo"
                  value={row.filename}
                  onChange={(event) => handleInputChange(index, "filename", event.target.value)}
                />
              </td>
              <td>

                <div>
                  <a href={`http://192.168.0.111:5174/download_cut/${row.filename}`} download>
                  <button className="download-button"> <FontAwesomeIcon icon={faDownload}/></button> 
                  </a>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="add-row-button" onClick={handleAddRow}>
        <FontAwesomeIcon icon={faPlus} /> Adicionar Linha
      </button>
    </div>
  );
};

export default DynamicTable;
