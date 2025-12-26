import { useState } from "react";
import HealthForm from "./components/HealthForm";
import HealthResult from "./components/HealthResult";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <h1>🧠 Digital Twin – Human Health Assessment</h1>

      <div className="card">
        <HealthForm onResult={setResult} />
      </div>

      <HealthResult result={result} />
    </div>
  );
}

export default App;
