import { useState } from "react";
import HealthForm from "./components/HealthForm";
import HealthResult from "./components/HealthResult";
import RiskPanel from "./components/RiskPanel";

function App() {
  const [result, setResult] = useState(null);
  const [inputs, setInputs] = useState(null);

  return (
    <div className="container">

      <div className="header">
        <h1>Digital Twin Health Assessment System</h1>
        <p>Clinical-grade human health evaluation using soft computing</p>
      </div>

      <div className="grid">
        <div className="card">
          <h2>Patient Parameters</h2>
          <HealthForm onResult={setResult} onInputs={setInputs} />
        </div>

        <div className="card">
          <h2>Health Summary</h2>
          <HealthResult result={result} inputs={inputs} />
        </div>
      </div>

      <div className="section">
        <RiskPanel risk={result?.health_risk} />
      </div>

      <div className="footer">
        ⚕️ This system provides clinical decision support and does not replace
        professional medical diagnosis.
      </div>

    </div>
  );
}

export default App;
