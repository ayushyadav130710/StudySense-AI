document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("answer-form");
    const input = document.getElementById("answer-input");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async(e) => {
        e.preventDefault();

        const answer = input.value.trim();
        if (!answer) return;

        // Reset UI
        resultDiv.className = "result";
        resultDiv.classList.remove("hidden");
        resultDiv.innerText = "⏳ Analyzing your answer...";

        try {
            const response = await fetch("/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `answer=${encodeURIComponent(answer)}`
            });

            const data = await response.json();

            if (data.status === "correct") {
                resultDiv.classList.add("success");
                resultDiv.innerText = data.feedback;
            } else {
                resultDiv.classList.add("error");
                resultDiv.innerText = data.feedback;
            }

        } catch (error) {
            resultDiv.classList.add("error");
            resultDiv.innerText = "❌ Something went wrong. Please try again.";
        }

        input.value = "";
    });
});