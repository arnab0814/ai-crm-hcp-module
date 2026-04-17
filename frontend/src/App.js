import React from "react";
import ChatBox from "./components/chatbox";
import Form from "./components/form";

function App() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI CRM HCP Module</h1>

      <div style={styles.grid}>
        <div style={styles.card}>
          <Form />
        </div>

        <div style={styles.card}>
          <ChatBox />
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "Inter, sans-serif",
    padding: "20px",
    background: "#f5f7fb",
    minHeight: "100vh"
  },
  title: {
    textAlign: "center",
    marginBottom: "20px"
  },
  grid: {
    display: "flex",
    gap: "20px"
  },
  card: {
    flex: 1,
    background: "#fff",
    padding: "20px",
    borderRadius: "12px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.05)"
  }
};

export default App;