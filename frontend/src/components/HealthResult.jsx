function HealthResult({ result }) {
  if (!result) return null;

  const riskClass =
    result.health_risk === "Healthy"
      ? "Healthy"
      : result.health_risk === "Moderate"
      ? "Moderate"
      : result.health_risk === "High Risk"
      ? "High"
      : "Critical";

  return (
    <div className="card result">
      <h2>Digital Twin Result</h2>
      <div className={`badge ${riskClass}`}>
        {result.health_risk}
      </div>
    </div>
  );
}

export default HealthResult;
