import { useState } from "react";

function HealthForm({ onResult, onInputs }) {
  const [form, setForm] = useState({
    age: "",
    bmi: "",
    bp_sys: "",
    sleep: "",
    stress: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      age: Number(form.age),
      bmi: Number(form.bmi),
      bp_sys: Number(form.bp_sys),
      sleep: Number(form.sleep),
      stress: Number(form.stress)
    };

    const response = await fetch("http://127.0.0.1:5000/assess-health", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    onInputs(payload);              // ✅ now defined
    onResult(data.digital_twin);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="age" placeholder="Age" onChange={handleChange} />
      <input name="bmi" placeholder="BMI" onChange={handleChange} />
      <input name="bp_sys" placeholder="Systolic BP" onChange={handleChange} />
      <input name="sleep" placeholder="Sleep Hours" onChange={handleChange} />
      <input name="stress" placeholder="Stress (0–1)" onChange={handleChange} />
      <button type="submit">Generate Digital Twin</button>
    </form>
  );
}

export default HealthForm;
