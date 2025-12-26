import "../styles.css";
import { ReactComponent as HumanBody } from "../assets/human-body.svg";

function getBodyColor(risk) {
  if (risk === "Healthy") return "#2ecc71";
  if (risk === "Moderate") return "#f1c40f";
  if (risk === "High Risk") return "#e67e22";
  return "#e74c3c";
}

function getHeartColor(bp) {
  if (bp < 120) return "#2ecc71";
  if (bp < 140) return "#f1c40f";
  if (bp < 160) return "#e67e22";
  return "#e74c3c";
}

function getLungColor(sleep) {
  if (sleep >= 7) return "#2ecc71";
  if (sleep >= 5) return "#3498db";
  return "#e74c3c";
}

function HumanBodyTwin({ risk, bp, sleep }) {
  const bodyColor = getBodyColor(risk);
  const heartColor = getHeartColor(bp);
  const lungColor = getLungColor(sleep);

  return (
    <div className="body-twin">
    <HumanBody
  style={{
    fill: bodyColor,
    opacity: 0.85,
    filter: `drop-shadow(0 0 10px ${bodyColor})`
  }}
/>


      {/* ORGAN OVERLAY */}
      <svg className="organ-overlay" width="200" height="400">
        <circle
          cx="100"
          cy="115"
          r="10"
          fill={heartColor}
          filter={`drop-shadow(0 0 8px ${heartColor})`}
        />
        <ellipse
          cx="88"
          cy="115"
          rx="8"
          ry="12"
          fill={lungColor}
          opacity="0.8"
        />
        <ellipse
          cx="112"
          cy="115"
          rx="8"
          ry="12"
          fill={lungColor}
          opacity="0.8"
        />
      </svg>

      <p className="risk-label">{risk}</p>
    </div>
  );
}

export default HumanBodyTwin;
