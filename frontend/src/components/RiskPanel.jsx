function RiskPanel({ risk }) {
  if (!risk) return null;

  const explanation = {
    Healthy: "All observed parameters fall within clinically acceptable ranges.",
    Moderate: "Certain lifestyle or physiological indicators require monitoring.",
    "High Risk": "Multiple parameters indicate elevated health risk.",
    Critical: "Immediate medical attention is recommended."
  };

  return (
    <div className="card section">
      <h2>Clinical Interpretation</h2>
      <p>{explanation[risk]}</p>
    </div>
  );
}

export default RiskPanel;
