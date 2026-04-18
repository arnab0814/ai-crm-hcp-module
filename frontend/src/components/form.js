import React, { useState, useEffect } from "react";
import axios from "axios";

function Form() {

  // ✅ Correct state
  const [form, setForm] = useState({
    doctor_name: "",
    notes: "",
    product: "",
    date: "",
    follow_up: ""
  });

  // ✅ Autofill listener
  useEffect(() => {
    const handler = (event) => {
      const data = event.detail;

      setForm({
        doctor_name: data.doctor_name || "",
        notes: data.notes || "",
        product: data.product || "",
        date: data.date || "",
        follow_up: data.follow_up || ""
      });
    };

    window.addEventListener("autofillForm", handler);

    return () => {
      window.removeEventListener("autofillForm", handler);
    };
  }, []);

  // ✅ Submit
  const handleSubmit = async () => {
    await axios.post("http://127.0.0.1:8000/interactions/", form);
    alert("✅ Interaction Saved");
  };

  return (
    <div>
      <h2>Log Interaction</h2>

      <div style={styles.form}>
        {Object.keys(form).map((key) => (
          <input
            key={key}
            placeholder={key}
            style={styles.input}
            value={form[key]}  // 🔥 IMPORTANT (missing in your code)
            onChange={(e) =>
              setForm({ ...form, [key]: e.target.value })
            }
          />
        ))}

        <button style={styles.button} onClick={handleSubmit}>
          Submit
        </button>
      </div>
    </div>
  );
}

const styles = {
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px"
  },
  input: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc"
  },
  button: {
    padding: "10px",
    borderRadius: "8px",
    background: "#28a745",
    color: "#fff",
    border: "none",
    cursor: "pointer"
  }
};

export default Form;