const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const copyBtn = document.getElementById("copy-btn");
const downloadBtn = document.getElementById("download-btn");

let generatedFilename = null; // Variable to store the generated PDF filename

sendBtn.addEventListener("click", async () => {
  const userMessage = userInput.value.trim();
  if (!userMessage) return;

  try {
    const response = await fetch("http://127.0.0.1:8000/story_gen/sGen", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ outline: userMessage }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let story = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      story += decoder.decode(value);
      document.getElementById("result").innerText = story;
    }

    // After generating the story, fetch the filename
    const saveResponse = await fetch("http://127.0.0.1:8000/story_gen/get_filename", {
      method: "GET",
    });

    if (!saveResponse.ok) {
      throw new Error(`HTTP error! Status: ${saveResponse.status}`);
    }

    const data = await saveResponse.json();
    generatedFilename = data.filename; // Store the filename for later use

  } catch (error) {
    console.error("Error calling API:", error);
    alert("Failed to generate the story. Check console for details.");
  }
});

copyBtn.addEventListener("click", () => {
  const resultText = document.getElementById("result").innerText;
  if (resultText) {
    navigator.clipboard.writeText(resultText).then(() => {
    }).catch(err => console.error("Failed to copy text:", err));
  }
});

downloadBtn.addEventListener("click", async () => {
  if (!generatedFilename) {
    alert("No story generated yet!");
    return;
  }

  try {
    const downloadUrl = `http://127.0.0.1:8000/story_gen/download_pdf/${generatedFilename}`;
    window.open(downloadUrl, "_blank"); // Open the PDF in a new tab for download
  } catch (error) {
    console.error("Error downloading PDF:", error);
    alert("Failed to download the PDF. Check console for details.");
  }
});
