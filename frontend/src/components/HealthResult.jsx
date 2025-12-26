import HumanBodyTwin from "./HumanBodyTwin";
import HealthScore from "./HealthScore";

function HealthResult({ result, inputs }) {
  // HARD GUARD — prevents ALL crashes
  if (!result) return null;

  const bp = inputs?.bp_sys ?? 120;     // fallback safe value
  const sleep = inputs?.sleep ?? 7;     // fallback safe value

  return (
    <div className="card result">
      <h2>Living Digital Twin</h2>

      <div style={{ display: "flex", gap: "40px", justifyContent: "center" }}>
        <HumanBodyTwin
          risk={result.health_risk}
          bp={bp}
          sleep={sleep}
        />
       <HealthScore
  score={result.health_score}
  risk={result.health_risk}
/>

      </div>
    </div>
  );
}

export default HealthResult;
