import React, { useState } from "react";
import axios from "axios";

function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/interactions/agent", {
      text: input
    });

    const data = res.data;

    console.log("API Response:", data);

    // 🔥 Autofill FIRST (before UI update)
    if (data.action === "log" && data.data) {
      console.log("Autofill event sent", data.data);

      window.dispatchEvent(
        new CustomEvent("autofillForm", {
          detail: data.data
        })
      );
    }

    let displayText = "";

    if (data.action === "log") {
      displayText = "✅ Interaction logged successfully";
    } 
    else if (data.action === "get") {
      displayText = data.result.map(
        (item) =>
          `${item.doctor_name} - ${item.product} - Follow up: ${item.follow_up}`
      ).join("\n");
    } 
    else if (data.action === "edit") {
      displayText = "✏️ Interaction updated successfully";
    }
    else if (data.action === "summarize") {
      displayText = "🧠 " + data.result;
    }
    else if (data.action === "suggest") {
      displayText = "💡 " + data.result;
    }

    setMessages((prev) => [
      ...prev,
      { user: input, bot: displayText }
    ]);

    setInput("");

  } catch (error) {
    console.error("Error:", error);
  }
};

  return (
    <div>
      <h2>AI Chat</h2>

      <div style={styles.chatBox}>
        {messages.map((msg, i) => (
          <div key={i}>
            <div style={styles.userMsg}>{msg.user}</div>
            <pre style={styles.botMsg}>{msg.bot}</pre>
          </div>
        ))}
      </div>

      <div style={styles.inputRow}>
        <input
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type interaction..."
        />
        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  chatBox: {
    height: "300px",
    overflowY: "auto",
    marginBottom: "10px",
    padding: "10px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    background: "#fafafa"
  },
  userMsg: {
    textAlign: "right",
    background: "#007bff",
    color: "#fff",
    padding: "8px",
    borderRadius: "8px",
    margin: "5px 0"
  },
  botMsg: {
    textAlign: "left",
    background: "#e9ecef",
    padding: "8px",
    borderRadius: "8px",
    margin: "5px 0",
    whiteSpace: "pre-wrap"
  },
  inputRow: {
    display: "flex",
    gap: "10px"
  },
  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc"
  },
  button: {
    padding: "10px 15px",
    borderRadius: "8px",
    background: "#007bff",
    color: "#fff",
    border: "none",
    cursor: "pointer"
  }
};

export default ChatBox;