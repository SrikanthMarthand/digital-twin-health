function getColor(risk) {
  if (risk === "Healthy") return "#16a34a";
  if (risk === "Moderate") return "#facc15";
  if (risk === "High Risk") return "#f97316";
  return "#dc2626";
}

function HealthScore({ score, risk }) {
  if (score === undefined || score === null) return null;

  const color = getColor(risk);
  const radius = 70;
  const circumference = 2 * Math.PI * radius;
  const progress = (score / 100) * circumference;

  return (
    <div className="score-ring">
      <svg width="180" height="180">
        <circle
          cx="90"
          cy="90"
          r={radius}
          stroke="#e5e7eb"
          strokeWidth="12"
          fill="none"
        />
        <circle
          cx="90"
          cy="90"
          r={radius}
          stroke={color}
          strokeWidth="12"
          fill="none"
          strokeDasharray={circumference}
          strokeDashoffset={circumference - progress}
          strokeLinecap="round"
          transform="rotate(-90 90 90)"
        />
        <text
          x="50%"
          y="48%"
          textAnchor="middle"
          dominantBaseline="middle"
          fontSize="32"
          fontWeight="700"
          fill="#0f172a"
        >
          {Math.round(score)}
        </text>
        <text
          x="50%"
          y="62%"
          textAnchor="middle"
          fontSize="14"
          fill="#475569"
        >
          / 100
        </text>
      </svg>
      <p style={{ marginTop: "8px", fontWeight: "600" }}>Health Score</p>
    </div>
  );
}

export default HealthScore;
