// --------------------------------------------------
// Get page elements
// --------------------------------------------------

const featureSelect = document.getElementById("feature");
const userInput = document.getElementById("userInput");
const generateBtn = document.getElementById("generateBtn");
const output = document.getElementById("output");

// --------------------------------------------------
// Backend URL
// --------------------------------------------------
// change this url if deploying the backend

const API_BASE_URL = "http://127.0.0.1:8000";

// --------------------------------------------------
// Button Click Event
// --------------------------------------------------

generateBtn.addEventListener("click", async () => {

    const selectedFeature = featureSelect.value;
    const inputText = userInput.value.trim();

    // Prevent empty input
    if (!inputText) {
        output.innerText = "Please enter some text.";
        return;
    }

    output.innerText = "Generating response...";

    try {

        let endpoint = "";
        let requestBody = {};

        // --------------------------------------------------
        // Topic Explanation
        // --------------------------------------------------

        if (selectedFeature === "explain") {

            endpoint = "/explain";

            requestBody = {
                topic: inputText
            };
        }

        // --------------------------------------------------
        // Question Answering
        // --------------------------------------------------

        else if (selectedFeature === "ask") {

            endpoint = "/ask";

            requestBody = {
                question: inputText
            };
        }

        // --------------------------------------------------
        // Summary
        // --------------------------------------------------

        else if (selectedFeature === "summary") {

            endpoint = "/summary";

            requestBody = {
                text: inputText
            };
        }

        // --------------------------------------------------
        // Quiz Generation
        // --------------------------------------------------

        else if (selectedFeature === "quiz") {

            endpoint = "/quiz";

            requestBody = {
                text: inputText
            };
        }

        // --------------------------------------------------
        // Learning Path
        // --------------------------------------------------

        else if (selectedFeature === "learning-path") {

            endpoint = "/learning-path";

            requestBody = {
                topic: inputText
            };
        }

        // --------------------------------------------------
        // API Request
        // --------------------------------------------------

        const response = await fetch(
            API_BASE_URL + endpoint,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(requestBody)
            }
        );

        const data = await response.json();

        // --------------------------------------------------
        // Display Results
        // --------------------------------------------------

        if (selectedFeature === "explain") {

            output.innerText =
                data.explanation;
        }

        else if (selectedFeature === "ask") {

            output.innerText =
                data.answer;
        }

        else if (selectedFeature === "summary") {

            output.innerText =
                data.summary;
        }

        else if (selectedFeature === "learning-path") {

            output.innerText =
                data.learning_path;
        }

        else if (selectedFeature === "quiz") {

            if (!data.quiz || data.quiz.length === 0) {

                output.innerText =
                    "No quiz questions generated.";

                return;
            }

            let quizOutput = "";

            data.quiz.forEach((question, index) => {

                quizOutput +=
                    `Question ${index + 1}\n`;

                quizOutput +=
                    `${question.question}\n\n`;

                question.options.forEach(option => {

                    quizOutput +=
                        `â¢ ${option}\n`;
                });

                quizOutput +=
                    `\nAnswer: ${question.answer}\n\n`;

                quizOutput +=
                    "--------------------------------\n\n";
            });

            output.innerText =
                quizOutput;
        }

    } catch (error) {

        console.error(error);

        output.innerText =
            "Unable to connect to the server.";
    }

});
